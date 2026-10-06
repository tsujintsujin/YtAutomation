"""Job server for the Gemini Runner extension: hands out a video's image batches, files the results.

usage: python gemini_job.py output/<slug> [--accounts 0,1,2,3,4,5] [--only 3,7] [--downloads DIR]

Serves 127.0.0.1:8766 until every batch has its images or every account has hit its Gemini limit, then
exits (0 = all images in, 2 = some still missing; see <folder>/gemini-results.json). The extension in
Chrome polls /status every 30 s, so starting this script is all it takes to start a run (n8n does that).

Batches are --per prompts per message (default 2; 8 made Gemini stop halfway and ask). A batch that comes back short is re-asked
for just its missing images; after 3 failed tries an image is left for review.
"""
import argparse
import base64
import io
import json
import os
import re
import shutil
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from PIL import Image

LIMIT_RE = re.compile(r"limit|try again (later|tomorrow)|can.t (create|generate) more|come back|quota", re.I)
STALE_S = 15 * 60      # a batch handed out but not reported back in this long goes back in the queue

p = argparse.ArgumentParser()
p.add_argument("folder")
p.add_argument("--accounts", default="",
               help="comma-separated Gemini account emails; default: gemini-accounts.json")
p.add_argument("--only", default="", help="image ids to (re)generate, e.g. 2,17,40")
p.add_argument("--per", type=int, default=1, help="images per Gemini message (2+ makes Gemini merge scenes into one split picture)")
p.add_argument("--tabs", type=int, default=3, help="accounts working at once (7 at once tripped Google's unusual-traffic check)")
p.add_argument("--pause", default="30,60", help="random pause range in seconds after each image, per account")
p.add_argument("--stop-on-error", action="store_true",
               help="test mode: the first image that fails ends the whole run, so its cause can be looked at")
p.add_argument("--downloads", default=str(Path(os.environ["USERPROFILE"]) / "Downloads"))
a = p.parse_args()

folder = Path(a.folder).resolve()
slug = folder.name
segs = json.loads((folder / "script.json").read_text(encoding="utf-8"))["segments"]
prompt = {s["id"]: s["prompt"] for s in segs}
(folder / "img").mkdir(exist_ok=True)
dl_dir = Path(a.downloads) / "ytauto" / slug


def batch_text(ids):
    body = [f"Generate {len(ids)} separate images, one for each numbered prompt below. Each prompt is complete on its own."]
    body += [f"\n{n}. (image {i:03d}) {prompt[i]}" for n, i in enumerate(ids, 1)]
    return "\n".join(body)


# Same text as the reviewed batch files: fail loudly if they ever drift apart.
for f in sorted((folder / "batches").glob("batch-*.txt")):
    lo, hi = map(int, re.findall(r"img-(\d+)-(\d+)", f.name)[0])
    assert batch_text(list(range(lo, hi + 1))) == f.read_text(encoding="utf-8"), f"{f.name} differs from script.json"

have = {int(x.stem) for x in (folder / "img").glob("[0-9][0-9][0-9].*")}
wanted = [int(x) for x in a.only.split(",") if x] or [s["id"] for s in segs if s["id"] not in have]
queue = [wanted[k:k + a.per] for k in range(0, len(wanted), a.per)]  # list of id-lists
assigned = {}                                                        # batch key -> (acct, ids, t)
tries = {}                                                           # image id -> attempts
accounts = [x.strip() for x in a.accounts.split(",") if x.strip()] or \
    json.loads((Path(__file__).parent / "gemini-accounts.json").read_text(encoding="utf-8"))["accounts"]
RUN = time.strftime("%Y%m%d-%H%M%S")                                 # each run starts a fresh chat per account
limited = set()
halted = ""                                                          # --stop-on-error: why the run stopped
blocked_until = 0.0                                                  # Google's unusual-traffic page: hold all work
log = []
lock = threading.Lock()
key_seq = iter(range(1, 10 ** 6))


def ref(name):
    im = Image.open(folder / "refs" / name).convert("RGB")
    im.thumbnail((1600, 1600))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=88)
    return {"name": name, "b64": base64.b64encode(buf.getvalue()).decode()}


REFS = [ref("style-ref.jpg"), ref("geek-sheet.jpg"), ref("cat-sheet.jpg")]


def have_now():
    return {int(x.stem) for x in (folder / "img").glob("[0-9][0-9][0-9].*")}


def finished():
    return bool(halted) or not queue and not assigned or all(x in limited for x in accounts)


def save_results():
    missing = sorted(set(wanted) - {int(x.stem) for x in (folder / "img").glob("[0-9][0-9][0-9].*")})
    (folder / "gemini-results.json").write_text(json.dumps(
        {"missing": missing, "limited_accounts": sorted(limited), "log": log}, indent=1), encoding="utf-8")
    return missing


class H(BaseHTTPRequestHandler):
    def log_message(self, *x):
        pass

    def send(self, obj):
        b = json.dumps(obj).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        u = urlparse(self.path)
        with lock:
            now = time.time()
            for k, (acct, ids, t) in list(assigned.items()):          # requeue batches whose worker vanished
                if now - t > STALE_S:
                    del assigned[k]
                    queue.insert(0, ids)
            if u.path == "/status":
                return self.send({"active": not finished(), "slug": slug,
                                  "accounts": [x for x in accounts if x not in limited][:a.tabs],
                                  "pause": [int(x) for x in a.pause.split(",")], "run": RUN})
            if u.path == "/build":                                   # lets the extension see its own code changed
                code = (Path(__file__).parent / "gemini-extension" / "background.js").read_text(encoding="utf-8")
                return self.send({"build": re.search(r"const BUILD = '([^']+)';", code).group(1)})
            if u.path == "/refs":
                return self.send(REFS)
            if u.path == "/next":
                q = parse_qs(u.query)
                acct = q["acct"][0]
                code = (Path(__file__).parent / "gemini-extension" / "background.js").read_text(encoding="utf-8")
                if q.get("build", [None])[0] != re.search(r"const BUILD = '([^']+)';", code).group(1):
                    return self.send({})                       # stale extension: no work until it reloads itself
                if halted or acct in limited or not queue or time.time() < blocked_until:
                    return self.send({})
                ids = queue.pop(0)
                k = next(key_seq)
                assigned[k] = (acct, ids, now)
                print(f"-> acct {acct}: images {ids}", flush=True)
                return self.send({"batch": {"n": k, "ids": ids, "text": batch_text(ids)}})
        self.send({})

    def do_POST(self):
        r = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        if urlparse(self.path).path == "/report":                    # a window's status, for the log
            print(f"   {r.get('acct')} image {r.get('id')}: {r.get('state')}", flush=True)
            return self.send({})
        if urlparse(self.path).path == "/image":                     # full-size bytes straight from the page
            iid = int(r["id"])
            try:
                data = base64.b64decode(r["b64"])
                Image.open(io.BytesIO(data)).verify()                # refuse anything that isn't a real image
                for old in (folder / "img").glob(f"{iid:03d}.*"):
                    old.unlink()
                (folder / "img" / f"{iid:03d}.jpg").write_bytes(data)
                return self.send({"ok": True})
            except Exception as e:
                return self.send({"ok": False, "error": str(e)})
        if urlparse(self.path).path == "/diag":                      # evidence from a failed image
            d = folder / "diag"
            d.mkdir(exist_ok=True)
            stem = f"{time.strftime('%H%M%S')}_{r.get('id') or 0:03d}_{r.get('stage')}_{r['acct'].split('@')[0]}"
            png = r.pop("png", "")
            if png.startswith("data:image/png;base64,"):
                (d / f"{stem}.png").write_bytes(base64.b64decode(png.split(",", 1)[1]))
            else:
                r["png"] = png
            (d / f"{stem}.json").write_text(json.dumps(r, indent=1), encoding="utf-8")
            print(f"## evidence saved: diag/{stem}", flush=True)
            return self.send({})
        with lock:
            acct, k = r["acct"], r.get("n")
            _, ids, _ = assigned.pop(k, (acct, [], 0))
            got = []
            for f in r.get("files", []):
                if f["ok"] and next((folder / "img").glob(f"{f['id']:03d}.*"), None):   # written by /image
                    got.append(f["id"])
                    continue
                # Chrome fixes the extension to the real type (Gemini serves JPEG), so match any.
                src = next(dl_dir.glob(f"{f['id']:03d}.*"), None)
                if f["ok"] and src:
                    for old in (folder / "img").glob(f"{f['id']:03d}.*"):
                        old.unlink()
                    shutil.move(str(src), folder / "img" / src.name)
                    got.append(f["id"])
            missing = [i for i in ids if i not in got]
            stop = False
            if a.stop_on_error and ids and (missing or r.get("error")) and not LIMIT_RE.search(r.get("reply") or ""):
                global halted
                halted = f"acct {acct} image {ids}: {r.get('error') or 'no file'} | reply: {(r.get('reply') or '')[:150]}"
                print("!! STOPPED ON FIRST FAILURE: " + halted, flush=True)
            if "google.com/sorry" in (r.get("error") or ""):
                # Google's unusual-traffic check. Justin solves it by hand; meanwhile put the batch back
                # without counting a try, and hand out nothing for 3 minutes.
                global blocked_until
                blocked_until = time.time() + 180
                queue.insert(0, missing)
                print(f"!! CAPTCHA on acct {acct}: solve it in a Gemini tab; pausing 3 min", flush=True)
                missing = []
            if missing:
                if LIMIT_RE.search(r.get("reply") or "") and not got:
                    limited.add(acct)
                    stop = True
                    queue.insert(0, missing)
                else:
                    retry = []
                    for i in missing:
                        tries[i] = tries.get(i, 0) + 1
                        if tries[i] < 2:
                            retry.append(i)
                    # one at a time: a short batch is usually two scenes merged into one picture
                    queue.extend([i] for i in retry)
            log.append({"t": time.strftime("%H:%M:%S"), "acct": acct, "chat": r.get("chat"), "ids": ids, "got": got,
                        "error": r.get("error"), "reply": (r.get("reply") or "")[:200], "limited": stop})
            print(f"<- acct {acct} [build {r.get('build')}]{' (after refresh+retry)' if r.get('retried') else ''}: got {got} missing {missing}{' LIMIT' if stop else ''} {r.get('error') or ''}", flush=True)
            save_results()
        self.send({"stop": stop})


srv = ThreadingHTTPServer(("127.0.0.1", 8766), H)
threading.Thread(target=srv.serve_forever, daemon=True).start()
print(f"{slug}: {len(wanted)} images in {len(queue)} batches, accounts {accounts}. Waiting for the Chrome extension...", flush=True)
while not finished():
    time.sleep(5)
time.sleep(2)
srv.shutdown()
missing = save_results()
print(f"done: {len(wanted) - len(missing)} of {len(wanted)} images in img/; missing {missing}; limited accounts {sorted(limited)}")
sys.exit(2 if missing else 0)

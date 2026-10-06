"""Bridge between n8n and the Chrome extension (127.0.0.1:8766). n8n runs the image steps; the extension's
runner tab carries them out in Gemini. Nothing here decides the flow.

  n8n       POST /command {"name": ..., "args": {...}}  -> waits for the extension's answer, returns it
  runner    GET  /cmd                                   -> next command (held open up to 25 s, {} if none)
  runner    POST /result {"id": ..., ...}               -> the answer to a command
  runner    GET  /prompt?slug=&id=                      -> the full prompt text for one image
  runner    GET  /refs?slug=                            -> the 3 reference sheets (base64 JPEG)
  runner    POST /image?slug= {"id": N, "b64": ...}     -> writes output/<slug>/img/NNN.jpg (must open as an image)
  n8n       GET  /missing?slug=                         -> image numbers not yet in img/
  n8n       POST /claim {"slug"}, POST /release {"slug"} -> one n8n run per video: a claim fails while another run holds it
  n8n       GET  /accounts                              -> gemini-accounts.json: the 3 window accounts first, then the rest

The shared lists for the 3 window loops (each loop is its own n8n run, all at the same time). They live here so two
loops can never take the same image or account; every change happens under one lock.
  POST /pool/reset   {slug, accounts}      new run: no accounts on limit, nothing taken, no loops
  POST /pool/account {slug, win}           frees the loop's account, gives it the first one not on limit and not in
                                           use by another loop -> {account} (null: none left)
  POST /pool/limit   {slug, win, account}  notes the account as on limit
  POST /pool/image   {slug, win}           frees the loop's image, gives it the first missing image no other loop
                                           has -> {id} (null: none left)
  POST /pool/result  {slug, win, saved}    counts rounds in a row with nothing saved -> {noProgress}
  POST /pool/loop    {slug, win, state, detail}  a loop reports running / done / noAccounts / robotCheck / stuck
  GET  /pool/status?slug=                  -> {loops, missing, onLimit}

For the dashboard (dashboard.py). The bridge only watches the orders passing through it; it changes nothing:
  GET  /status                             -> {claims, wins (window id -> account), recent (last orders)}
  usage.jsonl                              one line per image saved {t, slug, image, account}, per limit reply
                                           {t, event: "limit", account, image} and per robot check {t, event: "robot", account}

usage: tts/.venv/Scripts/python bridge.py      (start_bridge.cmd starts it in its own window if it isn't up)
"""
import base64
import io
import json
import select
import socket
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from PIL import Image

OUT = Path(__file__).parent / "output"
lock = threading.Condition()
queue = []            # commands waiting for the runner
results = {}          # command id -> answer
claims = {}           # slug -> time of the run's last activity (one n8n run per video at a time)
STALE = 3 * 3600      # a claim with no activity for 3 h belongs to a run that died
pools = {}            # slug -> the shared lists of that video's window loops (see the top of this file)
USAGE = Path(__file__).parent / "usage.jsonl"
wins = {}             # window id -> account in it, learned from openWindows / switchAccounts / newChat
recent = []           # the last 60 orders: {t, name, ok, info}
logged = set()        # limit / robot replies already written to usage.jsonl (look sees the same reply every 5 s)


def watch(name, args, ans):
    """Note what an order did: who is in which window, images saved, limit replies, robot checks."""
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    if name == "setup":
        wins.clear()
        logged.clear()
    for acct, win in (ans.get("opened") or {}).items():
        wins[str(win)] = acct
    if name in ("switchAccounts", "newChat"):
        for j in args.get("jobs", []):
            wins[str(j["windowId"])] = j["account"]
    if name == "saveImages":
        by_id = {j["id"]: str(j["windowId"]) for j in args.get("jobs", [])}
        for i in ans.get("saved", []):
            lines.append({"t": t, "slug": args.get("slug"), "image": i, "account": wins.get(by_id.get(i))})
    for win, f in (ans.get("found") or ans.get("sent") or {}).items():
        acct = wins.get(str(win))
        if f.get("limit") and (acct, f.get("forImage")) not in logged:
            logged.add((acct, f.get("forImage")))
            lines.append({"t": t, "event": "limit", "account": acct, "image": f.get("forImage")})
        if f.get("robotCheck") and (acct, "robot") not in logged:
            logged.add((acct, "robot"))
            lines.append({"t": t, "event": "robot", "account": acct})
    if lines:
        with USAGE.open("a", encoding="utf-8") as fh:
            fh.writelines(json.dumps(x) + "\n" for x in lines)
    info = ans.get("error") or (f"saved {ans['saved']}" if "saved" in ans else "")
    recent.append({"t": t, "name": name, "ok": bool(ans.get("ok")), "info": str(info)[:160]})
    del recent[:-60]


def pool(slug):
    return pools.setdefault(slug, {"accounts": [], "onLimit": {}, "account": {}, "image": {}, "noProgress": {},
                                   "loops": {}})


def pool_post(path, r):
    """The /pool/... changes. Called with the lock held."""
    slug, win = r["slug"], str(r.get("win", ""))
    if path == "/pool/reset":
        pools.pop(slug, None)
        p = pool(slug)
        p["accounts"] = list(r["accounts"])
        return {"ok": True}
    p = pool(slug)
    if path == "/pool/account":
        p["account"].pop(win, None)
        busy = set(p["account"].values())
        nxt = next((a for a in p["accounts"] if a not in p["onLimit"] and a not in busy), None)
        if nxt:
            p["account"][win] = nxt
        return {"ok": True, "account": nxt}
    if path == "/pool/limit":
        p["onLimit"][r["account"]] = time.strftime("%Y-%m-%d %H:%M:%S")
        if p["account"].get(win) == r["account"]:
            p["account"].pop(win)
        return {"ok": True, "onLimit": list(p["onLimit"])}
    if path == "/pool/image":
        p["image"].pop(win, None)
        taken = set(p["image"].values())
        nxt = next((i for i in missing(slug) if i not in taken), None)
        if nxt is not None:
            p["image"][win] = nxt
        return {"ok": True, "id": nxt}
    if path == "/pool/result":
        n = 0 if r.get("saved") else p["noProgress"].get(win, 0) + 1
        p["noProgress"][win] = n
        return {"ok": True, "noProgress": n}
    if path == "/pool/loop":
        p["loops"][win] = {"state": r["state"], "detail": r.get("detail", ""), "at": time.strftime("%H:%M:%S")}
        if r["state"] != "running":                          # an ended loop holds nothing
            p["image"].pop(win, None)
            p["account"].pop(win, None)
        return {"ok": True}
    raise KeyError(path)


def folder(slug):
    f = (OUT / slug).resolve()
    assert f.parent == OUT.resolve() and (f / "script.json").exists(), f"no video {slug}"
    return f


def segments(slug):
    return json.loads((folder(slug) / "script.json").read_text(encoding="utf-8"))["segments"]


def missing(slug):
    have = {int(p.stem) for p in (folder(slug) / "img").glob("[0-9][0-9][0-9].*")}
    return [s["id"] for s in segments(slug) if s["id"] not in have]


def prompt_text(slug, i):                    # same text as gemini_job.py's batch_text([i])
    p = {s["id"]: s["prompt"] for s in segments(slug)}[i]
    return "\n".join(["Generate 1 separate images, one for each numbered prompt below. Each prompt is complete on its own.",
                      f"\n1. (image {i:03d}) {p}"])


def refs(slug):
    out = []
    for name in ("style-ref.jpg", "geek-sheet.jpg", "cat-sheet.jpg"):
        im = Image.open(folder(slug) / "refs" / name).convert("RGB")
        im.thumbnail((1600, 1600))
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=88)
        out.append({"name": name, "b64": base64.b64encode(buf.getvalue()).decode()})
    return out


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, obj, code=200):
        b = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(b)

    def gone(self):
        """True when the other side has closed the connection (it reads as end-of-file)."""
        r, _, _ = select.select([self.connection], [], [], 0)
        if not r:
            return False
        try:
            return self.connection.recv(1, socket.MSG_PEEK) == b""
        except OSError:
            return True

    def do_GET(self):
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        try:
            if u.path == "/cmd":
                # Hand a command only to a runner that is still there: a runner tab closed by an extension reload
                # leaves its request waiting here, and a command given to it is lost.
                with lock:
                    for _ in range(25):
                        if queue or self.gone():
                            break
                        lock.wait(timeout=1)
                    if self.gone():
                        return
                    return self.send(queue.pop(0) if queue else {})
            if u.path == "/missing":
                return self.send({"missing": missing(q["slug"])})
            if u.path == "/prompt":
                return self.send({"text": prompt_text(q["slug"], int(q["id"]))})
            if u.path == "/refs":
                return self.send(refs(q["slug"]))
            if u.path == "/accounts":
                a = json.loads((Path(__file__).parent / "gemini-accounts.json").read_text(encoding="utf-8"))
                return self.send({"accounts": a["accounts"] + [x for x in a["pool"] if x not in a["accounts"]]})
            if u.path == "/pool/status":
                with lock:
                    p = pool(q["slug"])
                    return self.send({"loops": p["loops"], "missing": len(missing(q["slug"])),
                                      "onLimit": list(p["onLimit"])})
            if u.path == "/status":
                with lock:
                    return self.send({"claims": {k: round(time.time() - v) for k, v in claims.items()},
                                      "wins": dict(wins), "recent": list(recent)})
            if u.path == "/health":
                return self.send({"ok": True})
        except Exception as e:
            return self.send({"error": str(e)}, 500)
        self.send({"error": "unknown path"}, 404)

    def do_POST(self):
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        r = json.loads(self.rfile.read(int(self.headers["Content-Length"])) or b"{}")
        if u.path == "/command":
            cid = uuid.uuid4().hex
            with lock:
                for k in claims:                                      # the run is alive
                    claims[k] = time.time()
                queue.append({"id": cid, "name": r["name"], "args": r.get("args", {})})
                lock.notify_all()
                got = lock.wait_for(lambda: cid in results, timeout=float(r.get("timeout", 900)))
                if not got:
                    queue[:] = [c for c in queue if c["id"] != cid]
                    print(f"{time.strftime('%H:%M:%S')} {r['name']}: no answer", flush=True)
                    return self.send({"ok": False, "error": "no answer from the extension (is its runner tab open?)"})
                ans = results.pop(cid)
                try:
                    watch(r["name"], r.get("args", {}), ans)
                except Exception as e:                               # watching must never break an order
                    print(f"watch failed: {e}", flush=True)
            print(f"{time.strftime('%H:%M:%S')} {r['name']}: {json.dumps(ans)[:300]}", flush=True)
            return self.send(ans)
        if u.path.startswith("/pool/"):
            try:
                with lock:
                    return self.send(pool_post(u.path, r))
            except Exception as e:
                return self.send({"ok": False, "error": f"{type(e).__name__}: {e}"})
        if u.path == "/claim":
            with lock:
                t = claims.get(r["slug"])
                if t and time.time() - t < STALE:
                    return self.send({"ok": False, "error": "another run is already working on " + r["slug"]})
                claims[r["slug"]] = time.time()
            return self.send({"ok": True})
        if u.path == "/release":
            with lock:
                claims.pop(r.get("slug"), None)
            return self.send({"ok": True})
        if u.path == "/result":
            with lock:
                results[r["id"]] = r
                lock.notify_all()
            return self.send({})
        if u.path == "/image":
            try:
                data = base64.b64decode(r["b64"])
                Image.open(io.BytesIO(data)).verify()              # refuse anything that isn't a real image
                img = folder(q["slug"]) / "img"
                img.mkdir(exist_ok=True)
                for old in img.glob(f"{int(r['id']):03d}.*"):
                    old.unlink()
                (img / f"{int(r['id']):03d}.jpg").write_bytes(data)
                return self.send({"ok": True})
            except Exception as e:
                return self.send({"ok": False, "error": str(e)})
        self.send({"error": "unknown path"}, 404)


if __name__ == "__main__":
    print("bridge on 127.0.0.1:8766", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8766), H).serve_forever()

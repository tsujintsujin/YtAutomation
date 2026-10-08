"""YtAutomation dashboard on http://127.0.0.1:8770 (dashboard.html). Reads output/, the bridge and the n8n API;
its buttons do only what Justin would do by hand:

  Start   POST n8n /webhook/yt-render {slug, voice}       (same as HANDOFF section 7)
  Stop    n8n: stop every running "YouTube Render" execution; bridge: release the claim, then the runner's `setup`
          order closes every Gemini window and tab
  Redo    move img/NNN.* and img_clean/NNN.jpg into img/redo/ (the next run makes that image again; only for videos
          without an MP4)
  Delete  remove the whole output/<slug>/ folder, permanently; only after typing the name, never during a run
  TheJobStash Start  close any old scorer/tunnel windows, then start both fresh (what scorer.cmd does, minus n8n)

Image counts per account come from usage.jsonl, which the bridge writes as it saves images.
The n8n API key is read from the Credentials folder and never leaves this process.

usage: tts/.venv/Scripts/python dashboard.py     (start_dashboard.cmd starts it in its own window)
"""
import io
import json
import os
import re
import shutil
import subprocess
import time
import urllib.request
from collections import defaultdict
from datetime import date, datetime, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from PIL import Image

HERE = Path(__file__).parent
OUT = HERE / "output"
CACHE = HERE / "dashboard-cache"
PORT = 8770
N8N = "http://127.0.0.1:5678"
BRIDGE = "http://127.0.0.1:8766"
WORKFLOW = "ytrender00000001"
JOBSTASH = Path(r"D:\AIO Freelance\TheJobStash")
CLOUDFLARED = Path(os.environ["APPDATA"]) / r"npm\node_modules\cloudflared\bin\cloudflared.exe"
KEY = Path(r"D:\AIO Freelance\Credentials\n8n\api-key.txt").read_text(encoding="utf-8").strip()
SLUG = re.compile(r"^[a-z0-9][a-z0-9_-]*$")
IMG = re.compile(r"^(\d{3})\.(jpg|jpeg|png|webp)$", re.I)
TYPES = {".mp4": "video/mp4", ".srt": "text/plain; charset=utf-8", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
         ".png": "image/png", ".webp": "image/webp", ".html": "text/html; charset=utf-8"}


# ---------- outside services ----------

def http(url, method="GET", body=None, headers=None, timeout=5):
    req = urllib.request.Request(url, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Content-Type": "application/json", **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read() or b"{}")


def n8n(path, method="GET", body=None, timeout=10):
    return http(N8N + "/api/v1" + path, method, body, {"X-N8N-API-KEY": KEY}, timeout)


def up(url):
    try:
        urllib.request.urlopen(url, timeout=2)
        return True
    except urllib.error.HTTPError:
        return True                      # it answered
    except Exception:
        return False


def n8n_state():
    """'running' once n8n can take a run, 'starting' while it answers but its database is still loading,
    'restarting' for a while after the dashboard restarted it, else 'down'."""
    try:
        urllib.request.urlopen(N8N + "/healthz/readiness", timeout=2)
        return "running"
    except urllib.error.HTTPError:
        return "starting"
    except Exception:
        if up(N8N + "/healthz"):
            return "starting"
        return "restarting" if time.time() - _n8n_restarted < 300 else "down"


_n8n_restarted = 0                       # when the dashboard last restarted n8n


def n8n_restart():
    """End n8n (also when it is frozen: process alive, port open, never answers) and start it again the way
    start_dashboard.cmd does. Refused while a video run is going, since that would kill the run."""
    global _n8n_restarted
    if n8n_state() == "running" and any(r["live"] for r in runs(10)):
        raise ValueError("a run is going; stop it first")
    if time.time() - _n8n_restarted < 60:
        raise ValueError("already restarting; give it a few minutes")
    # n8n's own process and its task runner both run from the global npm n8n folder
    subprocess.run(["powershell", "-NoProfile", "-Command",
                    "Get-CimInstance Win32_Process -Filter \"Name='node.exe'\" | "
                    "Where-Object { $_.CommandLine -match 'node_modules\\\\n8n\\\\' } | "
                    "ForEach-Object { Stop-Process -Id $_.ProcessId -Force }"], capture_output=True, timeout=30)
    si = subprocess.STARTUPINFO()
    si.dwFlags, si.wShowWindow = subprocess.STARTF_USESHOWWINDOW, 7          # SW_SHOWMINNOACTIVE
    subprocess.Popen(["cmd", "/c", r"title n8n :5678 && .\start_n8n.cmd"], cwd=HERE.parent / "n8n",
                     creationflags=subprocess.CREATE_NEW_CONSOLE, startupinfo=si)
    _n8n_restarted = time.time()
    return {"message": "restarting n8n; it takes about 3 minutes to be ready"}


def ok(url):
    try:
        urllib.request.urlopen(url, timeout=2)
        return True
    except Exception:
        return False


_js_started = 0                          # when the dashboard last started TheJobStash's parts


def jobstash():
    """TheJobStash's scorer (py_server.py :3300) and its tunnel (cloudflared's /ready, metrics on 20241-20245),
    which are what let thejobstash.com take resumes. n8n is the same n8n as above."""
    s = {"scorer": ok("http://127.0.0.1:3300/healthz"),
         "tunnel": any(ok(f"http://127.0.0.1:{p}/ready") for p in range(20241, 20246))}
    s["starting"] = not (s["scorer"] and s["tunnel"]) and time.time() - _js_started < 30
    return s


def bridge_status():
    try:
        return http(BRIDGE + "/status", timeout=3)
    except Exception:
        return None


# ---------- videos ----------

_scripts = {}                            # path -> (mtime, script)


def script(d):
    f = d / "script.json"
    if not f.exists():
        return None
    m = f.stat().st_mtime
    if _scripts.get(f, (None,))[0] != m:
        try:
            _scripts[f] = (m, json.loads(f.read_text(encoding="utf-8-sig")))
        except ValueError as e:                     # one broken script.json must not take the whole page down
            _scripts[f] = (m, {"segments": [], "error": f"script.json can't be read: {e}"})
    return _scripts[f][1]


def images(d):
    """{id: Path} of the images made so far (img/NNN.*)."""
    out = {}
    if (d / "img").is_dir():
        for p in (d / "img").iterdir():
            m = IMG.match(p.name)
            if m and p.is_file():
                out[int(m[1])] = p
    return out


def thumbnails(d):
    """The video's YouTube thumbnails: [{id, text, scene, v}] from thumbnails.json, v = mtime of thumbs/thumb-N.jpg
    (None until it is made)."""
    f = d / "thumbnails.json"
    try:
        ts = json.loads(f.read_text(encoding="utf-8"))["thumbnails"] if f.exists() else []
    except (ValueError, KeyError):
        return []
    ok = approved(d)
    out = []
    for t in ts:
        p = d / "thumbs" / f"thumb-{t['id']}.jpg"
        out.append({"id": t["id"], "text": t.get("text", ""), "scene": t.get("scene", ""),
                    "v": int(p.stat().st_mtime) if p.exists() else None, "ok": t["id"] in ok})
    return out


def approved(d):
    """Thumbnail ids Justin ticked for YouTube (at most 3), from thumbs-approved.json."""
    try:
        return json.loads((d / "thumbs-approved.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []


def folder(slug):
    if not SLUG.match(slug or ""):
        raise ValueError("bad video name")
    d = (OUT / slug).resolve()
    if d.parent != OUT.resolve() or not d.is_dir():
        raise ValueError("no such video")
    return d


def story_title(d):
    """A story waiting for approval (script.md, no script.json yet) is titled by its opening question."""
    f = d / "script.md"
    if not f.exists():
        return None
    first = f.read_text(encoding="utf-8").strip().split("?")[0]
    return first + "?" if first and len(first) < 120 else None


def video_summary(d):
    s = script(d)
    imgs = images(d)
    mp4 = d / f"{d.name}.mp4"
    return {
        "slug": d.name,
        "title": (s or {}).get("title") or story_title(d) or d.name.replace("-", " ").capitalize(),
        "voice": (s or {}).get("voice", "am_liam"),
        "script": s is not None,
        "scriptError": (s or {}).get("error"),
        "total": len(s["segments"]) if s else len(imgs),
        "made": len(imgs) if not s else sum(1 for x in s["segments"] if x["id"] in imgs),
        "voiceDone": (d / "voice.wav").exists() and (d / "timings.json").exists(),
        "srt": (d / f"{d.name}.srt").exists(),
        "mp4": mp4.exists(),
        "mp4Size": mp4.stat().st_size if mp4.exists() else 0,
        "changed": max([d.stat().st_mtime] + [p.stat().st_mtime for p in imgs.values()]),
        "lastImage": max([p.stat().st_mtime for p in imgs.values()], default=0),
        "firstId": min(imgs, default=None),
        "thumbs": thumbnails(d),
    }


def videos():
    """Every output/<slug>/ that is a video (has script.json, its MP4, or a story to approve in script.md);
    "_" folders are tests."""
    return [video_summary(d) for d in OUT.iterdir()
            if d.is_dir() and not d.name.startswith("_")
            and any((d / f).exists() for f in ("script.json", f"{d.name}.mp4", "script.md"))]


# ---------- n8n runs ----------

RUNS_CACHE = CACHE / "runs.json"
_runs = json.loads(RUNS_CACHE.read_text(encoding="utf-8")) if RUNS_CACHE.exists() else {}


def first_json(rd, node):
    try:
        return rd[node][-1]["data"]["main"][0][0]["json"]
    except (KeyError, IndexError, TypeError):
        return None


def run_details(eid):
    """slug / outcome / reason of a finished run, read once from its execution data and kept in runs.json."""
    if eid in _runs:
        return _runs[eid]
    rd = n8n(f"/executions/{eid}?includeData=true", timeout=30)["data"]["resultData"]["runData"]
    slug = ((first_json(rd, "Read video name") or {}).get("slug") or (first_json(rd, "Pick that video") or {}).get("slug")
            or ((first_json(rd, "Start: make a video") or {}).get("body") or {}).get("slug"))
    fail = first_json(rd, "Collect failure")
    if "MP4 done" in rd:
        outcome, reason = "made", "MP4 made"
    elif fail:
        outcome, reason = "failed", f"{fail.get('stage', '')}: {fail.get('error', '')}".strip(": ")
    elif "Wait for next try" in rd:
        outcome, reason = "limits", "every account on limit, waiting for the 5-hour timer"
    elif "Stop: already in progress" in rd:
        outcome, reason = "skipped", "another run already had this video"
    elif not slug:
        outcome, reason = "idle", "timer check: nothing waiting"
    else:
        outcome, reason = "", ""
    _runs[eid] = {"slug": slug, "outcome": outcome, "reason": reason}
    CACHE.mkdir(exist_ok=True)
    RUNS_CACHE.write_text(json.dumps(_runs), encoding="utf-8")
    return _runs[eid]


def runs(limit=40):
    # n8n's plain list leaves out running executions: ask for those by status too
    got = {}
    for q in ("", "&status=running", "&status=waiting"):
        for e in n8n(f"/executions?workflowId={WORKFLOW}&limit={limit}{q}")["data"]:
            got[e["id"]] = e
    out = []
    for e in sorted(got.values(), key=lambda e: int(e["id"]), reverse=True)[:limit]:
        live = e["status"] in ("running", "waiting", "new")
        d = {"slug": None, "outcome": "running", "reason": ""} if live else run_details(e["id"])
        if not live and e["status"] == "canceled" and not d["outcome"]:
            d = dict(d, outcome="stopped", reason="stopped by hand")
        out.append({"id": e["id"], "status": e["status"], "mode": e["mode"], "startedAt": e["startedAt"],
                    "stoppedAt": e["stoppedAt"], "live": live, **d})
    return out


# ---------- accounts ----------

def usage():
    if not (HERE / "usage.jsonl").exists():
        return []
    rows = []
    for line in (HERE / "usage.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            rows.append(json.loads(line))
        except ValueError:
            pass
    return rows


def accounts(wins):
    cfg = json.loads((HERE / "gemini-accounts.json").read_text(encoding="utf-8"))
    order = cfg["accounts"] + [a for a in cfg["pool"] if a not in cfg["accounts"]]
    days = [(date.today() - timedelta(days=i)).isoformat() for i in range(6, -1, -1)]
    per = defaultdict(lambda: defaultdict(int))
    limits, robots = defaultdict(list), []
    for r in usage():
        if r.get("event") == "limit":
            limits[r.get("account")].append(r["t"])
        elif r.get("event") == "robot":
            robots.append(r)
        else:
            per[r.get("account")][r["t"][:10]] += 1
    out = []
    for a in order + [a for a in per if a and a not in order]:
        out.append({"account": a, "inWindow": a in wins.values(), "days": [per[a][d] for d in days],
                    "total": sum(per[a].values()), "lastLimit": (limits[a] or [None])[-1],
                    "limitsToday": sum(1 for t in limits[a] if t[:10] == days[-1])})
    return {"days": days, "accounts": out, "unknown": sum(per[None].values()), "robots": robots[-5:]}


# ---------- state ----------

def state():
    b = bridge_status()
    n8n_now = n8n_state()
    health = {"n8n": n8n_now == "running", "n8nState": n8n_now, "bridge": b is not None, "opencut": up("http://127.0.0.1:3000"),
              "jobstash": jobstash()}
    try:
        rs = runs() if health["n8n"] else []
    except Exception as e:
        rs, health["n8nError"] = [], str(e)
    vids = videos()
    claims = (b or {}).get("claims", {})
    live = [r for r in rs if r["live"]]
    for v in vids:
        last = next((r for r in rs if r["slug"] == v["slug"] and not r["live"]), None)
        v["lastRun"] = last
        if live and v["slug"] in claims:
            v["status"] = "running"
        elif v["mp4"]:
            v["status"] = "done"
        elif not v["script"]:
            v["status"] = "draft"
        elif last and last["outcome"] == "failed":
            v["status"] = "failed"
        else:
            v["status"] = "waiting"
    vids.sort(key=lambda v: (v["status"] != "running", -v["changed"]))
    run = None
    if live:
        slug = next(iter(claims), None)
        v = next((x for x in vids if x["slug"] == slug), None)
        recent_imgs = [p.stat().st_mtime for p in images(OUT / slug).values()] if v else []
        # images / min over the last 15 min, or since the run started if that is shorter
        started = datetime.fromisoformat(live[0]["startedAt"].replace("Z", "+00:00")).timestamp()
        since = max(time.time() - 900, started)
        mins = max((time.time() - since) / 60, 1)
        rate = sum(1 for m in recent_imgs if m > since) / mins
        run = {"id": live[0]["id"], "startedAt": live[0]["startedAt"], "slug": slug, "video": v,
               "rate": round(rate, 2), "eta": round((v["total"] - v["made"]) / rate) if v and rate else None}
    named = [r for r in rs if r["slug"]]
    robot = named[0] if named and not named[0]["live"] and "robot check" in named[0]["reason"] else None
    return {"health": health, "videos": vids, "run": run, "runs": [r for r in rs if r["outcome"] != "idle"],
            "idleRuns": sum(1 for r in rs if r["outcome"] == "idle"), "robot": robot,
            "wins": (b or {}).get("wins", {}), "recent": (b or {}).get("recent", [])[::-1],
            "accounts": accounts((b or {}).get("wins", {})), "now": time.time()}


def video_detail(slug):
    d = folder(slug)
    s = script(d) or {"segments": []}
    imgs = images(d)
    segs = [{"id": x["id"], "text": x.get("text", ""), "prompt": x.get("prompt", ""), "scene": x.get("scene", ""),
             "v": int(imgs[x["id"]].stat().st_mtime) if x["id"] in imgs else None} for x in s["segments"]]
    if not s["segments"]:                                    # old folder without script.json: just its images
        segs = [{"id": i, "text": "", "prompt": "", "scene": "", "v": int(p.stat().st_mtime)} for i, p in sorted(imgs.items())]
    return dict(video_summary(d), segments=segs)


# ---------- actions ----------

def start(slug):
    v = video_summary(folder(slug))
    if not v["script"]:
        raise ValueError("this video has no script.json yet")
    if v["mp4"]:
        raise ValueError("this video already has its MP4")
    if n8n_state() != "running":
        raise ValueError("n8n is not ready: open the dashboard shortcut (it starts n8n), wait for its dot to turn green, then press Start")
    if any(r["live"] for r in runs(10)):
        raise ValueError("a run is already going; stop it first")
    http(N8N + "/webhook/yt-render", "POST", {"slug": slug, "voice": v["voice"]}, timeout=15)
    return {"message": f"started {slug}"}


def stop():
    stopped = []
    for status in ("running", "waiting"):
        for e in n8n(f"/executions?workflowId={WORKFLOW}&status={status}&limit=20")["data"]:
            n8n(f"/executions/{e['id']}/stop", "POST", {})
            stopped.append(e["id"])
    b = bridge_status()
    if b is None:
        return {"message": f"stopped run(s) {stopped or 'none'}; the bridge is not running, so no windows were closed"}
    for slug in b["claims"]:
        http(BRIDGE + "/release", "POST", {"slug": slug})
    # the runner finishes the order it is on, then this one closes every Gemini window and tab
    ans = http(BRIDGE + "/command", "POST", {"name": "setup", "args": {}, "timeout": 90}, timeout=100)
    closed = f"closed {ans.get('closedTabs', 0)} Gemini tab(s)" if ans.get("ok") else f"windows not closed: {ans.get('error')}"
    return {"message": f"stopped run(s) {stopped or 'none'}, released {list(b['claims']) or 'nothing'}, {closed}"}


# Every window that runs TheJobStash's scorer or tunnel, whoever opened it (this dashboard, scorer.cmd, a terminal):
# the process itself, whatever holds :3300, and the cmd window each one runs in.
_JS_KILL = ("$p = Get-CimInstance Win32_Process; "
            "$own = @((Get-NetTCPConnection -LocalPort 3300 -State Listen -ErrorAction SilentlyContinue).OwningProcess); "
            "$hit = @($p | ? { ($_.Name -in 'cmd.exe','python.exe','cloudflared.exe' -and "
            "$_.CommandLine -match 'py_server\\.py|tunnel run jobstash-scorer') -or $own -contains $_.ProcessId }); "
            "$ids = @($hit.ProcessId) + @($p | ? { $_.Name -eq 'cmd.exe' -and $hit.ParentProcessId -contains $_.ProcessId } "
            "| % ProcessId); $ids | sort -Unique | % { taskkill /F /T /PID $_ 2>$null | Out-Null }")


def jobstash_start():
    """Restart TheJobStash's scorer and tunnel: close every window already running either (dead ones sit at `pause`,
    and a stale py_server keeps :3300 so a new one cannot start), then start both fresh, each in its own minimised
    window, with the same commands and .env.cloudflare as TheJobStash\\scorer.cmd (minus n8n, which is already the
    one above). Close a window to stop that part."""
    global _js_started
    s = jobstash()
    if s["starting"]:
        raise ValueError("already starting; give it a few seconds")
    env = dict(os.environ)
    for line in (JOBSTASH / ".env.cloudflare").read_text(encoding="utf-8").splitlines():
        k, sep, v = line.partition("=")
        if sep and k and v and not k.startswith("#"):
            env[k] = v
    subprocess.run(["powershell", "-NoProfile", "-Command", _JS_KILL], timeout=60,
                   creationflags=subprocess.CREATE_NO_WINDOW)
    si = subprocess.STARTUPINFO()
    si.dwFlags, si.wShowWindow = subprocess.STARTF_USESHOWWINDOW, 7          # SW_SHOWMINNOACTIVE
    for title, cmd in [("jobstash scorer :3300", "python py_server.py"),
                       ("jobstash tunnel", f"{CLOUDFLARED} tunnel run jobstash-scorer")]:
        # own console and no inherited handles, so it outlives this dashboard; `pause` keeps a crash readable
        subprocess.Popen(["cmd", "/c", f"title {title} && {cmd} & pause"], cwd=JOBSTASH, env=env,
                         creationflags=subprocess.CREATE_NEW_CONSOLE, startupinfo=si)
    _js_started = time.time()
    return {"message": "restarting TheJobStash scorer and tunnel"}


def thumb_pick(slug, i, on):
    d = folder(slug)
    i = int(i)
    if not (d / "thumbs" / f"thumb-{i}.jpg").exists():
        raise ValueError(f"thumbnail {i} is not made yet")
    ok = [x for x in approved(d) if x != i] + ([i] if on else [])
    if len(ok) > 3:
        raise ValueError("only 3 thumbnails can be picked; untick one first")
    (d / "thumbs-approved.json").write_text(json.dumps(sorted(ok)), encoding="utf-8")
    return {"message": f"thumbnail {i} {'picked' if on else 'unpicked'}", "ok": sorted(ok)}


def redo(slug, i):
    d = folder(slug)
    if (d / f"{slug}.mp4").exists():
        raise ValueError("this video already has its MP4; redo is only for videos still being made")
    i = int(i)
    old = [p for p in (d / "img").glob(f"{i:03d}.*") if IMG.match(p.name)] + list((d / "img_clean").glob(f"{i:03d}.jpg"))
    if not old:
        raise ValueError(f"image {i:03d} is not made yet")
    keep = d / "img" / "redo"
    keep.mkdir(exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    for p in old:
        shutil.move(str(p), keep / f"{p.stem}-{p.parent.name}-{stamp}{p.suffix}")
    return {"message": f"image {i:03d} moved to img/redo/; the next run makes it again"}


def delete(slug, typed):
    """Delete the whole output/<slug>/ folder (script, images, voice, MP4: everything). Permanent."""
    d = folder(slug)
    if typed != slug:
        raise ValueError("type the video's name exactly to delete it")
    if any(r["live"] for r in runs(10)):
        raise ValueError("a run is going; stop it before deleting a video")
    b = bridge_status()
    if b and slug in b["claims"]:
        raise ValueError("the bridge still has this video claimed by a run")

    def unlock(fn, path, _):                         # Windows: read-only files refuse to be removed
        Path(path).chmod(0o666)
        fn(path)

    shutil.rmtree(d, onerror=unlock)
    _scripts.pop(d / "script.json", None)
    return {"message": f"deleted {slug}"}


# ---------- thumbnails ----------

_thumbs = {}   # ponytail: unbounded in-memory cache, ~15 KB per image; fine for a handful of videos


def thumb(p):
    k = (p, p.stat().st_mtime)
    if k not in _thumbs:
        im = Image.open(p).convert("RGB")
        im.thumbnail((400, 400))
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=80)
        _thumbs[k] = buf.getvalue()
    return _thumbs[k]


# ---------- http ----------

class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, body, ctype="application/json", code=200, extra=None):
        if not isinstance(body, bytes):
            body = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def local(self):
        # only pages opened as 127.0.0.1 / localhost (stops DNS-rebinding sites from talking to this server)
        return (self.headers.get("Host") or "").split(":")[0] in ("127.0.0.1", "localhost")

    def file(self, p):
        """Serve a file, with byte ranges so the MP4 can be seeked."""
        size = p.stat().st_size
        rng = re.match(r"bytes=(\d*)-(\d*)", self.headers.get("Range") or "")
        start, end = 0, size - 1
        if rng and (rng[1] or rng[2]):
            start = int(rng[1]) if rng[1] else size - int(rng[2])
            end = min(int(rng[2]), size - 1) if rng[1] and rng[2] else end
        self.send_response(206 if rng else 200)
        self.send_header("Content-Type", TYPES.get(p.suffix.lower(), "application/octet-stream"))
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Length", str(end - start + 1))
        if rng:
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        if p.suffix.lower() == ".srt":
            self.send_header("Content-Disposition", f'attachment; filename="{p.name}"')
        self.end_headers()
        with p.open("rb") as fh:
            fh.seek(start)
            left = end - start + 1
            try:
                while left > 0:
                    chunk = fh.read(min(1 << 20, left))
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    left -= len(chunk)
            except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
                pass                                       # the player moved on

    def do_GET(self):
        if not self.local():
            return self.send({"error": "forbidden"}, code=403)
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        parts = u.path.strip("/").split("/")
        try:
            if u.path in ("/", "/index.html"):
                return self.send((HERE / "dashboard.html").read_bytes(), TYPES[".html"], extra={"Cache-Control": "no-store"})
            if u.path == "/api/state":
                return self.send(state())
            if u.path == "/api/video":
                return self.send(video_detail(q["slug"]))
            if parts[0] in ("thumb", "img") and len(parts) == 3:
                p = images(folder(parts[1])).get(int(parts[2]))
                if not p:
                    return self.send({"error": "no such image"}, code=404)
                if parts[0] == "thumb":
                    return self.send(thumb(p), "image/jpeg", extra={"Cache-Control": "max-age=86400"})
                return self.file(p)
            if parts[0] in ("ythumb", "ythumbfull") and len(parts) == 3:
                p = folder(parts[1]) / "thumbs" / f"thumb-{int(parts[2])}.jpg"
                if not p.exists():
                    return self.send({"error": "no such thumbnail"}, code=404)
                if parts[0] == "ythumb":
                    return self.send(thumb(p), "image/jpeg", extra={"Cache-Control": "max-age=86400"})
                return self.file(p)
            if parts[0] == "file" and len(parts) == 3:
                d = folder(parts[1])
                if parts[2] not in (f"{d.name}.mp4", f"{d.name}.srt") or not (d / parts[2]).exists():
                    return self.send({"error": "no such file"}, code=404)
                return self.file(d / parts[2])
        except (ValueError, KeyError) as e:
            return self.send({"error": str(e)}, code=400)
        except Exception as e:
            return self.send({"error": f"{type(e).__name__}: {e}"}, code=500)
        self.send({"error": "not found"}, code=404)

    def do_POST(self):
        # a custom header + JSON body: other web pages can't send this without a CORS preflight, which is refused
        if not self.local() or self.headers.get("X-Dash") != "1":
            return self.send({"error": "forbidden"}, code=403)
        r = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
        try:
            act = urlparse(self.path).path
            if act == "/api/start":
                return self.send(start(r["slug"]))
            if act == "/api/stop":
                return self.send(stop())
            if act == "/api/n8n/restart":
                return self.send(n8n_restart())
            if act == "/api/jobstash/start":
                return self.send(jobstash_start())
            if act == "/api/thumbpick":
                return self.send(thumb_pick(r["slug"], r["id"], bool(r["on"])))
            if act == "/api/redo":
                return self.send(redo(r["slug"], r["id"]))
            if act == "/api/delete":
                return self.send(delete(r["slug"], r.get("typed")))
        except (ValueError, KeyError) as e:
            return self.send({"error": str(e)}, code=400)
        except Exception as e:
            return self.send({"error": f"{type(e).__name__}: {e}"}, code=500)
        self.send({"error": "not found"}, code=404)


if __name__ == "__main__":
    print(f"dashboard on http://127.0.0.1:{PORT}", flush=True)
    ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()

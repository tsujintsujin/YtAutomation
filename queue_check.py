"""Has the Shorts Render run the queue started for this video ended, and how? For n8n "Shorts: run queue"
(n8n/build_shorts_queue.py), which runs this every 30 s after starting the render through its webhook.

    python queue_check.py <slug> <since: ms the queue started the render>
prints one JSON line: {"ended": false} | {"ended": true, "outcome": done|waiting|busy|stopped|failed, "reason": "..."}

The queue only runs while nothing else is being made (the dashboard refuses Start meanwhile), so the first
Shorts Render run started after <since> is the one it started. Its outcome is read the way the dashboard's Runs
list reads it (dashboard.run_details). No run 5 minutes after <since>: the render never started, a failure."""
import json
import sys
import time
from datetime import datetime

from dashboard import SHORTS_FLOW, flow_ids, n8n, run_details

OUTCOME = {"made": "done", "limits": "waiting", "skipped": "busy", "failed": "failed"}


def check(slug, since):
    found = []
    for wid in flow_ids(SHORTS_FLOW):
        for q in ("", "&status=running", "&status=waiting"):
            found += [e for e in n8n(f"/executions?workflowId={wid}&limit=20{q}")["data"]
                      if not e["startedAt"]           # "new": waiting for a free n8n slot, so started after <since>
                      or datetime.fromisoformat(e["startedAt"].replace("Z", "+00:00")).timestamp() >= since / 1000 - 5]
    if not found:
        if time.time() - since / 1000 > 300:
            return {"ended": True, "outcome": "failed", "reason": "the render did not start within 5 minutes"}
        return {"ended": False}
    e = min(found, key=lambda e: int(e["id"]))
    if e["status"] in ("running", "waiting", "new"):
        return {"ended": False}
    d = run_details(e["id"])
    if d["slug"] and d["slug"] != slug:
        return {"ended": True, "outcome": "failed", "reason": f"the run that started was for {d['slug']}, not {slug}"}
    if e["status"] == "canceled" and not d["outcome"]:
        return {"ended": True, "outcome": "stopped", "reason": "the render was stopped by hand"}
    return {"ended": True, "outcome": OUTCOME.get(d["outcome"], "failed"), "reason": d["reason"] or e["status"]}


if __name__ == "__main__":
    print(json.dumps(check(sys.argv[1], int(sys.argv[2]))))

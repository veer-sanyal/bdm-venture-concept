"""Flag agents that opened project files during a METHOD run.

Every generator, shaper, judge and team-fit agent must work from its prompt and the web only
(METHOD.md, "Rules for the orchestrator"). Run this on each agent's transcript (the JSONL
output file the Agent tool reports) before using its report or recording its scores.

Usage: python3 tools/audit_reads.py [label=]transcript.jsonl ...
Prints CLEAN or the offending tool calls for each transcript; exits 1 if any is flagged.
"""
import json, re, sys
from pathlib import Path

REPO = str(Path(__file__).resolve().parent.parent)
# Names that only make sense as reads of this repo (or of the orchestrator's hidden files).
REPO_NAMES = re.compile(r"\b(METHOD|STATE|AGENTS|README|CASEBOOK|CONCEPT|CANDIDATES[-\w]*)\.md\b|"
                        r"\bscores\.(csv|py)\b|\baudit_reads\.py\b|(^|[\s'\"=])(research|screens|predictions|archive|tools)/|\.orch\b")
OTHER_DIR = re.compile(r"^\s*cd\s+(/tmp|/root|/home/(?!user/bdm-venture-concept))")

def flags(call):
    name, inp = call.get("name"), call.get("input") or {}
    if name in ("Read", "NotebookRead"):
        return REPO in str(inp.get("file_path", ""))
    if name in ("Grep", "Glob"):
        path = str(inp.get("path", ""))
        return not path or REPO in path  # no path means the agent's cwd, which is the repo
    if name == "Bash":
        cmd = str(inp.get("command", ""))
        if REPO in cmd or REPO_NAMES.search(cmd):
            return True
        # A bare listing with no cd elsewhere lists the repo (the agent's cwd).
        return bool(re.match(r"\s*(ls|find|tree|cat|head|grep|rg)\b", cmd)) and not OTHER_DIR.match(cmd)
    return False

def audit(path):
    hits = []
    for line in open(path, errors="replace"):
        try:
            content = (json.loads(line).get("message") or {}).get("content")
        except ValueError:
            continue
        for b in content if isinstance(content, list) else []:
            if isinstance(b, dict) and b.get("type") == "tool_use" and flags(b):
                hits.append(f"{b['name']}: {json.dumps(b.get('input'))[:160]}")
    return hits

def _check():
    ok = {"name": "Bash", "input": {"command": "curl -s https://example.com | grep -i method"}}
    assert not flags(ok)
    assert flags({"name": "Read", "input": {"file_path": REPO + "/METHOD.md"}})
    assert flags({"name": "Bash", "input": {"command": "ls && wc -l METHOD.md STATE.md"}})
    assert flags({"name": "Grep", "input": {"pattern": "bar"}})
    assert not flags({"name": "Bash", "input": {"command": "cd /tmp/x && ls"}})
    assert flags({"name": "Bash", "input": {"command": "cd /tmp/x && ls .orch"}})

if __name__ == "__main__":
    _check()
    bad = 0
    for arg in sys.argv[1:]:
        label, _, path = arg.rpartition("=")
        hits = audit(path)
        bad += bool(hits)
        print(f"{label or path}: " + ("CLEAN" if not hits else f"FLAGGED ({len(hits)})"))
        for h in hits:
            print("   ", h)
    sys.exit(1 if bad else 0)

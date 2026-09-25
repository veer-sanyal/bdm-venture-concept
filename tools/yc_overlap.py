"""Find YC companies whose listing overlaps a candidate, for the merge step.

A candidate that nearly copies a funded company is a problem twice over: it is
not new, and the judge prompt tells the judge to treat a matching company as the
team, so the candidate would borrow that company's traction in its score.
Scores each company in the given batches by how many query terms its one-liner
and description contain, and prints the best matches. Batches come from the
yc-oss mirror of the YC directory and are cached under research/.yc-cache/.

Run: python3 tools/yc_overlap.py "dispute" "collector" "furnisher" [--batches fall-2026,summer-2026] [--top 15]
"""
import argparse, json, re, urllib.request
from pathlib import Path

API = "https://yc-oss.github.io/api/batches/{}.json"
DEFAULT = "winter-2026,spring-2026,summer-2026,fall-2026"
CACHE = Path(__file__).resolve().parent.parent / "research" / ".yc-cache"

def load(batch, refresh):
    path = CACHE / f"{batch}.json"
    if refresh or not path.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(API.format(batch), timeout=60) as r:
            path.write_bytes(r.read())
    return json.loads(path.read_text())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("terms", nargs="+", help="words or regexes; each hit counts once")
    ap.add_argument("--batches", default=DEFAULT)
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--refresh", action="store_true", help="re-download batches")
    a = ap.parse_args()
    pats = [re.compile(t, re.I) for t in a.terms]
    hits = []
    for batch in a.batches.split(","):
        for c in load(batch, a.refresh):
            text = f"{c.get('one_liner') or ''} {c.get('long_description') or ''}"
            matched = [p.pattern for p in pats if p.search(text)]
            if matched:
                hits.append((len(matched), batch, c["name"], c.get("one_liner") or "", matched))
    hits.sort(key=lambda h: -h[0])
    for n, batch, name, one, matched in hits[: a.top]:
        print(f"{n}/{len(pats)}  {batch:12} {name}: {one}  [{', '.join(matched)}]")
    if not hits:
        print("no matches")

if __name__ == "__main__":
    main()

"""Summarize scores.csv: per-round standings and parameter averages.

Several judges may score the same paragraph (one row each); a paragraph's
score is the mean of its judges. A candidate advances when its mean total is
at or above the median control total in the same round (ties count).
Run: python3 tools/scores.py
"""
import csv, statistics, sys
from collections import defaultdict
from pathlib import Path

PARAMS = ["need", "value", "market", "risk"]

def load(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for p in PARAMS:
            r[p] = int(r[p])
            assert 1 <= r[p] <= 5, f"{r['paragraph']}: {p}={r[p]} out of 1-5"
        r["total"] = sum(r[p] for p in PARAMS)
    return rows

def bar(rows):
    """Median control total for a round's rows."""
    return statistics.median(r["total"] for r in rows if r["kind"] == "control")

def averages(rows):
    out = {}
    for kind in ("control", "candidate"):
        sub = [r for r in rows if r["kind"] == kind]
        if sub:
            out[kind] = {p: statistics.mean(r[p] for r in sub) for p in PARAMS + ["total"]}
    return out

def pool(rows):
    """Collapse repeat judges of one paragraph into a single row of means."""
    groups = defaultdict(list)
    for r in rows:
        groups[(r["round"], r["paragraph"])].append(r)
    out = []
    for rs in groups.values():
        m = dict(rs[0])
        for p in PARAMS + ["total"]:
            m[p] = statistics.mean(r[p] for r in rs)
        m["n"] = len(rs)
        m["sd"] = statistics.stdev(r["total"] for r in rs) if len(rs) > 1 else 0.0
        out.append(m)
    return out

def report(rows):
    rows = pool(rows)
    rounds = defaultdict(list)
    for r in rows:
        rounds[r["round"]].append(r)
    lines = []
    for name, rs in rounds.items():
        b = bar(rs)
        lines.append(f"\n## {name} ({rs[0]['date']}), bar = median control total {b:g}")
        for r in sorted(rs, key=lambda r: -r["total"]):
            tag = "control" if r["kind"] == "control" else ("ADVANCES" if r["total"] >= b else "stops")
            lines.append(f"  {r['total']:>5.2f}  {r['need']:.1f} {r['value']:.1f} {r['market']:.1f} {r['risk']:.1f}  "
                         f"n={r['n']} sd={r['sd']:.2f}  {tag:<8}  {r['paragraph']}")
    reps = [r for r in rows if r["n"] > 1]
    if reps:
        pooled = (sum(r["sd"] ** 2 for r in reps) / len(reps)) ** 0.5
        lines.append(f"\n## Judge noise: pooled sd of one judge's total = {pooled:.2f} "
                     f"(from {len(reps)} paragraphs with repeat judges); "
                     f"sd of a 3-judge mean = {pooled / 3 ** 0.5:.2f}")
    lines.append("\n## Averages across all rounds (need value market risk | total)")
    for kind, a in averages(rows).items():
        lines.append(f"  {kind:<9} " + " ".join(f"{a[p]:.2f}" for p in PARAMS) + f" | {a['total']:.2f}")
    return "\n".join(lines)

def _check():
    rows = [dict(date="d", round="r", paragraph=n, kind=k, need=a, value=b, market=c, risk=d_)
            for n, k, a, b, c, d_ in [("c1", "control", "4", "3", "3", "2"), ("c2", "control", "4", "2", "3", "2"),
                                      ("c3", "control", "4", "2", "3", "2"), ("x", "candidate", "4", "3", "2", "2"),
                                      ("y", "candidate", "4", "2", "2", "2")]]
    for r in rows:
        for p in PARAMS:
            r[p] = int(r[p])
        r["total"] = sum(r[p] for p in PARAMS)
    assert bar(pool(rows)) == 11
    out = report(rows)
    line = {l.split()[-1]: l for l in out.splitlines() if l.startswith("  ")}
    assert "ADVANCES" in line["x"] and "stops" in line["y"], out  # x ties the median, y is below
    x2 = dict(rows[3], need=3)  # a second judge scores x one point lower
    x2["total"] = sum(x2[p] for p in PARAMS)
    line = {l.split()[-1]: l for l in report(rows + [x2]).splitlines() if l.startswith("  ")}
    assert "n=2" in line["x"] and "stops" in line["x"], line["x"]  # mean 10.5 < 11

if __name__ == "__main__":
    _check()
    print(report(load(Path(__file__).resolve().parent.parent / (sys.argv[1] if len(sys.argv) > 1 else "scores.csv"))))

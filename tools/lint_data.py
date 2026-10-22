#!/usr/bin/env python3
"""Structural checks on data/candidates.json (no network). Exit status 1 if anything is wrong.

Checks: unique ids, every cited source key exists, quotes always have a source, every topic id is known,
statements have a date and context, no duplicate statements, URLs look like URLs, and ZIP data covers
only districts that have candidates.
"""
import json, collections, re, sys, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root / "data" / "candidates.json").read_text())["candidates"]
topics = {t["id"] for t in json.loads((root / "data" / "topics.json").read_text())}
zips = json.loads((root / "data" / "zip_districts.json").read_text())
problems = []

ids = [c["id"] for c in data]
problems += [("duplicate id", k) for k, n in collections.Counter(ids).items() if n > 1]

for c in data:
    keys = [s["key"] for s in c["sources"]]
    problems += [(c["id"], "duplicate source key", k) for k, n in collections.Counter(keys).items() if n > 1]
    for s in c["sources"]:
        if not re.match(r"https?://", s["url"]):
            problems.append((c["id"], "bad source url", s["url"]))
    for url in [c.get("website")] + [l["url"] for l in c.get("links", [])]:
        if url and not re.match(r"https?://", url):
            problems.append((c["id"], "bad link", url))
    if c.get("reviewed") and c["reviewed"] not in keys:
        problems.append((c["id"], "reviewed source missing", c["reviewed"]))
    if not c.get("party") or not c.get("ticket"):
        problems.append((c["id"], "missing party or ticket"))

    def segments():
        for para in c["overview"]:
            yield from para
        for t, v in c["topics"].items():
            if t not in topics:
                problems.append((c["id"], "unknown topic", t))
            for para in v.get("paras", []) + v.get("plan", []):
                yield from para
            for item in v["said"]:
                if not item.get("when") or not item.get("context"):
                    problems.append((c["id"], t, "statement missing date or context"))
                yield from item["seg"]
    for seg in segments():
        if "q" in seg and not seg.get("s"):
            problems.append((c["id"], "quote without source", seg["q"][:50]))
        if seg.get("s") and seg["s"] not in keys:
            problems.append((c["id"], "unknown source key", seg["s"]))
    for t, v in c["topics"].items():
        seen = collections.Counter(json.dumps(i["seg"], sort_keys=True) for i in v["said"])
        problems += [(c["id"], t, "duplicate statement") for k, n in seen.items() if n > 1]

# ZIP lookup should only point at districts that exist in the data
houses = {c["district"] for c in data if c["office"] == "U.S. House"}
senates = {c["district"] for c in data if c["office"] == "State Senate"}
for z, r in zips.items():
    problems += [("zip " + z, "house district without candidates", d) for d, _ in r["h"] if d not in houses]
    problems += [("zip " + z, "senate district without candidates", d) for d, _ in r["s"] if d not in senates]

print(f"{len(data)} candidates, {len(zips)} ZIP areas checked; {len(problems)} problem(s)")
for p in problems[:50]:
    print("  ", p)
sys.exit(1 if problems else 0)

#!/usr/bin/env python3
"""Download U.S. House roll-call XML (clerk.house.gov) for the ten-year window and index it.

    python3 tools/fetch_house_rolls.py            # fetch what is missing, rebuild index

Raw XML goes to tools/votes_cache/house/ (git-ignored); tools/votes_cache/house_index.json lists
every roll (year, number, bill, question, result, date, description) so key votes can be chosen.
"""
import concurrent.futures as cf, json, pathlib, re, subprocess, sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).parent / "votes_cache"
RAW = ROOT / "house"
MAX = {2017: 700, 2018: 500, 2019: 700, 2020: 250, 2021: 450, 2022: 560, 2023: 730, 2024: 540, 2025: 430, 2026: 250}

def fetch(job):
    y, n = job
    f = RAW / f"{y}_{n}.xml"
    if f.exists() and f.stat().st_size > 500:
        return
    out = subprocess.run(["curl", "-s", "-m", "30", "-A", "Mozilla/5.0", f"https://clerk.house.gov/evs/{y}/roll{n}.xml"],
                         capture_output=True).stdout
    if b"<rollcall-vote" in out:
        f.write_bytes(out)

def index():
    rows = []
    for f in sorted(RAW.glob("*.xml")):
        try:
            m = ET.parse(f).getroot().find("vote-metadata")
        except ET.ParseError:
            continue
        g = lambda t: (m.findtext(t) or "").strip()
        rows.append({"year": int(f.stem.split("_")[0]), "roll": int(g("rollcall-num")), "bill": g("legis-num"),
                     "q": g("vote-question"), "result": g("vote-result"), "date": g("action-date"), "desc": g("vote-desc")})
    (ROOT / "house_index.json").write_text(json.dumps(rows, indent=0))
    return rows

if __name__ == "__main__":
    RAW.mkdir(parents=True, exist_ok=True)
    jobs = [(y, n) for y, mx in MAX.items() for n in range(1, mx + 1)]
    with cf.ThreadPoolExecutor(10) as ex:
        list(ex.map(fetch, jobs))
    print(len(index()), "rolls indexed")

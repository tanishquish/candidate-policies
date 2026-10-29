#!/usr/bin/env python3
"""Locate the U.S. House roll call for a bill on a given date by bisecting roll numbers by date (one XML per probe)."""
import datetime as dt, re, subprocess, sys, time, pathlib
import xml.etree.ElementTree as ET

SEL = pathlib.Path(__file__).parent / "votes_cache" / "house_sel"
MON = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}

def fetch(y, n):
    f = SEL / f"{y}_{n}.xml"
    if not f.exists():
        for _ in range(3):
            out = subprocess.run(["curl", "-s", "-m", "30", "-A", "Mozilla/5.0", f"https://clerk.house.gov/evs/{y}/roll{n}.xml"], capture_output=True).stdout
            if b"<rollcall-vote" in out:
                f.write_bytes(out); break
            time.sleep(1.5)
        time.sleep(0.25)
    if not f.exists():
        return None
    m = ET.parse(f).getroot().find("vote-metadata")
    d, mon, yr = m.findtext("action-date").split("-")
    return {"roll": n, "date": dt.date(int(yr), MON[mon], int(d)), "bill": m.findtext("legis-num").strip(), "q": m.findtext("vote-question").strip(),
            "result": m.findtext("vote-result").strip(), "desc": (m.findtext("vote-desc") or "").strip()}

def first_on_or_after(y, day, hi=900):
    lo = 1
    while lo < hi:
        mid = (lo + hi) // 2
        r = fetch(y, mid)
        if r is None:           # past the last roll of the year
            hi = mid
        elif r["date"] < day:
            lo = mid + 1
        else:
            hi = mid
    return lo

def find(y, day, bill):
    n0 = first_on_or_after(y, day)
    hits = []
    for n in range(max(1, n0 - 3), n0 + 45):
        r = fetch(y, n)
        if r and r["date"] >= day and r["bill"].replace(" ", "") == bill.replace(" ", "") and r["date"] <= day + dt.timedelta(days=3):
            hits.append(r)
    return hits

if __name__ == "__main__":
    y, day, bill = int(sys.argv[1]), dt.date.fromisoformat(sys.argv[2]), sys.argv[3]
    for r in find(y, day, bill):
        print(r)

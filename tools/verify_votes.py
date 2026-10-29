#!/usr/bin/env python3
"""Re-fetch every roll call cited in a voting record and confirm each stored vote and tally against it.

    python3 tools/verify_votes.py          (needs pypdf: pip install pypdf)

State tallies come from cga.ct.gov, federal ones from clerk.house.gov. Cached copies are ignored.
"""
import json, pathlib, re, subprocess, sys, io, time
import xml.etree.ElementTree as ET
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import ctvotes as C, votes_build as V

ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.load(open(ROOT / "data" / "candidates.json"))["candidates"]
fresh = {}

def fetch(url):
    if url not in fresh:
        for attempt in range(5):
            raw = subprocess.run(["curl", "-s", "-m", "40", "-A", "Mozilla/5.0", url], capture_output=True).stdout
            ok = raw.rstrip().endswith(b"%%EOF") if url.lower().endswith(".pdf") else len(raw) > 500
            if ok:
                break
            time.sleep(2)
        fresh[url] = raw
    return fresh[url]

def state_text(url):
    raw = fetch(url)
    if url.lower().endswith(".pdf"):
        import pypdf
        t = "\n".join(p.extract_text() for p in pypdf.PdfReader(io.BytesIO(raw)).pages)
    else:
        t = re.sub(r"<[^>]+>", " ", raw.decode("utf-8", "replace")).replace("&#160;", " ")
    return re.sub(r"\s+", " ", t)

problems, checked = [], 0
for c in data:
    for it in c["votes"]["items"]:
        src = {s["key"]: s["url"] for s in c["sources"]}
        url = src[it["s"]]
        checked += 1
        want = it["vote"]
        if it["body"] == "U.S. House":
            root = ET.fromstring(fetch(url))
            bid = V.FED_IDS[c["id"]]
            got = next((rv.findtext("vote") for rv in root.iter("recorded-vote") if rv.find("legislator").get("name-id") == bid), None)
            got = {"Aye": "Yea", "No": "Nay", "Not Voting": "Not voting"}.get(got, got)
            votes = [rv.findtext("vote") for rv in root.iter("recorded-vote")]
            tally = f"{sum(v in ('Yea','Aye') for v in votes)}–{sum(v in ('Nay','No') for v in votes)}"
        else:
            t = state_text(url)
            m = re.search(r"Those voting Yea[ .]*(\d+) Those voting Nay[ .]*(\d+)", t)
            tally = f"{m.group(1)}–{m.group(2)}" if m else None
            if "Senate" in it["body"]:
                body = t.split("roll call vote:")[-1]
                got = None
                for mm in re.finditer(r"\b([YNAX]) (\d{1,3}) (.+?)(?= [YNAX] \d{1,3} |$)", body):
                    if V._senate_match(c["name"], mm.group(3)):
                        got = V.CODES[mm.group(1)]
            else:
                sv = V.STATE_HOUSE_SERVICE[c["id"]]
                code = V._house_vote(t, sv[0], sv[1])
                got = V.CODES.get(code)
        if got != want or tally != it["tally"]:
            problems.append((c["id"], it["bill"], it["date"], f"stored {want} {it['tally']}", f"fresh {got} {tally}"))
print(f"{checked} votes checked against {len(fresh)} roll calls; {len(problems)} problem(s)")
for p in problems:
    print("  ", p)
sys.exit(1 if problems else 0)

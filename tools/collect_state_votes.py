#!/usr/bin/env python3
"""Read the final-passage roll calls for tools/vote_bills.STATE_BILLS from cga.ct.gov into votes_cache/state_votes.json."""
import json, pathlib, sys
import ctvotes as C
from vote_bills import STATE_BILLS, NOTES

out = []
for year, bill, topic, label in STATE_BILLS:
    url, html = C.bill_page(year, bill)
    entry = {"year": year, "bill": bill, "topic": topic, "label": label, "title": C.title_of(html).rstrip("."), "page": url, "votes": {}}
    if (year, bill) in NOTES:
        entry["note"] = list(NOTES[(year, bill)])
    for chamber in ("Senate", "House"):
        v = C.passage(html, chamber)
        if not v:
            continue
        path, _, num, lab = v
        full = "https://www.cga.ct.gov" + path
        r = C.parse(full)
        entry["votes"][chamber] = {"url": full, "roll": num, "label": lab, "date": r["date"], "yea": r["yea"], "nay": r["nay"],
                                   "absent": r["absent"], "members": {str(k): v for k, v in r["members"].items()} if chamber == "Senate" else None,
                                   "text": r["text"] if chamber == "House" else None}
    print(year, bill, {k: (v["date"], v["yea"], v["nay"]) for k, v in entry["votes"].items()})
    out.append(entry)
(pathlib.Path(__file__).parent / "votes_cache" / "state_votes.json").write_text(json.dumps(out, indent=1))

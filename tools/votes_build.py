"""Attach recorded votes to candidates (state roll calls from cga.ct.gov, U.S. House roll calls from clerk.house.gov).

Inputs are the caches written by collect_state_votes.py and find_house_rolls.py. Nothing here is typed by hand
except who is who: STATE_HOUSE_SERVICE and FED_IDS, each tied to a source for the identification.
"""
import datetime as dt, json, pathlib, re
import xml.etree.ElementTree as ET

CACHE = pathlib.Path(__file__).parent / "votes_cache"
CODES = {"Y": "Yea", "N": "Nay", "A": "Absent or not voting", "X": "Absent or not voting"}
FIRST_OK = {"rob": "robert", "norm": "norman", "bob": "robert", "joe": "joseph", "jeff": "jeffrey", "matt": "matthew"}

# State House members among the candidates. Roll calls list House members by surname only, so each person
# is tied to a published biography that confirms the surname belongs to them (and, where several members share
# one, their first initial). (surname as printed, initial or None, summary segment, source key, title, url)
STATE_HOUSE_SERVICE = {
    "ct-sen-05-slap": ("SLAP", None, "Served in the Connecticut House of Representatives (District 19) from January 5, 2017 to February 28, 2019.", "bio-v", "Derek Slap (Wikipedia)", "https://en.wikipedia.org/wiki/Derek_Slap"),
    "ct-sen-06-lopes": ("LOPES", None, "Served in the Connecticut House of Representatives (District 24) from January 2012 to January 2021.", "bio-v", "Rick Lopes (Wikipedia)", "https://en.wikipedia.org/wiki/Rick_Lopes"),
    "ct-sen-09-lesser": ("LESSER", None, "Was State Representative for the 100th District in Middletown from 2008 to 2019.", "bio-v", "Senator Matt Lesser: About (Senate Democrats)", "https://senatedems.ct.gov/lesser-about"),
    "ct-sen-16-sampson": ("SAMPSON", None, "Served in the Connecticut House of Representatives (District 80) from 2011 to 2018.", "bio-v", "Robert Sampson (Wikipedia)", "https://en.wikipedia.org/wiki/Robert_Sampson_(politician)"),
    "ct-sen-30-harding": ("HARDING", None, "Served in the Connecticut House of Representatives (District 107) from February 25, 2015 to January 4, 2023.", "bio-v", "Stephen Harding (Wikipedia)", "https://en.wikipedia.org/wiki/Stephen_Harding_(politician)"),
    "ct-sen-21-perillo": ("PERILLO", "J", "Was State Representative for Shelton for over 18 years before joining the State Senate.", "bio-v", "Jason Perillo Sworn in as a State Senator of Connecticut’s 21st District (Senate Republicans)", "https://www.ctsenaterepublicans.com/2025/02/jason-perillo-sworn-in-as-a-state-senator-of-connecticuts-21st-district/"),
    "ct-sen-27-miller": ("MILLER", "P", "Served in the Connecticut House of Representatives (District 145) from 2009 to March 8, 2021.", "bio-v", "Patricia Billie Miller (Wikipedia)", "https://en.wikipedia.org/wiki/Patricia_Billie_Miller"),
    "ct-comptroller-scanlon": ("SCANLON", None, "From 2015 to 2023 served as the State Representative for the 98th District in the Connecticut General Assembly.", "bio-v", "About the Office of the State Comptroller", "https://osc.ct.gov/about/"),
    "ct-secretary-of-the-state-thomas": ("THOMAS", None, "Represented Norwalk, Wilton, and Westport as State Representative for the 143rd District.", "bio-v", "The Biography of Stephanie Thomas (Secretary of the State)", "https://portal.ct.gov/sots/capitol/about-stephanie-thomas/the-biography-of-stephanie-thomas"),
    "ct-attorney-general-tong": ("TONG", None, "Served for 12 years as a State Representative in the Connecticut General Assembly.", "bio-v", "William Tong Biography (Office of the Attorney General)", "https://portal.ct.gov/AG/About-the-AG/William-Tong-Biography-page"),
    "ct-sen-33-ferraro": ("FERRARO", "C", "Served in the Connecticut House of Representatives (District 117) from January 7, 2015 to January 8, 2025.", "bio-v", "Charles Ferraro (Wikipedia)", "https://en.wikipedia.org/wiki/Charles_Ferraro"),
    "ct-sen-11-paolillo": ("PAOLILLO", "A", "Is State Representative for District 97, New Haven.", "bio-v", "Rep. Al Paolillo (House Democrats)", "https://housedems.ct.gov/node/4506"),
    "ct-sen-02-khan": ("KHAN", None, "Has served in the Connecticut House of Representatives (District 5) since 2022.", "bio-v", "Maryam Khan (Wikipedia)", "https://en.wikipedia.org/wiki/Maryam_Khan"),
    "ct-sen-13-fazzino": ("FAZZINO", None, "Was elected to the Connecticut House of Representatives (District 83) in 2022.", "bio-v", "Rep. Jack Fazzino: Biography (House Democrats)", "https://www.housedems.ct.gov/Fazzino/Biography"),
    "ct-treasurer-wilms": ("WILMS", None, "Represented the 142nd House District from 2015 to 2019 (listed as Friedrich Wilms).", "bio-v", "Connecticut’s 142nd House of Representatives district (Wikipedia)", "https://en.wikipedia.org/wiki/Connecticut%27s_142nd_House_of_Representatives_district"),
}

FED_IDS = {"ct-02-courtney": "C001069", "ct-03-delauro": "D000216", "ct-04-himes": "H001047", "ct-05-hayes": "H001081"}


def _norm(s):
    return re.sub(r"[^a-z ]", "", s.lower().replace("-", " ")).split()


def _senate_match(cname, tally_name):
    c, t = _norm(re.sub(r",? (Jr\.|Sr\.)$", "", cname)), _norm(tally_name)
    if not c or not t or c[-1] != t[-1]:
        return False
    a, b = c[0], t[0]
    a, b = FIRST_OK.get(a, a), FIRST_OK.get(b, b)
    return a.startswith(b) or b.startswith(a)


def _house_members(text):
    body = text.split("roll call vote:")[-1]
    out = []
    for m in re.finditer(r"\b([YNAX]) (.+?)(?= [YNAX] [A-Z']|$)", body):
        out.append((m.group(2).strip(), m.group(1)))
    return out


def _house_vote(text, surname, initial):
    ms = [(n, v) for n, v in _house_members(text) if re.split(r"[ ,]", n)[0].replace("'", "") == surname.replace("'", "")]
    if initial:
        by_init = [(n, v) for n, v in ms if re.search(r",\s*" + initial + r"\b", n)]
        if by_init:
            return by_init[0][1]
        ms = [(n, v) for n, v in ms if "," not in n]
    return ms[0][1] if len(ms) == 1 else None


def _fmt_date(d):
    return d.isoformat()


def state_items(cand):
    """[(date, body, bill, title, topic, vote, tally, roll_url, bill_url)] for a candidate, from the CGA roll calls."""
    votes = json.load(open(CACHE / "state_votes.json"))
    items = []
    house = STATE_HOUSE_SERVICE.get(cand["id"])
    for b in votes:
        for chamber in ("Senate", "House"):
            v = b["votes"].get(chamber)
            if not v:
                continue
            code = None
            if chamber == "Senate":
                for seat, (name, c) in v["members"].items():
                    if _senate_match(cand["name"], name):
                        code = c
            elif house:
                code = _house_vote(v["text"], house[0], house[1])
            if code is None:
                continue
            mo, d = [int(x) for x in v["date"].split("/")]
            items.append({
                "date": _fmt_date(dt.date(b["year"], mo, d)), "body": f"Connecticut {chamber}", "bill": b["bill"].replace("-", " "),
                "title": b["title"], "label": b["label"], "topic": b["topic"], "vote": CODES[code], "tally": f"{v['yea']}–{v['nay']}",
                "roll": v["url"], "page": b["page"], "note": b.get("note"), "kind": "state", "year": b["year"], "rollno": v["roll"]})
    return items


def fed_items(cand_id):
    bid = FED_IDS.get(cand_id)
    if not bid:
        return []
    from fed_targets import FED
    items = []
    final = re.compile(r"Passage|Pass\b|Conference Report|Concur|Agree", re.I)
    other = re.compile(r"Recommit|Previous Question|Rule|Table|Adjourn|Reconsider|Commit|Amendment\b(?!.*Concur)", re.I)
    for year, day, bill, topic, label in FED:
        chosen = []
        hits = sorted((CACHE / "house_sel").glob(f"{year}_*.xml"), key=lambda f: int(f.stem.split("_")[1]))
        for f in hits:
            root = ET.parse(f).getroot()
            m = root.find("vote-metadata")
            if m.findtext("legis-num").strip().replace(" ", "") != bill.replace(" ", ""):
                continue
            dd, mon, yr = m.findtext("action-date").split("-")
            date = dt.datetime.strptime(f"{dd}-{mon}-{yr}", "%d-%b-%Y").date()
            if date.isoformat() != day:
                continue
            code = None
            for rv in root.iter("recorded-vote"):
                lg = rv.find("legislator")
                if lg is not None and lg.get("name-id") == bid:
                    code = rv.findtext("vote")
            if code is None:
                continue
            n = int(m.findtext("rollcall-num"))
            congress = int(m.findtext("congress"))
            num = re.sub(r"\D", "", bill.split()[-1])
            kind = "house-bill" if bill.startswith("H R") else "senate-bill"
            tot = {t.findtext("party"): t for t in m.iter("totals-by-party")}
            pick = lambda t, *names: int(next(t.findtext(n) for n in names if t.findtext(n) is not None))
            yea = sum(pick(t, "yea-total", "aye-total") for t in tot.values())
            nay = sum(pick(t, "nay-total", "no-total") for t in tot.values())
            q = m.findtext("vote-question").strip()
            if not final.search(q) or other.search(q):
                continue
            chosen.append({
                "date": date.isoformat(), "body": "U.S. House", "bill": bill.replace("H R", "H.R.").replace("S ", "S. "), "title": label, "label": label,
                "topic": topic, "vote": {"Yea": "Yea", "Aye": "Yea", "Nay": "Nay", "No": "Nay", "Not Voting": "Not voting", "Present": "Present"}[code],
                "tally": f"{yea}–{nay}", "roll": f"https://clerk.house.gov/evs/{year}/roll{n}.xml",
                "page": f"https://www.congress.gov/bill/{congress}th-congress/{kind}/{num}", "kind": "fed", "year": year, "rollno": n,
                "question": q})
        if chosen:
            items.append(chosen[-1])   # the last qualifying roll on that day is the final vote on the measure
    return items


def build(BYID, add_src):
    stats = {"with_votes": 0, "none": 0}
    for cid, c in BYID.items():
        items = fed_items(cid) if cid in FED_IDS else state_items(c)
        items.sort(key=lambda i: i["date"], reverse=True)
        rec = {"scope": "federal" if cid in FED_IDS or c["office"] == "U.S. House" else "state", "items": [], "service": []}
        if cid in STATE_HOUSE_SERVICE:
            sv = STATE_HOUSE_SERVICE[cid]
            add_src(cid, sv[3], sv[4], sv[5])
            rec["service"].append({"t": sv[2], "s": sv[3]})
        for i in items:
            rk = f"roll-{i['kind']}-{i['year']}-{i['rollno']}"
            bk = f"bill-{i['kind']}-{i['year']}-{i['bill'].replace(' ', '').replace('.', '')}"
            rt = f"{i['body']} roll call vote {i['rollno']}, {i['bill']}"
            add_src(cid, rk, rt, i["roll"])
            add_src(cid, bk, f"{i['bill']}: {i['title']}", i["page"])
            row = {k: i[k] for k in ("date", "body", "bill", "title", "label", "topic", "vote", "tally")}
            row["s"], row["b"] = rk, bk
            if i.get("note"):
                nk = "note-" + bk
                add_src(cid, nk, i["note"][1], i["note"][2])
                row["note"] = {"t": i["note"][0], "s": nk}
            rec["items"].append(row)
        c["votes"] = rec
        stats["with_votes" if rec["items"] else "none"] += 1
    return stats

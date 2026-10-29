"""Fetch and parse Connecticut General Assembly vote tallies (official PDFs)."""
import re, subprocess, io, json, pathlib, sys
import pypdf

CACHE = pathlib.Path(__file__).parent / "votes_cache"
UA = "Mozilla/5.0"

def get(url, binary=False):
    key = CACHE / re.sub(r"[^A-Za-z0-9]+", "_", url)[-150:]
    if key.exists():
        return key.read_bytes() if binary else key.read_text()
    out = subprocess.run(["curl", "-s", "-m", "40", "-A", UA, url], capture_output=True).stdout
    key.write_bytes(out)
    return out if binary else out.decode("utf-8", "replace")

def bill_page(year, bill):
    m = re.match(r"([A-Z]+)-?0*(\d+)$", bill)
    typ = {"HB": "Bill", "SB": "Bill", "HJ": "Resolution", "SJ": "Resolution"}[m.group(1)]
    url = f"https://www.cga.ct.gov/asp/cgabillstatus/cgabillstatus.asp?selBillType=Bill&which_year={year}&bill_num={m.group(2)}"
    # CT status pages are keyed by number; the type letter is in the title
    return url, get(url)

def title_of(html):
    m = re.search(r"((?:AN ACT|RESOLUTION)[^<]{5,300})", html)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""

def vote_links(html):
    """[(path, chamber, number, label)] for every roll call listed on a bill page."""
    out = []
    for m in re.finditer(r'(?i)href\s*=\s*"(/\d{4}/VOTE/[hs]/[^"]+?\.(?:pdf|htm))"[^>]*>\s*(House|Senate) Roll Call Vote (\d+)([^<]*)', html):
        out.append((m.group(1), m.group(2), int(m.group(3)), re.sub(r"\s+", " ", m.group(4)).strip()))
    return out

def passage(html, chamber):
    """The final-passage roll call in a chamber: highest-numbered vote not about an amendment or procedure."""
    skip = re.compile(r"AMD|AMEND(?!ED)|ADOPT|MOTION|RECOMMIT|TABLE|SUSPEN|REJECT|DISAGREE|CONCUR|RECONSIDER", re.I)
    cands = [v for v in vote_links(html) if v[1] == chamber and not skip.search(v[3].replace("AS AMENDED", ""))]
    return max(cands, key=lambda v: v[2]) if cands else None

def text_of(url):
    """Roll-call text as one whitespace-normalised line; handles the PDF and the older HTML tallies."""
    if url.lower().endswith(".pdf"):
        r = pypdf.PdfReader(io.BytesIO(get(url, binary=True)))
        t = "\n".join(p.extract_text() for p in r.pages)
    else:
        t = re.sub(r"<[^>]+>", " ", get(url)).replace("&#160;", " ").replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", t)

def parse(url):
    t = text_of(url)
    d = re.search(r"Taken on ([\d/]+)", t)
    cnt = {k: int(v) for k, v in re.findall(r"Those (?:voting )?(Yea|Nay|absent and not voting)[ .]*(\d+)", t)}
    body = t.split("roll call vote:")[-1]
    mem = {}
    for m in re.finditer(r"\b([YNAX]) (\d{1,3}) (.+?)(?= [YNAX] \d{1,3} |$)", body):
        mem[int(m.group(2))] = (m.group(3).strip(), m.group(1))
    return {"date": d.group(1) if d else None, "yea": cnt.get("Yea"), "nay": cnt.get("Nay"),
            "absent": cnt.get("absent and not voting"), "members": mem, "text": t}

def summary(year, bill):
    url, html = bill_page(year, bill)
    ps, ph = passage(html, "Senate"), passage(html, "House")
    return url, title_of(html), ps, ph

if __name__ == "__main__" and len(sys.argv) > 2 and ":" in sys.argv[1]:
    for yb in sys.argv[1:]:
        y, b = yb.split(":")
        url, t, ps, ph = summary(y, b)
        print(y, b, "|", t[:110], "| S:", ps and ps[2:], "| H:", ph and ph[2:])
elif __name__ == "__main__":
    year, bill = sys.argv[1], sys.argv[2]
    url, html = bill_page(year, bill)
    print(url); print(title_of(html))
    for l, ch, n, lab in vote_links(html):
        t = parse_pdf("https://www.cga.ct.gov" + l)
        d = re.search(r"Taken on ([\d/]+)", t); tot = re.findall(r"Those voting (Yea|Nay)[ .]*(\d+)", t)
        print(ch, n, lab, "|", d.group(1) if d else "?", tot, "AS AMENDED" if "AS AMENDED" in t[:200] else "")

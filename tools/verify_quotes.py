#!/usr/bin/env python3
"""Check that every direct quote in data/candidates.json appears on the page it cites.

Exit status 1 if any quote is missing.
"""
import json, re, html, subprocess, pathlib, sys, time

UAS = ["Mozilla/5.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"]
root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root / "data" / "candidates.json").read_text())
cache = {}

def norm(s):
    s = html.unescape(s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s+([,.;:!?])", r"\1", s)
    return s.strip().lower()

RENDERED = json.loads((root / "tools" / "rendered" / "index.json").read_text()) if (root / "tools" / "rendered" / "index.json").exists() else {}

def page_text(url):
    if url in RENDERED:  # pages whose text is added by JavaScript: copied from a real browser session
        return norm((root / "tools" / "rendered" / RENDERED[url]).read_text())
    if url not in cache:
        if "ballotpedia.org" in url:
            time.sleep(4)  # Ballotpedia rate-limits bursts of requests
        h = ""
        for ua in UAS:  # some sites block one agent string or the other
            h += subprocess.run(["curl", "--compressed", "-sL", "-m", "30", "-A", ua, url], capture_output=True).stdout.decode("utf8", "ignore")
        h = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", "", h)
        h = re.sub(r"(?i)<(br|/p|/div|/h\d|/li|/section)[^>]*>", "\n", h)
        blocked = "sgcaptcha" in h or "captcha" in h.lower()[:2000]
        cache[url] = None if blocked else norm(re.sub(r"<[^>]+>", " ", h))
    return cache[url]

bad = 0
skipped = set()
for c in data["candidates"]:
    urls = {s["key"]: s["url"] for s in c["sources"]}
    segs = [seg for para in c["overview"] for seg in para]
    for t in c["topics"].values():
        segs += [seg for para in t.get("paras", []) for seg in para]
        for item in t["said"]:
            segs += item["seg"]
        segs += [seg for para in t.get("plan", []) for seg in para]
    for seg in segs:
        if "q" in seg:
            text = page_text(urls[seg["s"]])
            if text is None:
                skipped.add(urls[seg["s"]])  # site served a bot-check page; not bypassed
                continue
            if norm(seg["q"]) not in text:
                bad += 1
                print(f"MISSING  {c['name']} [{seg['s']}] {seg['q'][:90]}")
for u in sorted(skipped):
    print("SKIPPED (site showed a bot check; re-run later or check by hand):", u)
print("quotes checked; problems:", bad)
sys.exit(1 if bad else 0)

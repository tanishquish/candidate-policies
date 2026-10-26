#!/usr/bin/env python3
"""Static file server plus the comparison agent endpoint.

    ANTHROPIC_API_KEY=... python3 tools/serve.py        # http://localhost:8000

The agent only ever sees facts already in data/candidates.json (each one tied to
a cited source). Its answer is a list of points, each pointing at fact ids; the
server drops any point whose ids do not exist, so every sentence shown on the
site traces to a vetted source. Without a key the site still works and the
Compare panel explains how to enable it.
"""
import ssl, functools, hashlib, http.server, json, os, re, sys, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = os.environ.get('COMPARE_MODEL', 'claude-sonnet-5-5')
PORT = int(os.environ.get('PORT', 8000))
CACHE = {}

SYSTEM = """You are a strictly nonpartisan comparison assistant on a voter-information site.
You are given numbered FACTS about the candidates in one race. Each fact is already cited and vetted.

Rules:
- Use ONLY the facts provided. Never add outside knowledge, polling, predictions, or judgments about who is right, better, electable or more qualified.
- Neutral wording. Do not use loaded adjectives. Describe each candidate's stated positions and plans in parallel terms and the same depth, whatever their party.
- Every point must cite the fact ids it rests on. A comparison point cites facts from each candidate it mentions.
- Where a candidate has no fact on a topic, say so plainly under that topic (e.g. "No published position was found for X") and never infer.
- Distinguish a stated position from a plan of action from a past statement.
- Do not quote text directly; paraphrase closely. Do not include URLs.
- Cover where candidates are similar, where they differ, and what each says it would do (plans), by topic.
Respond with ONLY JSON: {"summary":[point],"topics":[{"topic":str,"similarities":[point],"differences":[point],"gaps":[point]}]}
where point = {"text": str, "facts": ["F1","F2"]}. Gap points may cite no facts."""

def flat(segs):
    return ''.join(g.get('q') or g.get('t') or '' for g in segs).strip()

def build_facts(cands, topics):
    facts, table, n = [], {}, 0
    def add(c, topic, kind, text, srcs, extra=''):
        nonlocal n
        n += 1; fid = f'F{n}'
        urls = []
        for k in srcs:
            for s in c['sources']:
                if s['key'] == k and s['url'] not in [u['url'] for u in urls]:
                    urls.append({'url': s['url'], 'title': s['title']})
        table[fid] = {'candidate': c['id'], 'sources': urls}
        facts.append(f'{fid} | {c["name"]} | {topic} | {kind} | {text}{extra}')
    for c in cands:
        for para in c['overview']:
            add(c, 'Overview', 'overview', flat(para), {g['s'] for g in para if g.get('s')})
        for t in topics:
            d = c['topics'].get(t['id'])
            if not d: continue
            for para in d.get('paras') or []:
                add(c, t['label'], 'stated position', flat(para), {g['s'] for g in para if g.get('s')})
            for para in d.get('plan') or []:
                add(c, t['label'], 'plan of action', flat(para), {g['s'] for g in para if g.get('s')})
            for it in d.get('said') or []:
                add(c, t['label'], 'past statement', flat(it['seg']), {g['s'] for g in it['seg'] if g.get('s')},
                    f' (said {it["when"]}; context: {it["context"]})')
    return '\n'.join(facts), table

def call_claude(system, user):
    body = json.dumps({'model': MODEL, 'max_tokens': 8000, 'system': system,
                       'messages': [{'role': 'user', 'content': user}]}).encode()
    req = urllib.request.Request('https://api.anthropic.com/v1/messages', body, {
        'x-api-key': os.environ['ANTHROPIC_API_KEY'], 'anthropic-version': '2023-06-01',
        'content-type': 'application/json'})
    cafile = '/etc/ssl/cert.pem' if os.path.exists('/etc/ssl/cert.pem') else None  # python.org builds on macOS ship without CA certs
    with urllib.request.urlopen(req, timeout=180, context=ssl.create_default_context(cafile=cafile)) as r:
        out = json.load(r)
    return ''.join(b.get('text', '') for b in out['content'])

def parse_json(text):
    a, b = text.find('{'), text.rfind('}')
    return json.loads(text[a:b + 1])

def clean(points, table, need_cite=True):
    ok = []
    for p in points or []:
        ids = [f for f in p.get('facts', []) if f in table]
        if isinstance(p.get('text'), str) and p['text'].strip() and (ids or not need_cite):
            ok.append({'text': p['text'].strip(), 'facts': ids})
    return ok

def compare(state, race, question):
    data = json.load(open(os.path.join(ROOT, 'data', 'candidates.json')))
    topics = json.load(open(os.path.join(ROOT, 'data', 'topics.json')))
    cands = [c for c in data['candidates'] if c['state'] == state and race_key(c) == race]
    if len(cands) < 2:
        return {'error': 'A comparison needs at least two candidates in the race.'}, 400
    facts, table = build_facts(cands, topics)
    names = '; '.join(f'{c["name"]} ({c["ticket"]})' for c in cands)
    user = f'Race: {cands[0]["office"]}{" district " + str(cands[0]["district"]) if cands[0].get("district") else ""}.\nCandidates: {names}.\n\nFACTS (id | candidate | topic | kind | text):\n{facts}\n\n'
    user += (f'Voter question: {question}\nAnswer only from the facts, in the same JSON shape, using one topic entry per area the question touches.'
             if question else 'Produce the full comparison across every topic where at least one candidate has facts.')
    key = hashlib.sha256((user + MODEL).encode()).hexdigest()
    if key in CACHE: return CACHE[key], 200
    res = None
    for _ in range(2):
        try:
            res = parse_json(call_claude(SYSTEM, user)); break
        except (ValueError, KeyError):
            continue
    if res is None:
        return {'error': 'The agent returned an unreadable answer. Please try again.'}, 502
    out = {'summary': clean(res.get('summary'), table), 'topics': []}
    for t in res.get('topics', []):
        out['topics'].append({'topic': str(t.get('topic', '')),
            'similarities': clean(t.get('similarities'), table), 'differences': clean(t.get('differences'), table),
            'gaps': clean(t.get('gaps'), table, need_cite=False)})
    out['topics'] = [t for t in out['topics'] if t['similarities'] or t['differences'] or t['gaps']]
    out['facts'] = {k: v for k, v in table.items()}
    out['model'] = MODEL
    CACHE[key] = out
    return out, 200

SLUG = lambda t: re.sub(r'^-|-$', '', re.sub(r'[^a-z]+', '-', t.lower()))

def race_key(c):
    if c['office'] == 'U.S. House': return f'house-{c["district"]}'
    if c['office'] == 'State Senate': return f'senate-{c["district"]}'
    return SLUG(c['office'])

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != '/api/compare':
            return self.reply({'error': 'Not found'}, 404)
        if not os.environ.get('ANTHROPIC_API_KEY'):
            return self.reply({'error': 'nokey'}, 503)
        try:
            req = json.loads(self.rfile.read(int(self.headers.get('content-length', 0))))
            q = (req.get('question') or '').strip()[:500]
            body, code = compare(str(req['state']), str(req['race']), q)
        except urllib.error.URLError as e:
            body, code = {'error': f'Could not reach the Anthropic API ({e.reason}).'}, 502
        except Exception as e:
            body, code = {'error': f'Request failed: {type(e).__name__}'}, 400
        self.reply(body, code)
    def reply(self, obj, code):
        b = json.dumps(obj).encode()
        self.send_response(code); self.send_header('content-type', 'application/json')
        self.send_header('content-length', str(len(b))); self.end_headers(); self.wfile.write(b)

if __name__ == '__main__':
    h = functools.partial(Handler, directory=ROOT)
    print(f'http://localhost:{PORT}  agent: {"ON (" + MODEL + ")" if os.environ.get("ANTHROPIC_API_KEY") else "OFF (set ANTHROPIC_API_KEY)"}')
    http.server.ThreadingHTTPServer(('127.0.0.1', PORT), h).serve_forever()

"""Shared helpers for the per-candidate research modules."""

def make(BYID, add_src):
    def reviewed(cid, key, title, url):
        c = BYID[cid]
        add_src(cid, key, title, url)
        c["reviewed"] = key
        c["unreviewed"] = False
        c["accessed"] = "2026-10-22"

    def _topic(cid, topic):
        t = BYID[cid]["topics"]
        cur = t.get(topic)
        if not isinstance(cur, dict):
            cur = t[topic] = {"gap": True, "said": [], "plan": []}
        return cur

    def web(cid, topic, *paras):
        cur = _topic(cid, topic)
        cur.setdefault("paras", []).extend(paras)
        cur["gap"] = False

    def plan(cid, topic, *paras):
        _topic(cid, topic).setdefault("plan", []).extend(paras)

    return reviewed, web, plan

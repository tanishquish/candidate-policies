"""State Senate District 36 (open seat): Joe Kelly (R) and added debate material for Jill Oberlander (D).

Sources are Greenwich Free Press articles whose text loads with JavaScript; the text was copied from a
real browser session into tools/rendered/ so verify_quotes.py can check each quote.
"""
import helpers


def build(BYID, T, Q, add_src):
    reviewed, web, plan = helpers.make(BYID, add_src)
    base = "https://greenwichfreepress.com/news/government/"
    ann = ("ann", "Greenwich Free Press: Greenwich’s Joe Kelly Announces Run for State Senate in 36th District (Mar. 6, 2026)", base + "greenwichs-joe-kelly-announces-run-for-state-senate-in-36th-district-244700/")
    rh = ("rh", "Greenwich Free Press: Round Hill Association Hosts Debate for State Senate 36th District (Oct. 8, 2026)", base + "round-hill-association-hosts-debate-for-state-senate-36th-district-255043/")
    lw = ("lw", "Greenwich Free Press: LWV Greenwich Candidates Debate (Oct. 16, 2026)", base + "lwv-greenwich-candidates-debate-inflation-affordability-taxes-reproductive-rights-gun-safety-255373/")
    RH = "Round Hill Association debate (Oct. 7, 2026) between Joe Kelly and Jill Oberlander, as reported by the Greenwich Free Press. "
    LW = "League of Women Voters Greenwich debate (Oct. 14, 2026) between Joe Kelly and Jill Oberlander, as reported by the Greenwich Free Press. "

    # ---- Joe Kelly (R): no campaign website found; profile built from news coverage
    k = "ct-sen-36-kelly"
    for s in (ann, rh, lw):
        add_src(k, *s)
    BYID[k]["unreviewed"] = False
    BYID[k]["accessed"] = "2026-10-22"
    BYID[k]["overview"].append([T("At his March 2026 campaign announcement he said "), Q("Public service should bring people together to solve problems", "ann"), T(".")])
    BYID[k]["overview"].append([T("The announcement also described him as a Greenwich Board of Estimate and Taxation member and former Board of Education chair.", "ann")])

    def said(cid, topic, when, ctx, *segs):
        t = BYID[cid]["topics"]
        if not isinstance(t.get(topic), dict):
            t[topic] = {"gap": True, "said": [], "plan": []}
        t[topic].setdefault("said", []).append({"when": when, "context": ctx, "seg": list(segs)})

    said(k, "abortion", "2026-10-14", LW + "Asked about reproductive rights and abortion; the article notes that in 2020 he had said he had not made up his mind.",
         Q("I’m pro-choice", "lw"), T(", adding: "), Q("I was brought up as a Catholic with 16 years of Catholic education. I have three strong daughters and a strong wife. There’s no way I can argue any other way.", "lw"))
    said(k, "guns", "2026-10-14", LW + "Asked whether he would have supported the 2026 law (Public Act 26-41) banning pistols that can easily be converted into automatic weapons.",
         Q("If a device is going to turn a handgun into an automatic weapon, that is bad. We should not vote in favor of that", "lw"))
    said(k, "taxes", "2026-10-07", RH + "Asked about the state’s unfunded pension liabilities.",
         Q("We have to take bold moves in order to fix that by stimulating business. How do we do that? By lowering taxes", "rh"))
    plan(k, "taxes", [Q("You have to cut the taxes.", "lw"), T(" The Greenwich Free Press also reported he talked about removing the public benefit charge from electricity bills.", "lw")])
    said(k, "economy", "2026-10-07", RH, Q("Jobs are leaving, we can’t have that. We have to stimulate the state by making it more attractive", "rh"))
    plan(k, "economy", [Q("I think 8-30g has created an adversarial relationship between the municipalities and Hartford", "rh"), T(", and on repealing it: "), Q("We’d vote it out", "rh"), T(".")])
    said(k, "healthcare", "2026-10-07", RH + "Asked about rising health insurance premiums.",
         Q("Healthcare should be a right, but I can’t have health care be run by the government because the government doesn’t run things well.", "rh"))
    said(k, "education", "2026-10-07", RH + "Asked about federal funding cuts to healthcare and education.",
         Q("We do have to make sure we fund our schools.", "rh"), T(" "), Q("whatever is going to happen with federal funding, we have to have to make up for it with the state, because we can’t put our schools at risk", "rh"))
    plan(k, "education", [Q("we have to have to make up for it with the state, because we can’t put our schools at risk", "rh")])
    said(k, "climate", "2026-10-07", RH + "Asked about data centers.",
         T("The Greenwich Free Press reported he said building a data center would only create temporary construction jobs, since data centers employ few permanent workers.", "rh"))
    plan(k, "economy", [Q("If elected, I will continue working to ensure Connecticut lives within its means while strengthening the communities we call home.", "ann")])

    # ---- Jill Oberlander (D): add debate statements to her reviewed profile
    o = "ct-sen-36-oberlander"
    for s in (rh, lw):
        add_src(o, *s)
    said(o, "abortion", "2026-10-14", LW + "Asked about reproductive rights and abortion; she said her father was an OB/GYN.",
         Q("These days it goes beyond saying, ‘I support the right to choose,’", "lw"), T(" and added it was also important to support doctors, healthcare providers and access to services including prescriptions and counseling.", "lw"))
    said(o, "guns", "2026-10-14", LW + "Asked whether she would have supported the 2026 convertible-pistol law.",
         Q("And I will vote that way for any gun violence prevention bill. Anything that will keep our children and residents safe from gun violence, I will be a strong supporter of.", "lw"))
    said(o, "taxes", "2026-10-14", LW,
         Q("I would work hard to bring money back to our district and I would not support new taxes", "lw"))
    said(o, "climate", "2026-10-07", RH + "Asked about data centers.",
         Q("I think New York has the right approach. I think we should pause consideration on any data center", "rh"))
    said(o, "economy", "2026-10-07", RH + "Asked what she would change about the 8-30g affordable housing law.",
         Q("What I won’t do is give into pressure to support bills that aren’t good for our community. I will be an advocate for our district and our local zoning laws.", "rh"))
    plan(o, "economy", [Q("In Hartford, I want to be the liaison between the municipalities and the State to ensure we’re getting the support we need and to push back and fight against overreach on the part of the state.", "rh")])

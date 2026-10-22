"""Positions and plans for statewide and State Senate candidates whose websites have been reviewed.

Called from build_data.py after extra_candidates. A candidate listed here is no longer flagged
"in progress"; topics not mentioned say the candidate's website does not address them.
"""

def build(BYID, T, Q, add_src):
    def reviewed(cid, key, title, url):
        c = BYID[cid]
        add_src(cid, key, title, url)
        c["reviewed"] = key
        c["unreviewed"] = False
        c["accessed"] = "2026-10-22"

    def web(cid, topic, *paras):
        t = BYID[cid]["topics"]
        cur = t.get(topic)
        if not isinstance(cur, dict):
            cur = t[topic] = {"gap": True, "said": [], "plan": []}
        cur.setdefault("paras", []).extend(paras)
        cur["gap"] = False

    def plan(cid, topic, *paras):
        t = BYID[cid]["topics"]
        cur = t.get(topic)
        if not isinstance(cur, dict):
            cur = t[topic] = {"gap": True, "said": [], "plan": []}
        cur.setdefault("plan", []).extend(paras)

    # ---------------- Sam Nestor (D), Senate 26 ----------------
    c = "ct-sen-26-nestor"
    reviewed(c, "nv", "Sam Nestor for State Senate: Vision", "https://www.samforct.com/vision")
    CIV = "I am absolutely committed to protecting civil rights, free speech, equality, women's rights, bodily autonomy, LGBTQIA+ rights, healthcare, voting rights, religious freedoms, and freedom of the press"
    web(c, "abortion", [T("Her vision page says "), Q(CIV, "nv"), T(".")])
    web(c, "lgbtq", [T("Her vision page says "), Q(CIV, "nv"), T(".")])
    web(c, "healthcare", [T("She says "), Q("Healthcare costs are one of the main drivers of municipal budgets, school budgets, the cost of running a business, and our own household budgets.", "nv")])
    plan(c, "healthcare", [Q("I will work to hold insurers accountable, to ensure it’s not just urban centers that have access to quality care, and find solutions to ever rising costs", "nv"), T(".")])
    web(c, "education", [T("She says "), Q("outstanding public education is near and dear to my heart", "nv"), T(".")])
    plan(c, "education", [Q("fully funding special education", "nv"), T(", and "), Q("I will promote and support alternative pathways to work, though career training, community college, and trade schools", "nv"), T(".")])
    web(c, "climate", [T("She says "), Q("The cost of energy is an enormous burden for households, businesses, and government.", "nv")])
    plan(c, "climate",
        [T("Short term: "), Q("I will advocate for increased funding for programs that bridge the gap on energy bills for those who can’t make ends meet", "nv"), T(".")],
        [T("Long term: "), Q("we need to double down on renewable energy sources", "nv"), T(", and "), Q("I will propose policies that make it easier for homeowners, businesses, and towns to build renewable energy capacity", "nv"), T(".")])
    web(c, "economy", [T("She says "), Q("Solving the housing crisis in Connecticut is key to solving the affordability crisis", "nv"), T(".")])
    plan(c, "economy", [Q("if we don’t make it profitable for builders to build, lots remain undeveloped", "nv"), T(", and "), Q("we can help lower administrative costs for builders without sacrificing environmental or regulatory compliance", "nv"), T(".")])

    # ---------------- Alma Sarelli (R), Senate 26 ----------------
    c = "ct-sen-26-sarelli"
    reviewed(c, "si", "Alma Sarelli for State Senate: Issues", "https://votealma.com/issues/")
    web(c, "economy", [T("Her issues page says her campaign is focused on "), Q("making Connecticut more affordable, protecting local control, preserving educational excellence, and strengthening support for special education", "si"), T(".")])
    plan(c, "economy", [Q("fight to protect local zoning authority, oppose unfunded mandates, and require infrastructure planning before major development moves forward", "si"), T(".")])
    plan(c, "taxes", [Q("oppose unfunded mandates", "si"), T(" and "), Q("protect taxpayers", "si"), T(".")])
    web(c, "education", [T("She says "), Q("strong schools and taxpayer accountability must go together", "si"), T(".")])
    plan(c, "education", [Q("support excellent schools, require clear cost controls, improve traffic and parking planning, protect neighborhoods, and keep residents involved before major decisions are made", "si"), T(", and "), Q("push for more responsible state support for education and special education", "si"), T(".")])

    # ---------------- Jill Oberlander (D), Senate 36 ----------------
    c = "ct-sen-36-oberlander"
    reviewed(c, "oi", "Jill Oberlander for State Senate: Jill on the Issues", "https://jilloberlander.com/jill-on-the-issues/")
    web(c, "climate", [T("Her site says "), Q("ratepayers deserve greater transparency and accountability", "oi"), T(".")])
    plan(c, "climate", [Q("Strengthen utility accountability and transparency in the rate-setting process.", "oi")], [Q("Audit ratepayer-funded programs and protect effective energy-assistance programs.", "oi")])
    web(c, "taxes", [T("Her site says "), Q("fiscal discipline and strong public services can go hand in hand", "oi"), T(".")])
    plan(c, "taxes", [Q("Oppose broad-based tax increases and maintain Connecticut’s fiscal guardrails.", "oi")], [Q("Reduce state-to-local cost shifting that puts pressure on property taxes.", "oi")])
    web(c, "economy", [T("Her site says "), Q("we should make it easier and less expensive to start and grow a business here", "oi"), T(".")])
    plan(c, "economy", [Q("Cut unnecessary red tape for businesses.", "oi")], [Q("Expand apprenticeships and workforce training that lead to jobs.", "oi")])
    web(c, "education", [T("Her site says "), Q("the state should be a reliable funding partner", "oi"), T(".")])
    plan(c, "education", [Q("Strengthen state support for local schools and improve Educational Cost Sharing funding.", "oi")], [Q("Increase support for special education so local taxpayers aren’t left carrying disproportionate costs.", "oi")])
    web(c, "healthcare", [Q("The rising cost of healthcare is straining families, seniors, small businesses and self-employed residents.", "oi")])
    plan(c, "healthcare", [Q("Expand insurance-pooling options for small businesses and nonprofits.", "oi")], [Q("Work to reduce premiums for families who purchase their own coverage.", "oi")])

    # ---------------- William Tong (D), Attorney General ----------------
    c = "ct-attorney-general-tong"
    reviewed(c, "ta", "William Tong for Attorney General: About", "https://www.williamtong.com/about/")
    web(c, "abortion", [T("His site says he is "), Q("fighting hard against extremist threats to our reproductive freedom and healthcare", "ta"), T(".")])
    web(c, "guns", [T("His site says he is fighting "), Q("challenges to our post-Sandy Hook gun laws", "ta"), T(".")])
    web(c, "economy", [T("His site says he "), Q("stood up to our state’s utilities to stop $700 million in rate increases", "ta"), T(".")])

    # ---------------- Erick Russell (D), Treasurer ----------------
    c = "ct-treasurer-russell"
    reviewed(c, "ra", "Erick Russell for State Treasurer: About", "https://www.erickforct.com/about")
    web(c, "abortion", [T("His site says the Treasurer’s Office has "), Q("leveraged private donations to protect access to reproductive and gender-affirming care", "ra"), T(".")])
    web(c, "lgbtq", [T("His site says the Treasurer’s Office has "), Q("leveraged private donations to protect access to reproductive and gender-affirming care", "ra"), T(".")])
    web(c, "economy", [T("His site highlights "), Q("launching CT Baby Bonds, a first-in-the-nation program that invests directly in the future of Connecticut’s children", "ra"), T(".")])
    web(c, "education", [T("His site says Baby Bonds give children "), Q("the financial resources to buy a home, start a business, pursue college or vocational training, or build toward a dignified retirement", "ra"), T(".")])

    # ---------------- Fred Wilms (R), Treasurer ----------------
    c = "ct-treasurer-wilms"
    reviewed(c, "wh", "Fred Wilms for State Treasurer", "https://www.fredforconnecticut.com/")
    web(c, "taxes", [T("His site says the budget he helped pass as a legislator "), Q("put in fiscal guardrails, respected the constitutional spending cap, boosted the Rainy-Day Fund, and pushed for long-overdue pension reform", "wh"), T(".")])
    web(c, "economy", [Q("Connecticut deserves a State Treasurer who puts performance over politics.", "wh")])
    plan(c, "economy", [T("He says voters deserve "), Q("better oversight, better returns, and a stronger financial future", "wh"), T(" for the state’s pension system.")])

    # ---------------- Jen Tooker (R), Comptroller ----------------
    c = "ct-comptroller-tooker"
    reviewed(c, "tk", "Jen Tooker for Comptroller", "https://www.jentooker.com/")
    web(c, "economy", [Q("Connecticut doesn’t have a revenue problem, it has a trust problem.", "tk")])
    plan(c, "economy", [T("She says she is running "), Q("to restore accountability, transparency, and discipline to Connecticut’s finances", "tk"), T(".")])
    web(c, "education", [T("Her site says she wants to "), Q("ensure access to great schools for every student because she believes that your zip code should not determine your opportunities in life", "tk"), T(".")])

    # ---------------- Susan Bysiewicz (D), Lieutenant Governor ----------------
    c = "ct-lieutenant-governor-bysiewicz"
    reviewed(c, "bh", "Susan Bysiewicz for Lieutenant Governor", "https://bysiewiczforct.com")
    REC = "Together, the Lamont-Bysiewicz Administration has delivered real results"
    web(c, "taxes", [T("Her site says the Lamont-Bysiewicz administration has delivered "), Q("two historic tax cuts", "bh"), T(".")])
    web(c, "healthcare", [T("Her site says the administration "), Q("reduced the cost of insulin", "bh"), T(".")])
    web(c, "economy", [T("Her site says the administration "), Q("raised the state minimum wage", "bh"), T(".")])
    web(c, "education", [T("Her site says the administration "), Q("expanded access to affordable, high-quality childcare", "bh"), T(".")])

"""State Senate Districts 28 and 26 (open seats): added news and questionnaire coverage (Oct. 22, 2026)."""
import helpers


def build(BYID, T, Q, add_src):
    reviewed, web, plan = helpers.make(BYID, add_src)

    def said(cid, topic, when, ctx, *segs):
        t = BYID[cid]["topics"]
        if not isinstance(t.get(topic), dict):
            t[topic] = {"gap": True, "said": [], "plan": []}
        t[topic].setdefault("said", []).append({"when": when, "context": ctx, "seg": list(segs)})

    # ================= District 28 =================
    # ---- Rob Blanchard (D)
    b = "ct-sen-28-blanchard"
    add_src(b, "pq", "Patch: Patch Candidate Profile: Rob Blanchard, 28th Senate District (Oct. 16, 2026)", "https://patch.com/connecticut/fairfield/patch-candidate-profile-rob-blanchard-28th-senate-district")
    add_src(b, "nj", "CT News Junkie: Lamont Staffer Announces Run For State Senate Seat (Apr. 1, 2026)", "https://ctnewsjunkie.com/2026/04/01/lamont-staffer-announces-run-for-state-senate-seat/")
    PQ = "Patch candidate questionnaire (answers written by the candidate). "
    said(b, "abortion", "2026-10-16", PQ + "In answer to “Why are you seeking this office?”",
         Q("defend our fundamental rights, such as a woman’s right to reproductive freedom and access to paid family and medical leave, regardless of who is in the White House", "pq"))
    plan(b, "guns", [Q("I will fund public safety, strengthen red flag gun laws that save lives, and pass gun safety laws.", "pq")])
    said(b, "taxes", "2026-10-16", PQ + "In answer to “What do you believe is the No. 1 issue facing Connecticut, and how do you plan to address it?”",
         Q("I’ll back tax relief that puts money straight into family budgets, like the Earned Income Tax Credit, the Child Tax Credit, and the property tax credit.", "pq"))
    plan(b, "taxes", [Q("I’ll fight for more municipal aid and bonding so our towns can fund their schools without reaching deeper into homeowners’ pockets.", "pq")])
    said(b, "healthcare", "2026-10-16", PQ + "Same answer.",
         Q("I’ll support letting small employers join together to buy coverage at a lower price, with the key ACA protections intact.", "pq"))
    said(b, "healthcare", "2026-04-01", "Quoted in CT News Junkie’s report on his campaign announcement.",
         Q("Every kid deserves pre-K, families need an affordable public healthcare option they can actually count on, and we have to hold utility companies accountable.", "nj"))
    plan(b, "healthcare", [Q("push down the cost of prescriptions, protect and strengthen paid family and medical leave, and invest in and expand our childcare endowment", "pq")])
    said(b, "climate", "2026-10-16", PQ + "In answer to “Energy costs have been soaring in Connecticut. What are your plans to help address this issue?”",
         Q("I’ll start by protecting what’s working: the fixed-price nuclear contracts that shield us from price spikes, and the new rule that stops utilities from billing customers for lobbying, PR, and political donations.", "pq"))
    plan(b, "climate", [Q("Then I’ll go line by line through the public benefits charge.", "pq"), T(" "), Q("Anything that doesn’t earn its place on your bill should go.", "pq")])
    said(b, "economy", "2026-10-16", PQ + "In answer to “Why are you seeking this office?”",
         Q("towns should take the lead on where and how they grow", "pq"))
    plan(b, "economy",
        [Q("reform 830-g, repurpose existing buildings, and protect our watershed and open space from overdevelopment", "pq")],
        [Q("we must invest in a workforce that attracts and trains the next generation of teachers, health care and public safety professionals, mental health workers, and manufacturers", "pq")])
    plan(b, "education", [Q("Every kid deserves pre-K", "nj")])
    BYID[b]["overview"].append([T("He describes himself, in the Patch questionnaire, as having served as "), Q("Governor Lamont's communications director", "pq"), T(".")])

    # ---- Amybeth Laroche (R): no campaign website or questionnaire found; profile built from news coverage
    l = "ct-sen-28-laroche"
    add_src(l, "nb", "The Newtown Bee: Newtown Resident Amybeth Laroche Officially Announces Campaign For State Senate (Feb. 13, 2026)", "https://www.newtownbee.com/02132026/newtown-resident-amybeth-laroche-officially-announces-campaign-for-state-senate/")
    BYID[l]["unreviewed"] = False
    BYID[l]["accessed"] = "2026-10-22"
    NB = "Remarks at her campaign kickoff event in Newtown, as reported by The Newtown Bee. "
    BYID[l]["overview"].append([T("At her campaign launch she said she ran for Newtown’s Board of Finance because she believed the town "), Q("deserved fiscal discipline, transparency, and respect for taxpayer dollars", "nb"), T(".")])
    PRI = "real tax relief, lower energy costs, lower health care costs, housing solutions rooted in local control, child care and workforce pathways, transparency, and accountability"
    said(l, "taxes", "2026-02-13", NB + "She listed her priorities.", T("She said her priorities are "), Q(PRI, "nb"), T("."))
    said(l, "climate", "2026-02-13", NB + "She listed her priorities.", T("She said her priorities include "), Q("lower energy costs", "nb"), T("."))
    said(l, "healthcare", "2026-02-13", NB + "She listed her priorities.", T("She said her priorities include "), Q("lower health care costs", "nb"), T("."))
    said(l, "economy", "2026-02-13", NB + "She listed her priorities.", T("She said her priorities include "), Q("housing solutions rooted in local control, child care and workforce pathways", "nb"), T("."))

    # ================= District 26 =================
    s = "ct-sen-26-sarelli"
    n = "ct-sen-26-nestor"
    add_src(s, "nod", "Westport Journal: RTM Member Alma Sarelli receives GOP nod for state senate District 26 (May 23, 2026)", "https://westportjournal.com/politics/rtm-member-alma-sarelli-receives-gop-nod-for-state-senate-district-26/")
    add_src(s, "lwv", "Westport Journal: Westport LWV debate is latest cancelled reportedly for Sarelli’s non-participation (Oct. 9, 2026)", "https://westportjournal.com/politics/westport-lvw-debate-is-latest-cancelled-reportedly-for-sarellis-non-participation/")
    add_src(n, "lwv", "Westport Journal: Westport LWV debate is latest cancelled reportedly for Sarelli’s non-participation (Oct. 9, 2026)", "https://westportjournal.com/politics/westport-lvw-debate-is-latest-cancelled-reportedly-for-sarellis-non-participation/")
    said(s, "economy", "2026-05-23", "Statement after winning the Republican nomination, as reported by the Westport Journal.",
         Q("Decisions affecting our towns should be made by locally elected officials, not transferred by state politicians to bureaucrats in Hartford", "nod"))
    BYID[s]["overview"].append([T("The Westport Journal reported that League of Women Voters debates in the district were canceled because Sarelli's campaign said she would not participate or she did not respond to invitations, and that she did not respond to the Journal's request for comment.", "lwv")])
    BYID[n]["overview"].append([T("The Westport Journal reported that League of Women Voters debates in the district were canceled after the Republican candidate did not take part; Nestor said she was "), Q("disappointed", "lwv"), T(" that she would not get to debate.")])

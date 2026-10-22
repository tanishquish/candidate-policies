"""Contested incumbent State Senate races (Districts 2, 17, 34, 35): Patch candidate questionnaires and news (Oct. 22, 2026)."""
import helpers


def build(BYID, T, Q, add_src):
    reviewed, web, plan = helpers.make(BYID, add_src)

    def said(cid, topic, when, ctx, *segs):
        t = BYID[cid]["topics"]
        if not isinstance(t.get(topic), dict):
            t[topic] = {"gap": True, "said": [], "plan": []}
        t[topic].setdefault("said", []).append({"when": when, "context": ctx, "seg": list(segs)})

    PQ = "Patch candidate questionnaire (answers written by the candidate). "
    NO1 = PQ + "In answer to “What do you believe is the No. 1 issue facing Connecticut, and how do you plan to address it?” "
    EN = PQ + "In answer to “Energy costs have been soaring in Connecticut. What are your plans to help address this issue?” "
    AF = PQ + "In answer to “Affordability has been a major topic across the country and here in Connecticut. How do you plan to address this issue?” "
    WHY = PQ + "In answer to “Why are you seeking this office?” "

    def patch(cid, title, url):
        add_src(cid, "pq", title, url)

    # ---------------- District 34 ----------------
    c = "ct-sen-34-cicarella"
    patch(c, "Patch: Candidate Profile: Paul Cicarella, 34th State Senate District (Oct. 16, 2026)", "https://patch.com/connecticut/northhaven/candidate-profile-paul-cicarella-34th-state-senate-district-0")
    BYID[c]["unreviewed"] = False; BYID[c]["accessed"] = "2026-10-22"
    said(c, "taxes", "2026-10-16", AF, Q("My focus is simple: keep more money in people’s pockets, control state spending, and make Connecticut a place where families can afford to live, work, and retire.", "pq"))
    plan(c, "taxes", [Q("Eliminating the Highway Use Tax", "pq"), T(", "), Q("Eliminating Sales Tax on Meals sold at Grocery Stores", "pq"), T(", and "), Q("Implementing a Gas Tax Holiday", "pq"), T(" are among the measures he lists.")])
    said(c, "climate", "2026-10-16", EN, Q("eliminate the Public Benefits Charge on electric bills, cap long-term power purchase agreements (PPAs) to prevent ratepayers from being locked into contracts at prices substantially above market rates, and return all proceeds from the Regional Greenhouse Gas Initiative (RGGI) directly to ratepayers through electricity-bill relief", "pq"))
    plan(c, "climate", [Q("eliminate the Public Benefits Charge on electric bills, cap long-term power purchase agreements (PPAs) to prevent ratepayers from being locked into contracts at prices substantially above market rates, and return all proceeds from the Regional Greenhouse Gas Initiative (RGGI) directly to ratepayers through electricity-bill relief", "pq")])
    said(c, "economy", "2026-10-16", WHY + "He listed what he would focus on if re-elected.", Q("Protecting local control by ensuring decisions reflect the needs of our communities, not one-size-fits-all mandates from Hartford.", "pq"))
    said(c, "education", "2026-10-16", WHY, Q("Delivering funding for our schools and fighting for a fairer education funding system.", "pq"))

    c = "ct-sen-34-mandato"
    patch(c, "Patch: Candidate Profile: Brandi Mandato, 34th State Senate District (Oct. 15, 2026)", "https://patch.com/connecticut/northhaven/candidate-profile-brandi-mandato-34th-state-senate-district-0")
    said(c, "taxes", "2026-10-15", NO1, Q("I will fight to reform Connecticut’s tax code so that the wealthiest individuals and most profitable corporations pay their fair share, while providing meaningful tax relief to working families and small businesses.", "pq"))
    said(c, "climate", "2026-10-15", EN, Q("I support giving municipalities and regional entities more flexibility to own and operate electric utilities, expanding access to affordable locally generated power, and making it easier for communities to pursue alternatives to investor-owned utilities.", "pq"))
    plan(c, "climate", [Q("I support giving municipalities and regional entities more flexibility to own and operate electric utilities, expanding access to affordable locally generated power, and making it easier for communities to pursue alternatives to investor-owned utilities.", "pq")])
    plan(c, "taxes", [Q("reforming Connecticut’s tax code to provide meaningful relief for working families and small businesses while asking the wealthiest individuals and most profitable corporations to contribute their fair share", "pq")])
    said(c, "healthcare", "2026-10-15", AF, Q("It means fully funding public education, expanding access to affordable childcare and paid family leave, protecting affordable housing, tackling healthcare and medical debt, and addressing the high cost of energy.", "pq"))
    said(c, "education", "2026-10-15", AF, Q("fully funding public education", "pq"))

    # ---------------- District 17 ----------------
    c = "ct-sen-17-cabrera"
    patch(c, "Patch: Candidate Profile: Jorge Cabrera, 17th State Senate District (Oct. 16, 2026)", "https://patch.com/connecticut/hamden/candidate-profile-jorge-cabrera-17th-state-senate-district")
    BYID[c]["unreviewed"] = False
    said(c, "economy", "2026-10-16", NO1, Q("The number one issue facing Connecticut families is affordability.", "pq"))
    said(c, "taxes", "2026-10-16", AF, Q("we also need to do more in terms of tax cuts, such as completely eliminating the state income tax on Social Security", "pq"))
    plan(c, "taxes", [Q("completely eliminating the state income tax on Social Security", "pq"), T(", and he says he would "), Q("look at other taxes like the property tax on motor vehicles", "pq"), T(".")])
    said(c, "healthcare", "2026-10-16", NO1, Q("As Chair of the Insurance and Real Estate Committee, I will also work to lower the cost of healthcare and prescription drugs so people aren’t choosing between everyday essentials and life-saving medicine.", "pq"))
    plan(c, "healthcare", [Q("work to lower the cost of healthcare and prescription drugs", "pq")])
    said(c, "climate", "2026-10-16", EN, Q("I think we can also look at ways to incentive towns to have their own utility companies similar to what a few towns do who pay far less in energy costs.", "pq"))
    plan(c, "climate", [Q("look at ways to incentive towns to have their own utility companies", "pq")])
    said(c, "education", "2026-10-16", NO1, Q("I will continue advocating for increased school and municipal funding that will help lower property taxes.", "pq"))

    c = "ct-sen-17-dorais"
    patch(c, "Patch: Candidate Profile: John-Paul Dorais, 17th State Senate District (Oct. 16, 2026)", "https://patch.com/connecticut/hamden/candidate-profile-john-paul-dorais-17th-state-senate-district")
    said(c, "taxes", "2026-10-16", NO1, Q("I would support meaningful tax relief, efforts to control property-tax growth, reducing unnecessary regulations and fees, and policies that make Connecticut more competitive for businesses and working families.", "pq"))
    said(c, "climate", "2026-10-16", EN, Q("I support reviewing programs currently funded through electric bills and determining which legitimate state programs should instead go through the normal state budget process", "pq"))
    plan(c, "climate", [Q("I also support reasonable limits on costly power-purchase agreements and requiring legislative approval before PURA creates new programs that increase costs for ratepayers.", "pq")])
    said(c, "economy", "2026-10-16", AF, Q("We also need to expand opportunities for skilled trades and apprenticeships so young people have pathways to good-paying careers without assuming a four-year college degree is the only option.", "pq"))

    # ---------------- District 2 ----------------
    c = "ct-sen-02-knotts"
    patch(c, "Patch: Patch Candidate Profile: Tim Knotts For 2nd State Senate (Oct. 21, 2026)", "https://patch.com/connecticut/windsor/patch-candidate-profile-tim-knotts-2nd-state-senate")
    said(c, "taxes", "2026-10-21", NO1, Q("We have to cut down on unfunded mandates, give an honest accounting of what we are taxing and spending, and stop government waste and fraud.", "pq"))
    plan(c, "taxes", [Q("We have to demand that ongoing costs are dealt with within the budget and not drive them out to bonding or down to towns.", "pq")])
    said(c, "climate", "2026-10-21", EN, Q("our state should not be in the business of underwriting or commanding their development", "pq"), T(" of new energy technologies."))
    said(c, "economy", "2026-10-21", NO1, Q("Connecticut has been unaffordable.", "pq"))

    c = "ct-sen-02-khan"
    add_src(c, "ctm", "CT Mirror: Doug McCrory loses Democratic primary for CT 2nd Senate District (Aug. 11, 2026)", "https://ctmirror.org/2026/08/11/doug-mccrory-primary-general-assembly-house-senate/")
    said(c, "taxes", "2026-08-11", "Statement after winning the Democratic primary, as reported by CT Mirror.", T("She said the district deserves "), Q("a government that taxes the wealthy their fair share, holds Eversource accountable, and puts real money into the neighborhood schools that raised us", "ctm"), T("."))
    plan(c, "climate", [T("In her primary-night statement she listed "), Q("holds Eversource accountable", "ctm"), T(" among her priorities.")])
    plan(c, "education", [T("In her primary-night statement she listed putting "), Q("real money into the neighborhood schools that raised us", "ctm"), T(" among her priorities.")])

    # ---------------- District 35 ----------------
    c = "ct-sen-35-werstler"
    add_src(c, "pl", "Patch: Woodstock's Ethan Werstler Launches Campaign For Connecticut's 35th Senate District (Apr. 6, 2026)", "https://patch.com/connecticut/stafford-willington/woodstocks-ethan-werstler-launches-campaign-connecticuts-35th-senate")
    BYID[c]["unreviewed"] = False; BYID[c]["accessed"] = "2026-10-22"
    said(c, "economy", "2026-04-06", "Patch’s report on his campaign launch.", T("Patch reported he is "), Q("launching a campaign centered on agriculture, housing, small business and rising costs in northeastern Connecticut", "pl"), T("."))

    # ---------------- District 35: Jeff Gordon (R, incumbent); District 32: Eric Berthel (R, incumbent) ----------------
    c = "ct-sen-35-gordon"
    add_src(c, "pg", "Patch: State Sen. Jeff Gordon Wins Unanimous Convention Endorsement In 35th District (May 20, 2026)", "https://patch.com/connecticut/stafford-willington/state-sen-jeff-gordon-wins-unanimous-convention-endorsement-35th")
    BYID[c]["unreviewed"] = False; BYID[c]["accessed"] = "2026-10-22"
    GL = "Statement quoted by Patch after his unanimous Republican convention endorsement. "
    said(c, "healthcare", "2026-05-20", GL, T("He listed "), Q("strengthening rural healthcare access", "pg"), T(" among the issues guiding his work."))
    said(c, "economy", "2026-05-20", GL, T("He listed "), Q("addressing affordability concerns", "pg"), T(", "), Q("helping small businesses", "pg"), T(" and "), Q("protecting taxpayers", "pg"), T("."))
    said(c, "education", "2026-05-20", GL, T("He listed "), Q("supporting public education", "pg"), T("."))

    c = "ct-sen-32-berthel"
    add_src(c, "pq", "Patch: CT Patch Candidate Profile: Eric Berthel For State Senator (Oct. 1, 2024)", "https://patch.com/connecticut/brookfield/ct-patch-candidate-profile-eric-berthel-state-senator")
    BQ = "Patch candidate questionnaire from his 2024 re-election campaign (answers written by the candidate). "
    said(c, "taxes", "2024-10-01", BQ + "In answer to “Why are you seeking this office?”", Q("My work has been focused on lowering taxes, lowering the cost of living, attracting new businesses and keeping our communities safe.", "pq"))
    said(c, "economy", "2024-10-01", BQ + "In answer to “What are the major differences between you and the other candidates?”", Q("I am a fiscal conservative who believes in smaller government, local control, lower taxes and creating opportunity for people to succeed", "pq"))
    plan(c, "taxes", [Q("I will continue to fight to reduce the burden caused by each of these issues.", "pq"), T(" (inflation, cost of living and taxes)")])

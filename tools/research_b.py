"""State Senate districts 12-22 (reviewed from candidates' own websites, Oct. 22, 2026)."""
import helpers


def build(BYID, T, Q, add_src):
    reviewed, web, plan = helpers.make(BYID, add_src)

    def official(cid):
        c = BYID[cid]
        reviewed(cid, "w", f"{c['name']}: legislator or campaign page (no policy statements)", c["website"])

    for cid in ["ct-sen-12-cohen", "ct-sen-13-fazzino", "ct-sen-15-hartley", "ct-sen-17-cabrera", "ct-sen-19-osten",
                "ct-sen-20-marx", "ct-sen-21-perillo", "ct-sen-22-gadkar-wilcox"]:
        official(cid)

    # ---- District 12: Lisa Deane (R)
    c = "ct-sen-12-deane"
    reviewed(c, "w", "Lisa Deane for State Senate", "https://www.deane2026.com")
    web(c, "taxes", [T("Her site says she is "), Q("committed to supporting immediate sales and income tax relief, the development of a state child tax deduction, and a reduction of small business filing fees to help facilitate economic development", "w"), T(".")])
    plan(c, "taxes", [Q("immediate sales and income tax relief, the development of a state child tax deduction, and a reduction of small business filing fees", "w")])
    plan(c, "safety", [Q("invest in police recruitment, revise the Police Accountability bill, and educate our youth on the dangers of intoxicated and distracted driving", "w")])

    # ---- District 14: Owen Weaver (R), James Maroney (D)
    c = "ct-sen-14-weaver"
    reviewed(c, "w", "Owen Weaver for State Senate: About", "https://www.owforsenate.com/about")
    add_src(c, "h", "Owen Weaver for State Senate (home page)", "https://www.owforsenate.com")
    web(c, "taxes", [T("His site says he wants "), Q("making the state more affordable through tax cuts and property tax relief", "w"), T(".")])
    web(c, "economy", [T("His site says "), Q("Connecticut’s top-down approach to affordable housing is both bad law and bad policy.", "h")])
    plan(c, "taxes", [Q("making the state more affordable through tax cuts and property tax relief", "w")])

    c = "ct-sen-14-maroney"
    reviewed(c, "w", "James Maroney for State Senate (home page)", "https://maroneyforus.com")
    add_src(c, "pg", "James Maroney for State Senate: Policy Goals", "https://maroneyforus.com/policy-goals/")
    web(c, "economy", [T("His site says his focus includes "), Q("cutting red tape for small businesses", "w"), T(".")])
    web(c, "education", [T("His policy-goals page says on early childhood education: "), Q("So, this is an investment in both Connecticut’s short term and long term workforce.", "pg")])
    plan(c, "education", [Q("James is excited to work with Senator Fonfara and other legislators on ECE policy.", "pg")])

    # ---- District 16: Jack Perry (D)
    c = "ct-sen-16-perry"
    reviewed(c, "w", "Jack Perry for State Senate", "https://www.voteforjackperry.com")
    add_src(c, "ab", "Jack Perry for State Senate: Meet Jack", "https://www.voteforjackperry.com/about")
    add_src(c, "en", "Jack Perry for State Senate: Perry Campaign Releases Energy Platform", "https://www.voteforjackperry.com/news/perry-campaign-releases-energy-platform")
    web(c, "taxes", [T("His site's slogan is "), Q("lower taxes, LOWER HOUSEHOLD COSTS, HOLD EVERSOURCE ACCOUNTABLE", "w"), T(".")])
    web(c, "climate", [Q("Your electric bill keeps climbing while Eversource posts record profits.", "w")])
    plan(c, "climate", [Q("Connecticut needs publicly-owned power grids.", "en")])
    plan(c, "economy", [Q("lowering costs, expanding access to child care and housing, and making sure small businesses and working families actually have a fair shot", "ab")])

    # ---- District 17: John-Paul Dorais (R)
    c = "ct-sen-17-dorais"
    reviewed(c, "w", "John-Paul Dorais for State Senate", "https://www.doraisforstatesenate.com")
    web(c, "taxes", [Q("Connecticut families work hard for their money. They should not have to watch more of every paycheck disappear into taxes while state government continues to grow.", "w")])
    plan(c, "taxes",
        [Q("Cap annual municipal property-tax levy increases at the greater of 2% or inflation, while allowing voters to approve exceptions for major projects.", "w")],
        [Q("Reduce Connecticut's Paid Family Leave payroll tax by 20%.", "w")],
        [T("His site cites a Senate Republican package that included "), Q("a $1 billion working- and middle-class income tax cut", "w"), T(".")])
    web(c, "climate", [Q("Connecticut families shouldn't dread opening their electric bills.", "w")])
    plan(c, "climate", [Q("A moratorium on data centers should be considered as an option.", "w")])
    web(c, "immigration", [T("His site says Senate Republicans "), Q("proposed public-safety exceptions to legislation restricting cooperation with federal authorities", "w"), T(".")])
    plan(c, "safety", [Q("recruiting and retaining qualified officers", "w")])
    web(c, "economy", [T("His site lists the priority "), Q("Protect Local Control of Housing Policy", "w"), T(".")])

    # ---- District 18: Joe de la Cruz (D)
    c = "ct-sen-18-cruz"
    reviewed(c, "w", "Joe de la Cruz for State Senate: Platform", "https://www.joeforct.com/platform")
    add_src(c, "h", "Joe de la Cruz for State Senate (home page)", "https://www.joeforct.com")
    web(c, "healthcare", [Q("Joe is fighting for universal health coverage so no family has to go without critical care, even when life circumstances change.", "w")])
    web(c, "guns", [T("His site says he and his wife "), Q("co-founded Community Speaks Out after losing a son to gun violence", "h"), T(".")])
    plan(c, "economy", [Q("securing paid family leave, to raising the minimum wage, to bringing down our energy costs", "w")])
    plan(c, "taxes", [Q("fight for lower taxes", "w")])

    # ---- District 19: Jason Guidone (R)
    c = "ct-sen-19-guidone"
    reviewed(c, "w", "Jason Guidone for State Senate", "https://www.guidoneforsenate.com")
    web(c, "taxes", [Q("I support responsible spending, transparency in government, and policies that keep taxes under control.", "w")])
    web(c, "education", [Q("I support strong parental involvement, a rigorous curriculum, and keeping education decisions in local hands", "w"), T(".")])
    web(c, "economy", [T("His site lists "), Q("Making Connecticut more affordable so families, retirees, and young people can afford to stay here.", "w")])

    # ---- District 20: Lee Elci (R)
    c = "ct-sen-20-elci"
    reviewed(c, "w", "Lee Elci for CT Senate: Platform", "https://www.leeelci.com/issues")
    add_src(c, "h", "Lee Elci for CT Senate (home page)", "https://www.leeelci.com")
    web(c, "taxes", [Q("Connecticut families are being taxed and priced out of their own state — while Hartford sits on surpluses instead of delivering relief.", "w")])
    plan(c, "taxes",
        [Q("Enact permanent, broad-based middle-class tax cuts, funded by real spending cuts, not gimmicks.", "w")],
        [Q("Impose a strict spending cap tied to inflation and population growth.", "w"), T(" "), Q("Ban hidden fee and tax hikes buried in budget implementer bills.", "w")])
    web(c, "safety", [Q("The 2020 police accountability law turned our officers into suspects instead of protectors, and it's driving good men and women out of the profession.", "w")])
    plan(c, "safety", [Q("Restore real legal protections for officers acting in good faith.", "w")])
    plan(c, "climate", [Q("Get public-benefit charges off your electric bill, keep Millstone working, and modernize the grid.", "h")])

    # ---- District 21: Carolann Reid (D)
    c = "ct-sen-21-reid"
    reviewed(c, "w", "Carolann Reid for State Senate: Issues", "https://www.reidforstatesenate.com/issues")
    web(c, "economy", [Q("Affordability and economic security are central challenges for District 21 and Connecticut.", "w")])
    plan(c, "taxes", [Q("I will advocate for a state child tax credit, meaningful property-tax relief, more affordable child care, and workforce development that connects residents to sustainable careers.", "w")])
    plan(c, "climate", [Q("I will push for greater scrutiny of utility costs, transparent electricity-rate decisions, and more affordable energy supplies without sacrificing reliability.", "w")])

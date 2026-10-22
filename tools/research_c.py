"""State Senate districts 23-35 (reviewed from candidates' own websites, Oct. 22, 2026)."""
import helpers


def build(BYID, T, Q, add_src):
    reviewed, web, plan = helpers.make(BYID, add_src)

    for cid in ["ct-sen-23-gaston", "ct-sen-29-flexer", "ct-sen-31-martin", "ct-sen-33-needleman"]:
        c = BYID[cid]
        reviewed(cid, "w", f"{c['name']}: legislator page (no policy statements)", c["website"])

    # ---- District 24: Julie Kushner (D), Melissa Lindsey (R)
    c = "ct-sen-24-kushner"
    reviewed(c, "w", "Julie Kushner for State Senate", "https://www.juliekushnerforct.com")
    web(c, "taxes", [T("Her site lists among her accomplishments "), Q("Passing two of the largest tax cuts in state history", "w"), T(".")])
    web(c, "economy", [T("Her site lists "), Q("Raising the minimum wage to $16.94", "w"), T(" among her accomplishments.")])
    web(c, "guns", [T("Her site lists "), Q("Taken action to reduce gun violence and ban ghost guns", "w"), T(".")])
    plan(c, "healthcare", [Q("Making health insurance affordable for the tens of thousands still struggling with costs", "w")])
    plan(c, "education", [Q("Ensuring schools are properly resourced to support special education students and multilingual learners", "w"), T(", and "), Q("Continuing investment in early childhood education to ensure our earliest learners can thrive and families can afford care", "w"), T(".")])

    c = "ct-sen-24-lindsey"
    reviewed(c, "w", "Melissa Lindsey for CT Senate: Issues", "https://www.lindseyforsenatect.com/issues")
    add_src(c, "af", "Melissa Lindsey for CT Senate: Affordability", "https://www.lindseyforsenatect.com/issues/affordability")
    web(c, "taxes", [Q("Connecticut families don’t need more hidden costs and higher taxes.", "af")])
    plan(c, "climate", [Q("Lower energy costs & electric bills by eliminating public benefits charge", "w"), T(", and "), Q("Connecticut must pursue a balanced, all-of-the-above energy strategy. This strategy should include nuclear, natural gas, and renewable energy.", "af")])
    web(c, "safety", [Q("I support law enforcement and believe safe communities are common sense.", "w")])

    # ---- District 26: handled in state_research (Nestor, Sarelli)

    # ---- District 28: Rob Blanchard (D)
    c = "ct-sen-28-blanchard"
    reviewed(c, "w", "Rob Blanchard for CT State Senate", "https://www.robblanchardct.com")
    web(c, "economy", [T("His site says he is "), Q("focused on making Connecticut more affordable by tackling the rising costs of housing, healthcare, and childcare, while supporting strong schools and vibrant local communities", "w"), T(".")])
    web(c, "healthcare", [T("His site says he is "), Q("tackling the rising costs of housing, healthcare, and childcare", "w"), T(".")])

    # ---- District 30: Aaron Zimmer (D)
    c = "ct-sen-30-zimmer"
    reviewed(c, "w", "Aaron Zimmer for State Senate (home page)", "https://www.zimmerforct.com")
    add_src(c, "pf", "Aaron Zimmer for State Senate: Platform", "https://www.zimmerforct.com/platform")
    add_src(c, "pp", "Aaron Zimmer for State Senate: Planned Parenthood Votes - Connecticut endorsement (posted on his site)", "https://www.zimmerforct.com/planned-parenthood-connecticut-votes-endorses-zimmer-for-the-state-senate")
    web(c, "taxes", [T("His site says he is running to "), Q("tax the ultra-rich", "w"), T(", and his platform says "), Q("Taxing the ultra-rich their fair share isn’t about class warfare or punishing success.", "pf")])
    web(c, "healthcare", [Q("Healthcare in Connecticut shouldn’t feel like a luxury. It should be a guarantee that every family can see a doctor, fill a prescription, and get the care they need without fear of financial ruin.", "pf")])
    web(c, "immigration", [Q("Every human being deserves the right to lead happy, healthy and dignified lives, regardless of economic or immigration statuses.", "pf")])
    web(c, "abortion", [T("A Planned Parenthood Votes–Connecticut endorsement posted on his site says "), Q("Aaron Zimmer will defend our right to choose.", "pp")])
    web(c, "economy", [Q("Lowering costs for Connecticut families is about more than just taxes and energy bills.", "pf")])

    # ---- District 31: Laurel LaPorte-Grimes (D)
    c = "ct-sen-31-laporte-grimes"
    reviewed(c, "w", "Laurel for State Senate: Platform", "https://www.laurelforsenate.com/platform")
    web(c, "economy", [Q("Working families, seniors, young adults, and small businesses are being squeezed from every direction.", "w")])
    plan(c, "healthcare", [Q("Make healthcare more affordable for families, workers, and small businesses", "w")])
    plan(c, "climate", [Q("Reduce energy costs and protect consumers from unreasonable rate increases", "w")])
    plan(c, "education", [Q("Provide free breakfast and lunch in our schools so every child can focus on learning", "w")])
    plan(c, "economy", [Q("Support practical solutions that make housing more affordable", "w")])
    plan(c, "taxes", [Q("Reduce reliance on property taxes to fund essential local services", "w")])

    # ---- District 32: Eric Berthel (R), Matt Knickerbocker (D)
    c = "ct-sen-32-berthel"
    reviewed(c, "w", "Eric Berthel for State Senate: About Eric", "https://www.berthelforsenate.org/about-eric")
    web(c, "education", [Q("He is a fierce advocate for public school education on all levels - student outcomes, teacher recruitment, funding and curriculum.", "w"), T(" "), Q("He is also outspoken about parental choice in education, including support of families who chose to homeschool their children.", "w")])

    c = "ct-sen-32-knickerbocker"
    reviewed(c, "w", "Matt Knickerbocker for Senate: Priorities", "https://www.mattknickerbocker.com/priorities")
    web(c, "education", [Q("Every child deserves a strong public education, no matter their ZIP code.", "w")])
    plan(c, "education", [Q("Matt will fight to secure our fair share of state funding so local taxpayers aren’t left filling the gap.", "w"), T(" "), Q("Matt will push for full reimbursement of excess special education costs", "w"), T(".")])
    web(c, "taxes", [Q("The state shouldn’t pass requirements without paying for them.", "w")])
    plan(c, "taxes", [Q("Matt will work to end this practice and ensure municipalities aren’t stuck covering costs for decisions made in Hartford.", "w")])
    plan(c, "economy", [Q("Matt will work to cut red tape", "w")])

    # ---- District 34: Brandi Mandato (D)
    c = "ct-sen-34-mandato"
    reviewed(c, "w", "Brandi Mandato for State Senate: About", "https://www.mandatofor34.com/about")
    web(c, "economy", [T("Her site says her work has focused on "), Q("to expand access to quality jobs, education pathways, including apprenticeships, trade schools, and higher education, and economic opportunity", "w"), T(".")])

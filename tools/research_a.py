"""State Senate districts 1-9 (reviewed from candidates' own websites, Oct. 22, 2026)."""
import helpers


def build(BYID, T, Q, add_src):
    reviewed, web, plan = helpers.make(BYID, add_src)

    # District 1: Fonfara (site is an official Senate Democrats profile with no policy text), Delgado (no site)
    reviewed("ct-sen-01-fonfara", "w", "Connecticut Senate Democrats: John Fonfara", "http://www.senatedems.ct.gov/Fonfara")
    reviewed("ct-sen-02-khan", "w", "Maryam Khan for State Senate", "https://www.khanforconn.com")
    reviewed("ct-sen-05-slap", "w", "Connecticut Senate Democrats: Derek Slap", "http://www.senatedems.ct.gov/slap")

    # ---- District 2: Tim Knotts (R)
    c = "ct-sen-02-knotts"
    reviewed(c, "w", "Tim Knotts for State Senate", "https://www.timknottsforsenate.com")
    web(c, "economy", [T("His site says he is running to "), Q("root out the waste and special-interest costs that have made Connecticut unaffordable for working families", "w"), T(".")])
    plan(c, "economy", [Q("Audit and roll back the hidden fees, surcharges, and middleman costs tacked onto utility bills, healthcare bills, motor vehicle bills, and tax bills.", "w")])
    web(c, "taxes", [Q("taxes should be called taxes", "w"), T(", he says in his list of priorities.")])
    web(c, "education", [T("His site says "), Q("parents are a child’s first and most important educator", "w"), T(".")])
    plan(c, "education", [Q("Strong, well-funded public schools, real parental involvement, and respect for every family’s educational choice without punishing any of them.", "w")])

    # ---- District 3: Eliott Hughes (R), Saud Anwar (D)
    c = "ct-sen-03-hughes"
    reviewed(c, "w", "Eliott Hughes for Senate", "https://eliotthughesforsenate.com")
    web(c, "taxes", [T("His site says "), Q("Taxes, fees, energy bills, and everyday costs keep climbing while too many voices get ignored at the Capitol.", "w")])
    plan(c, "taxes", [Q("I will focus on lowering income and property taxes, stopping the state from passing down hidden costs to our towns", "w"), T(".")])
    plan(c, "climate", [Q("pushing for energy policies that bring down utility bills", "w")])
    web(c, "education", [T("His site says "), Q("Parents should decide what’s best for their children — public school, private, or homeschool.", "w")])
    plan(c, "education", [Q("I will pursue school funding models that reward real student outcomes while protecting parent’s right to choose the best learning environment for their children including the right to homeschool.", "w")])
    plan(c, "economy", [Q("reduce burdens on small businesses", "w")])

    c = "ct-sen-03-anwar"
    reviewed(c, "w", "Dr. Saud Anwar for State Senate", "https://www.saudanwar.com")
    web(c, "healthcare", [T("His site says "), Q("he'll keep fighting rising insurance and prescription costs, defending coverage from federal cuts, and keeping private equity out of our hospitals", "w"), T(".")])
    plan(c, "healthcare", [T("He cites leading "), Q("Led Senate Bill 196, restricting future hospital sale-leaseback deals on main campuses", "w"), T(".")])
    web(c, "economy", [Q("Building on more than $600 million already saved for residents, he'll keep going after the everyday costs squeezing our families.", "w")])

    # ---- District 4: MD Rahman (D)
    c = "ct-sen-04-rahman"
    reviewed(c, "w", "MD Rahman for State Senate: Platform", "https://www.mdforsenate.com/platform")
    web(c, "abortion", [Q("Abortion is a woman’s right, fullstop.", "w")])
    plan(c, "abortion", [Q("MD will strongly oppose and stop Republican efforts to repeal any of the protections Democrats have enshrined in Connecticut law", "w"), T(".")])
    web(c, "lgbtq", [Q("MD will defend LGBTQ+ rights and supports access to medical care for all children and adults.", "w")])
    web(c, "healthcare", [T("His platform says "), Q("healthcare is a right, not a privilege", "w"), T(".")])
    plan(c, "healthcare", [Q("He’ll support a Public Option", "w"), T(", and "), Q("will always ensure our safety net is fully funded", "w"), T(".")])
    plan(c, "guns", [Q("MD will work to strengthen our prohibitions on ghost guns and illegal weapons, require training for firearm permits, and fund mental health and jobs programs to help stop violence before it starts.", "w")])
    web(c, "education", [Q("Education is the answer to so many of the obstacles faced by Connecticut families.", "w")])
    plan(c, "education", [Q("Providing the opportunity to attend community college and technical schools for free", "w"), T(", and "), Q("universal pre-Kindergarten", "w"), T(".")])
    plan(c, "climate", [Q("invest in our electric grid and electric-car charging infrastructure", "w")])
    plan(c, "economy", [Q("we need a state government that fosters growth through targeted investments, reduced college and technical school costs, and aligns our workforce with the jobs of tomorrow", "w")])

    # ---- District 7: David Kiner (D)
    c = "ct-sen-07-kiner"
    reviewed(c, "w", "David Kiner for State Senate: Priorities", "https://www.kinerforsenate.com/priorities")
    web(c, "economy", [T("His priorities page says "), Q("policies that lower everyday costs, expanding access to affordable housing, strengthening public transportation", "w"), T(".")])
    web(c, "climate", [T("His site says "), Q("utility companies must be held accountable when they put profits ahead of the people they serve", "w"), T(".")])
    plan(c, "climate", [Q("greater transparency in how utility rates are set", "w"), T(", and "), Q("push for reforms that put consumers first", "w"), T(".")])
    plan(c, "taxes", [Q("pursue policies that help communities fund essential services without relying so heavily on property tax increases", "w")])
    plan(c, "healthcare", [Q("expand access to affordable healthcare and prescriptions", "w")])
    web(c, "education", [T("His site says he will "), Q("advocate for fair and reliable education funding so schools have the resources they need to help students thrive", "w"), T(".")])

    # ---- District 7: John Kissel (R)
    c = "ct-sen-07-kissel"
    reviewed(c, "w", "John Kissel for State Senate", "https://www.johnkisselforsenate.com")
    web(c, "economy", [Q("John knows every state policy should help make Connecticut more affordable to live, work and raise a family.", "w")])
    web(c, "education", [Q("John will continue to fight for more state dollars for local education.", "w")])
    plan(c, "education", [Q("John is leading the fight for greater state support for special education teachers and programs, as well as early childhood education.", "w")])

    # ---- District 8: Mike Criss (R), Paul Honig (D)
    c = "ct-sen-08-criss"
    reviewed(c, "w", "Mike Criss for State Senate", "https://www.mikecriss.com")
    web(c, "taxes", [T("His site's slogan is "), Q("Lower Costs, Local Control", "w"), T(".")])
    plan(c, "taxes", [Q("Deliver real relief for homeowners and working families burdened by rising costs.", "w")])
    plan(c, "climate", [Q("Tackle the \"public benefits\" charges on your bill, stop policies that increase your rates", "w")])

    c = "ct-sen-08-honig"
    reviewed(c, "w", "Paul Honig for State Senate: Issues", "https://paulhonigforstatesenate.com/issues")
    web(c, "taxes", [T("His issues page says "), Q("I was proud to support Connecticut’s bipartisan balanced state budget that maintains the largest middle-class tax cut in state history.", "w")])
    web(c, "education", [T("His site lists a record that includes "), Q("Increased K-12 regular education funding more than $4.6 million", "w"), T(" and "), Q("Provided $1.4 million in grants for special ed", "w"), T(".")])

    # ---- District 9: Gwen Samuel (I), Matt Lesser (D)
    c = "ct-sen-09-samuel"
    reviewed(c, "w", "Gwen Samuel for State Senate: Issues", "https://gwenforct.com/issues")
    web(c, "economy", [T("Her issues page says "), Q("Affordability is more than one tax or one bill.", "w")])
    plan(c, "economy", [Q("Reduce unnecessary barriers and costs that make it harder for local businesses and entrepreneurs to grow.", "w")])
    plan(c, "taxes", [Q("Work to reduce the pressure placed on local property taxpayers by examining state mandates", "w")])
    plan(c, "climate", [Q("Push for greater transparency, accountability, competition, and long-term solutions to Connecticut's high energy costs.", "w")])
    plan(c, "healthcare", [Q("Support efforts that reduce out-of-pocket healthcare and prescription costs", "w")])
    web(c, "education", [T("Her site lists "), Q("Strong public schools and academic excellence", "w"), T(" and "), Q("Meaningful parental involvement and transparency", "w"), T(".")])

    c = "ct-sen-09-lesser"
    reviewed(c, "w", "Matt Lesser for State Senate", "https://www.mattlesser.com")
    web(c, "healthcare", [T("His site calls him "), Q("the leading voice for affordable health care", "w"), T(".")])
    web(c, "education", [T("His site calls him "), Q("a passionate advocate for public education", "w"), T(".")])
    web(c, "immigration", [T("His site says he is "), Q("leading the charge to protect our community from ICE & MAGA Republicans in Washington", "w"), T(".")])

    # ---- District 11: Rosa Pepper-Macias (Workers' Voice Party)
    c = "ct-sen-11-pepper-macias"
    reviewed(c, "w", "Workers' Voice Party: Rosa Pepper-Macias, Issues", "https://voteworkersvoice.net/issues")
    web(c, "immigration", [Q("Abolish ICE!", "w")])
    plan(c, "immigration", [Q("Stop all ICE raids, detentions and deportations", "w")])
    web(c, "defense", [Q("STOP the war and use the Pentagon’s trillion-dollar budget for jobs, education, housing, food, and healthcare as rights", "w")])
    plan(c, "taxes", [Q("No taxes on anyone earning $50,000 or less per year", "w"), T(", and "), Q("Tax all income above $250,000 at 95% (when federal income tax is included)", "w"), T(".")])
    web(c, "healthcare", [Q("Socialize and expand healthcare: For a unified public healthcare plan", "w")])
    web(c, "lgbtq", [Q("Equal rights for all regardless of their gender identity. Free access to gender-affirming care for all.", "w")])
    plan(c, "lgbtq", [Q("Re-establish all gender affirming care at all CT hospitals and make it free, as a human right", "w")])
    web(c, "abortion", [Q("Contraception, abortion and other reproductive services free and on demand", "w")])
    web(c, "education", [Q("Make all public colleges and universities tuition free", "w")])
    web(c, "climate", [Q("Workers' control over production to combat climate change and provide for human need, not for war, genocide and big tech authoritarianism", "w")])
    web(c, "economy", [Q("End unemployment with a shortened workweek compensated at full-time pay.", "w")])

    reviewed("ct-sen-11-paolillo", "w", "Connecticut House Democrats: Alphonse Paolillo", "http://www.housedems.ct.gov/Paolillo")

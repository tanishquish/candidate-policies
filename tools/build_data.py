#!/usr/bin/env python3
"""Source of truth for data/candidates.json (Connecticut, 2026).

Every statement is a segment: T(text, source) for a paraphrase, Q(quote, source) for a
verbatim quote. Run `python3 tools/build_data.py` to regenerate the JSON, then
`python3 tools/verify_quotes.py` to confirm each quote appears on the cited page.
"""
import json, pathlib

ACCESSED = "2026-10-15"
GREEN = "https://www.thegreenpapers.com/G26/CT"

def T(text, s=None):
    d = {"t": text}
    if s: d["s"] = s
    return d

def Q(quote, s):
    return {"q": quote, "s": s}

def src(key, title, url):
    return {"key": key, "title": title, "url": url}

BALLOT = src("ballot", "The Green Papers: Connecticut 2026 General Election", GREEN)

def cand(**kw):
    kw.setdefault("state", "CT")
    kw.setdefault("photo", None)
    kw.setdefault("photoSource", None)
    kw.setdefault("topics", {})
    kw.setdefault("accessed", ACCESSED)
    return kw

C = []

# ---------------- GOVERNOR ----------------
C.append(cand(
    id="ct-gov-lamont", name="Ned Lamont", party="D", ticket="Democratic; Working Families",
    office="Governor", website="https://www.nedlamont.com", reviewed="pri",
    photo="https://www.nedlamont.com/Share-2.jpg", photoSource="https://www.nedlamont.com",
    sources=[BALLOT,
        src("pri", "Ned Lamont for Governor: Priorities", "https://www.nedlamont.com/priorities"),
        src("abt", "Ned Lamont for Governor: About", "https://www.nedlamont.com/about")],
    overview=[
        [T("Ned Lamont, the incumbent governor, was first elected in 2018 and is on the November ballot as the nominee of the Democratic and Working Families parties.", "ballot")],
        [T("His campaign website says Connecticut has a governor who "), Q("began his career as a business owner and job creator", "abt"), T(", and that as governor he has delivered "), Q("the largest income-tax cut in history for middle-income families", "abt"), T(".")],
        [T("The site describes Connecticut as "), Q("a firewall for protecting our values", "pri"), T(".")],
    ],
    topics={
        "abortion": [[T("His priorities page lists "), Q("Protect reproductive freedom and abortion access", "pri"), T(" among its healthcare goals, and lists "), Q("Abortion and reproductive freedom", "pri"), T(" among areas where he says he has signed protective legislation.")]],
        "lgbtq": [[T("The site lists "), Q("LGBTQ rights and protections", "pri"), T(" among the areas where he says he has signed protective legislation.")]],
        "taxes": [[T("His about page cites "), Q("the largest income-tax cut in history for middle-income families", "abt"), T(" as a result of his time in office.")],
                  [T("The site says its healthcare plan would "), Q("Strengthen Connecticut’s healthcare system without raising taxes on residents or small businesses", "pri"), T(".")]],
        "healthcare": [[T("The site lists goals including "), Q("Lower prescription drug costs", "pri"), T(" and "), Q("Expand access to high-quality healthcare coverage with the CT Option", "pri"), T(".")],
                       [T("It describes a “Fair Share Healthcare Initiative” that would require employers with more than 100 employees, and nonprofits with more than 1,000, whose workers are enrolled in HUSKY (Medicaid) to contribute up to $1,000 per employee.", "pri")]],
        "immigration": [[T("The site lists "), Q("Immigrant and civil rights protections", "pri"), T(" among the areas where he says he has signed protective legislation.")]],
        "economy": [[T("The site says his agenda is "), Q("lowering costs and making life more affordable for working families", "pri"), T(", naming childcare, healthcare, housing and education.", "pri")],
                    [T("Listed housing goals include "), Q("Reducing housing costs by increasing housing supply responsibly", "pri"), T(".")]],
        "climate": [[T("The site states a goal to "), Q("Achieve a 100% zero-carbon grid by 2040 and net-zero emissions by 2050 targets", "pri"), T(".")],
                    [T("It also lists a goal of "), Q("Permanently preserving 21% of Connecticut as open space", "pri"), T(", and a utility plan that would "), Q("Require affordability to be considered when determining utility profits", "pri"), T(".")]],
        "guns": [[T("The site lists "), Q("Gun violence prevention measures", "pri"), T(" among the areas where he says he has signed protective legislation.")]],
        "education": [[T("Listed education goals include "), Q("Implementing universal pre-K and expanding affordable childcare", "pri"), T(", "), Q("Continuing to deliver universal free school meals", "pri"), T(", and "), Q("Increasing state support for special education", "pri"), T(".")]],
    }))

C.append(cand(
    id="ct-gov-fazio", name="Ryan Fazio", party="R", ticket="Republican; Independent Party of Connecticut",
    office="Governor", website="https://ryanfazio.com", reviewed="iss",
    photo="https://ryanfazio.com/wp-content/uploads/2023/04/Fazio-Portrait-Centered.jpeg", photoSource="https://ryanfazio.com/meet-ryan/",
    sources=[BALLOT,
        src("iss", "Ryan Fazio for Governor: Issues", "https://ryanfazio.com/issues/"),
        src("meet", "Ryan Fazio for Governor: Meet Ryan", "https://ryanfazio.com/meet-ryan/"),
        src("tax", "Ryan Fazio for Governor: Tax cut plan", "https://ryanfazio.com/the-fazio-tax-cut-plan/"),
        src("edu", "Ryan Fazio for Governor: Education plan", "https://ryanfazio.com/leadership-on-education-funding-access/")],
    overview=[
        [T("Ryan Fazio is a state senator and the nominee of the Republican and Independent parties for Governor.", "ballot")],
        [T("His campaign website says that in the State Senate he has "), Q("fought relentlessly to make Connecticut more affordable", "meet"), T(", and lists among his distinctions "), Q("A lifetime perfect score from the CT Business and Industry Association", "meet"), T(".")],
    ],
    topics={
        "taxes": [[T("His issues page says his plan would "), Q("reduce state income-tax rates, providing more than $2.5 billion in annual tax relief when fully implemented", "iss"), T(".")],
                  [T("It also says his plan would "), Q("lower income taxes for every Connecticut family by $1,500 and implement property tax caps", "iss"), T(".")],
                  [T("His tax plan page is headlined "), Q("Fazio Announces Largest Middle-Class Tax Cut in Connecticut History", "tax"), T(".")]],
        "economy": [[T("On housing, the site describes a plan that "), Q("reduces the cost of housing, allows Connecticut to grow its housing supply, and protects local control of zoning and decision-making", "iss"), T(".")]],
        "climate": [[T("On energy costs, the site says he has a plan to "), Q("cut electricity bills by 20%", "iss"), T(" by "), Q("ending hidden taxes, expanding reliable supply, and removing the mandates driving up costs", "iss"), T(".")],
                    [T("It says he would end a state tax break for large data centers.", "iss")]],
        "education": [[T("The site says "), Q("our reading achievement has fallen and our math achievement is barely above average", "iss"), T(".")],
                      [T("His education plan lists "), Q("High standards for literacy education: Every Connecticut student should be able to read by 3rd grade", "edu"), T(" and "), Q("No smartphones in classrooms", "edu"), T(".")]],
        "safety": [[T("The site says his plan "), Q("reforms the 2020 anti-police legislation, closes parole loopholes for violent offenders, and reinstates proactive policing", "iss"), T(".")]],
        "veterans": [[T("The site says he would "), Q("streamline veteran services, reduce costs, cut fees, recognize out-of-state licenses", "iss"), T(".")]],
    }))

# ---------------- CT-1 ----------------
C.append(cand(
    id="ct-01-bronin", name="Luke Bronin", party="D", ticket="Democratic",
    office="U.S. House", district="1", website="https://www.broninforcongress.com", reviewed="iss",
    photo="https://run.imgix.net/14d84d79-60f4-48a6-8537-8ed9721f92d3/fdabd80e-4f26-43c9-baf1-0ee61eb3f032/fdabd80e-4f26-43c9-baf1-0ee61eb3f032.jpg?ixlib=js-3.8.0&bri=0&con=0&sat=0&high=0&shad=0&usm=0&rect=2277%2C5%2C4052%2C4475&auto=compress%2Cformat&fit=fillmax&w=2048&q=75",
    photoSource="https://www.broninforcongress.com/about",
    sources=[BALLOT,
        src("iss", "Luke Bronin for Congress: Issues", "https://www.broninforcongress.com/issues"),
        src("abt", "Luke Bronin for Congress: About", "https://www.broninforcongress.com/about")],
    overview=[
        [T("Luke Bronin is the Democratic nominee in the 1st Congressional District, an open seat because incumbent Rep. John Larson lost his primary.", "ballot")],
        [T("His campaign website says "), Q("From 2016 to 2024, Luke served as the mayor of Hartford", "abt"), T(", and that he "), Q("served as a Navy intelligence officer and deployed to Afghanistan", "abt"), T(".")],
    ],
    topics={
        "abortion": [[Q("Reproductive freedom is a basic human right. Congress must pass federal protections for abortion access nationwide.", "iss")]],
        "lgbtq": [[Q("Every person deserves to live freely, safely, and with dignity, no matter who they love or how they identify.", "iss")]],
        "taxes": [[Q("We need a tax system that is progressive, fair, simple, and enforced.", "iss"), T(" His site says that means "), Q("ensuring the wealthiest Americans and biggest corporations actually pay their fair share", "iss"), T(".")]],
        "healthcare": [[T("The site says "), Q("We need to protect and strengthen Medicare and Medicaid, negotiate down the price of prescription drugs, and push for universal, affordable healthcare.", "iss")]],
        "immigration": [[T("The site says he has "), Q("outlined a plan to stop ICE’s lawlessness in the short term while working to abolish ICE from the ground up in the longer term", "iss"), T(".")]],
        "economy": [[T("The site says "), Q("High costs are crushing almost everyone but the wealthiest Americans", "iss"), T(", and that he would "), Q("focus relentlessly to make life easier and more affordable", "iss"), T(".")]],
        "climate": [[T("The site says "), Q("Climate change isn’t some distant future threat. It’s now.", "iss")]],
        "guns": [[T("The site says he would fight for "), Q("universal background checks, an assault weapons ban, safe storage laws, red-flag laws", "iss"), T(", among other measures.")]],
        "education": [[T("The site says he would "), Q("expand support to quality classroom education across the country, from early childhood education all the way through to affordable pathways to college or skilled trades", "iss"), T(".")]],
    }))

C.append(cand(
    id="ct-01-chai", name="Amy Fogelstrom Chai", party="R", ticket="Republican",
    office="U.S. House", district="1", website="https://chaiforcongress.com", reviewed="iss",
    photo="https://chaiforcongress.com/_next/image?url=https%3A%2F%2Fhebbkx1anhila5yf.public.blob.vercel-storage.com%2FCHAI-2026%2520copy-b49HtidJodp8sHrsgmMxeLcQx4Aebf.webp&w=1200&q=75",
    photoSource="https://chaiforcongress.com/about",
    sources=[BALLOT,
        src("iss", "Chai for Congress: Issues", "https://chaiforcongress.com/issues"),
        src("abt", "Chai for Congress: About Amy", "https://chaiforcongress.com/about")],
    overview=[
        [T("Amy Fogelstrom Chai is the Republican nominee in the 1st Congressional District.", "ballot")],
        [T("Her campaign website says "), Q("Doc Chai, MD, MS, is an expert in Primary Care and Addiction Medicine", "abt"), T(", and describes her as "), Q("a proven leader and a rational actor", "abt"), T(".")],
    ],
    topics={
        "lgbtq": [[T("In a passage on education, her site says "), Q("The current leadership seems more interested in making sure children get confused about their gender and exposed to pornography than they are interested in students learning reading and math.", "iss")]],
        "taxes": [[Q("Property taxes must be capped.", "iss"), T(" The site also says "), Q("More tax on financial industry and less tax on earned income will help to offset this harsh imbalance", "iss"), T(" and "), Q("The self-employment tax (FICA at 15%) must be eliminated if fairness is to be restored.", "iss")]],
        "defense": [[T("The site says "), Q("I believe in a strong defense force, and would prefer not to deploy it.", "iss")]],
        "healthcare": [[Q("Health care should not cost as much as it currently does.", "iss"), T(" The site also says "), Q("I want to support you on a prevention journey", "iss"), T(".")]],
        "immigration": [[Q("I believe in secure borders.", "iss")]],
        "economy": [[Q("We must support local economies, small businesses, and American industry.", "iss")]],
        "education": [[Q("Parents should know exactly what is being taught, and it should be reading, writing, and math.", "iss"), T(" The site also says "), Q("Parents have every right to determine what their children are learning, whether it be through public schools or home education.", "iss")]],
    }))

C.append(cand(
    id="ct-01-sanders", name="Mary L. Sanders", party="G", ticket="Green",
    office="U.S. House", district="1", website=None, reviewed=None,
    sources=[BALLOT],
    overview=[[T("Mary L. Sanders is the Green Party candidate in the 1st Congressional District.", "ballot")]],
    noInfo=True))

# ---------------- CT-2 ----------------
C.append(cand(
    id="ct-02-courtney", name="Joe Courtney", party="D", ticket="Democratic",
    office="U.S. House", district="2", website="https://courtney.house.gov", reviewed="bio",
    photo="https://courtney.house.gov/sites/evo-subsites/courtney-evo.house.gov/files/evo-media-image/jdc-photo.png",
    photoSource="https://courtney.house.gov/",
    siteNote="His campaign domain was not in use when reviewed, so this profile cites his official congressional website.",
    sources=[BALLOT,
        src("bio", "Rep. Joe Courtney (official site): Biography", "https://courtney.house.gov/about/full-biography"),
        src("op", "Rep. Joe Courtney (official site): Op-Ed, October 9, 2026", "https://courtney.house.gov/media-center/press-releases/op-ed-health-care-premiums-continue-rise-congress-can-lower-them")],
    overview=[
        [T("Joe Courtney, the incumbent, is the Democratic nominee in the 2nd Congressional District.", "ballot")],
        [T("His official biography says he "), Q("was elected in 2006 to represent the Second Congressional District of Connecticut", "bio"), T(" and is "), Q("Ranking Member of the House Armed Services Subcommittee on Seapower and Projection Forces", "bio"), T(".")],
    ],
    topics={
        "defense": [[T("His biography says he has "), Q("worked to strengthen our nation's defense by leading the call for increased submarine production", "bio"), T(".")]],
        "healthcare": [[T("In an October 9, 2026 op-ed he wrote "), Q("I am a co-sponsor of the Lowering Drug Costs for American Families Act (H.R. 6166)", "op"), T(", and that "), Q("Congress should pass the Lowering Drug Costs for American Families Act into law", "op"), T(".")]],
        "climate": [[T("His biography says he "), Q("introduced and won passage of a law that designated the Eightmile River in Connecticut as a part of the National Wild and Scenic Rivers System", "bio"), T(".")]],
        "veterans": [[T("His biography says he has "), Q("distinguished himself as a tireless advocate for both our nation's veterans and our men and women in uniform", "bio"), T(".")]],
    }))

C.append(cand(
    id="ct-02-austin", name="George Austin", party="R", ticket="Republican; Independent Party of Connecticut",
    office="U.S. House", district="2", website="https://votegeorgeforcongress.com", reviewed="meet",
    photo="https://votegeorgeforcongress.com/wp-content/uploads/2026/04/George-portrait-header-home.jpg",
    photoSource="https://votegeorgeforcongress.com/",
    sources=[BALLOT,
        src("meet", "Vote George for Congress: Meet George", "https://votegeorgeforcongress.com/meet-george/"),
        src("dol", "Vote George for Congress: Dollars & Sense", "https://votegeorgeforcongress.com/dollars-and-sense/"),
        src("opp", "Vote George for Congress: Building Opportunity", "https://votegeorgeforcongress.com/building-opportunity/")],
    overview=[
        [T("George Austin is the nominee of the Republican and Independent parties in the 2nd Congressional District.", "ballot")],
        [T("His campaign website says "), Q("I’m not a politician—I’m one of you, an everyday working man", "meet"), T(", and that he "), Q("earned a degree in Construction Management, and built a life as a small business owner", "meet"), T(".")],
    ],
    topics={
        "taxes": [[T("The site lists plans to "), Q("Deliver tax relief to keep more money in your pocket", "dol"), T(" and "), Q("Support term limits to end career politicians putting themselves ahead of the people", "dol"), T(".")]],
        "defense": [[T("The site says "), Q("Defense manufacturers like Electric Boat in eastern Connecticut and Pratt & Whitney are the backbone of our local economy", "opp"), T(", and links their workforce shortages to national security.", "opp")]],
        "economy": [[T("The site lists plans to "), Q("Secure federal investments to strengthen infrastructure, stabilize housing, and grow good-paying jobs", "dol"), T(".")]],
        "climate": [[T("The site lists a plan to "), Q("Push for energy policies that lower utility bills", "dol"), T(", and says "), Q("I refuse to bow to extreme green ideology that relies on shame, propaganda, and fear instead of real solutions", "dol"), T(".")]],
        "guns": [[T("His site lists him as a member of "), Q("both CCDL and the NRA", "meet"), T(". The site does not set out a gun policy.", "meet")]],
        "education": [[T("The site says "), Q("We need to restore respect for trade education by reintroducing classes like wood & metal shop into high schools", "opp"), T(", and that he would "), Q("direct federal funds toward apprenticeships, job training, and technical education", "opp"), T(".")]],
    }))

# ---------------- CT-3 ----------------
C.append(cand(
    id="ct-03-delauro", name="Rosa DeLauro", party="D", ticket="Democratic",
    office="U.S. House", district="3", website="https://rosadelauro.com", reviewed="abt",
    photo="https://rosadelauro.com/wp-content/uploads/2025/08/b3-1.jpg", photoSource="https://rosadelauro.com/about/",
    sources=[BALLOT,
        src("abt", "Rosa DeLauro for Congress: About", "https://rosadelauro.com/about/"),
        src("hc", "Rosa DeLauro for Congress: Health Care", "https://rosadelauro.com/issue/health-care/"),
        src("col", "Rosa DeLauro for Congress: The Cost of Living", "https://rosadelauro.com/issue/the-cost-of-living/"),
        src("imm", "Rosa DeLauro for Congress: Immigration", "https://rosadelauro.com/issue/immigration/"),
        src("gv", "Rosa DeLauro for Congress: Gun Violence Prevention", "https://rosadelauro.com/issue/gun-violence-prevention/"),
        src("clim", "Rosa DeLauro for Congress: Climate Crisis", "https://rosadelauro.com/issue/climate-crisis/"),
        src("edu", "Rosa DeLauro for Congress: Education", "https://rosadelauro.com/issue/education/")],
    overview=[
        [T("Rosa DeLauro, the incumbent, is the Democratic nominee in the 3rd Congressional District.", "ballot")],
        [T("Her campaign website says she has been "), Q("Representing Connecticut’s 3rd Congressional District since 1991", "abt"), T(" and is the Ranking Member of the House Appropriations Committee.", "abt")],
    ],
    topics={
        "abortion": [[Q("a woman’s healthcare decisions belong to her, her family, and her doctor—full stop", "hc"), T(". The site also says "), Q("I am leading the effort to codify the protections of Roe v. Wade into federal law", "hc"), T(".")]],
        "taxes": [[T("The site says she will "), Q("always oppose tax cuts for billionaires so we can invest in our communities", "col"), T(", and lists a goal to "), Q("Ensure the wealthy and corporations pay their fair share", "col"), T(".")],
                  [T("She says she led "), Q("the charge for the expanded Child Tax Credit", "col"), T(" and is working to make it permanent.", "col")]],
        "healthcare": [[Q("Everyone should have affordable healthcare.", "hc"), T(" The site credits the Inflation Reduction Act, which she says she championed, with letting Medicare ", "hc"), Q("negotiate lower drug prices", "hc"), T(".")]],
        "immigration": [[T("The site says "), Q("We can—and must—strengthen border security and manage immigration in a way that upholds the legal values that define our nation.", "imm")]],
        "economy": [[T("The site says "), Q("our economy is strongest when it is built from the middle out, not the top down", "col"), T(".")]],
        "climate": [[T("Among her listed goals are to "), Q("Replace diesel school buses with clean electric fleets", "clim"), T(" and "), Q("Weatherize older homes to cut both energy costs and pollution for working families", "clim"), T(".")]],
        "guns": [[T("The site calls gun violence "), Q("a public health crisis that demands urgent, commonsense action", "gv"), T(", and says she "), Q("authored and introduced Ethan’s Law", "gv"), T(", which it says "), Q("establishes federal requirements for safe gun storage", "gv"), T(".")]],
        "education": [[T("The site lists results including "), Q("A historic increase in funding for students with disabilities and for schools serving a high number of low-income families through Title I grants", "edu"), T(".")]],
    }))

C.append(cand(
    id="ct-03-lancia", name="Chris Lancia", party="R", ticket="Republican",
    office="U.S. House", district="3", website="https://lanciaforcongress2026.org", reviewed="home",
    sources=[BALLOT, src("home", "Lancia for Congress 2026", "https://lanciaforcongress2026.org/")],
    overview=[
        [T("Christopher “Chris” Lancia is the Republican nominee in the 3rd Congressional District.", "ballot")],
        [T("His campaign website says he is "), Q("a proud veteran of the United States Coast Guard", "home"), T(" who "), Q("became a Federal Law Enforcement Officer", "home"), T(".")],
    ],
    topics={
        "lgbtq": [[T("His site says "), Q("biological men should not compete in women’s sports", "home"), T(".")]],
        "taxes": [[Q("I’ll fight for lower taxes, a balanced budget", "home"), T(" is how his site describes his approach.")]],
        "defense": [[T("His site says "), Q("I believe in putting America First", "home"), T(".")]],
        "immigration": [[T("His site says "), Q("border security is national security", "home"), T(".")]],
        "economy": [[T("The site lists a priority to "), Q("Fight inflation, lower taxes, and hold Washington accountable for reckless spending", "home"), T(".")]],
        "guns": [[Q("I will always stand up for the Second Amendment", "home"), T(" is how his site puts it.")]],
        "education": [[T("The site says "), Q("Parents—not bureaucrats—should make decisions for their children", "home"), T(".")]],
        "safety": [[T("The site says he will "), Q("support our law enforcement", "home"), T(".")]],
    }))

C.append(cand(
    id="ct-03-egan", name="Tom Egan", party="I", ticket="Independent Party of Connecticut",
    office="U.S. House", district="3", website=None, reviewed=None,
    sources=[BALLOT],
    overview=[[T("Thomas “Tom” Egan is the Independent Party of Connecticut candidate in the 3rd Congressional District.", "ballot")]],
    noInfo=True))

# ---------------- CT-4 ----------------
C.append(cand(
    id="ct-04-himes", name="Jim Himes", party="D", ticket="Democratic",
    office="U.S. House", district="4", website="https://www.himesforcongress.com", reviewed="pri",
    photo="https://www.himesforcongress.com/wp-content/uploads/2023/07/video-thumb.jpg", photoSource="https://www.himesforcongress.com/",
    sources=[BALLOT,
        src("abt", "Jim Himes for Congress: Meet Jim", "https://www.himesforcongress.com/about/"),
        src("pri", "Jim Himes for Congress: Priorities", "https://www.himesforcongress.com/priorities/"),
        src("lgbt", "Jim Himes for Congress: LGBTQ Rights", "https://www.himesforcongress.com/priorities/lgbtq-rights/"),
        src("hc", "Jim Himes for Congress: Healthcare & Social Security", "https://www.himesforcongress.com/priorities/healthcare-social-security/"),
        src("nat", "Jim Himes for Congress: National Security", "https://www.himesforcongress.com/priorities/national-security/"),
        src("eco", "Jim Himes for Congress: Economy & Jobs", "https://www.himesforcongress.com/priorities/economy-jobs/"),
        src("env", "Jim Himes for Congress: Energy & Environment", "https://www.himesforcongress.com/priorities/energy-environment/"),
        src("edu", "Jim Himes for Congress: Education", "https://www.himesforcongress.com/priorities/education/")],
    overview=[
        [T("Jim Himes, the incumbent, is the Democratic nominee in the 4th Congressional District.", "ballot")],
        [T("His campaign website says "), Q("Since his election to Congress in 2008", "abt"), T(" he has served as "), Q("Ranking Member of the House Permanent Select Committee on Intelligence", "abt"), T(".")],
    ],
    topics={
        "abortion": [[T("His priorities page says "), Q("Jim stood against Republican attempts to defund family planning, and he opposed multiple efforts to ban abortion at the federal level", "pri"), T(".")]],
        "lgbtq": [[T("His site says he "), Q("co-sponsored and helped pass the Equality Act in the House", "lgbt"), T(" and "), Q("won’t stop fighting until it is signed into law", "lgbt"), T(".")]],
        "healthcare": [[T("The site says he works to "), Q("prioritize access to quality, affordable healthcare for all Americans", "hc"), T(", and that he is "), Q("proud to stand against any efforts to privatize Social Security", "hc"), T(".")]],
        "defense": [[T("The site says he is "), Q("dedicated to upholding the legacy of skilled, active global leadership", "nat"), T(", and that he "), Q("passed the USA FREEDOM Act which ended bulk collection programs", "nat"), T(" as part of a bipartisan coalition.", "nat")]],
        "economy": [[T("The site cites his work on "), Q("raising the minimum wage to $15 nationwide", "eco"), T(" and his role in "), Q("writing the Dodd-Frank Act", "eco"), T(".")]],
        "climate": [[T("The site says "), Q("Jim introduced the National Green Bank Act", "env"), T(".")]],
        "guns": [[T("His gun safety page opens by saying "), Q("Every day, 100 Americans are killed by guns and hundreds more are injured.", "pri")]],
        "education": [[T("The site says he is "), Q("pushing for legislation that gives states and local districts more flexibility without losing accountability", "edu"), T(".")]],
    }))

C.append(cand(
    id="ct-04-goldstein", name="Michael Goldstein", party="R", ticket="Republican",
    office="U.S. House", district="4", website="https://goldsteinforcongress.com", reviewed="home",
    sources=[BALLOT, src("home", "Goldstein for Congress", "https://goldsteinforcongress.com/")],
    overview=[
        [T("Dr. Michael Ted Goldstein is the Republican nominee in the 4th Congressional District.", "ballot")],
        [T("His campaign website describes him as "), Q("Doctor. Lawyer. Father. Fighter.", "home"), T(" and says he was "), Q("President of New York County Medical Society — twice", "home"), T(".")],
    ],
    topics={
        "lgbtq": [[T("His policy platform lists "), Q("Ban gender-affirming surgery until adulthood", "home"), T(" under healthcare and "), Q("Defend equality for all", "home"), T(" under constitutional rights.", "home")]],
        "taxes": [[T("His economic platform lists "), Q("Keep taxes low", "home"), T(" and "), Q("Reduce regulatory burdens on small businesses", "home"), T(".")]],
        "healthcare": [[T("The site says "), Q("The cure for high healthcare costs isn't more government. It's less.", "home")]],
        "immigration": [[T("His platform lists "), Q("Close border to illegal aliens and drugs", "home"), T(".")]],
        "climate": [[T("His platform lists "), Q("Increase CT's natural gas and nuclear power supply", "home"), T(", and he says he will "), Q("fight to unblock pipeline capacity", "home"), T(".")]],
        "guns": [[T("His platform lists "), Q("Support religious exemption and 2nd Amendment", "home"), T(".")]],
        "education": [[T("His platform lists "), Q("Promote school choice", "home"), T(" and "), Q("Expand vocational training", "home"), T(".")]],
    }))

C.append(cand(
    id="ct-04-wesley", name="Ben Wesley", party="I", ticket="Independent Party of Connecticut",
    office="U.S. House", district="4", website=None, reviewed=None,
    sources=[BALLOT],
    overview=[[T("Benjamin “Ben” Wesley is the Independent Party of Connecticut candidate in the 4th Congressional District.", "ballot")]],
    noInfo=True))

# ---------------- CT-5 ----------------
C.append(cand(
    id="ct-05-hayes", name="Jahana Hayes", party="D", ticket="Democratic",
    office="U.S. House", district="5", website="https://jahanahayes.com", reviewed="iss",
    photo="https://hayes.house.gov/index.cfm?a=Files.Serve&File_id=A47D77B3-85C8-4C24-B5BB-509263F3B499", photoSource="https://hayes.house.gov/about",
    sources=[BALLOT,
        src("abt", "Jahana Hayes for Congress: Meet Jahana", "https://jahanahayes.com/about/"),
        src("iss", "Jahana Hayes for Congress: Issues", "https://jahanahayes.com/issues/"),
        src("rep", "Jahana Hayes for Congress: Reproductive Rights", "https://jahanahayes.com/issues/protecting-the-right-to-choose/"),
        src("lgbt", "Jahana Hayes for Congress: LGBTQ+ Rights", "https://jahanahayes.com/issues/lbgtq-rights/"),
        src("hc", "Jahana Hayes for Congress: Healthcare", "https://jahanahayes.com/issues/health-care/"),
        src("imm", "Jahana Hayes for Congress: Immigration", "https://jahanahayes.com/issues/immigration/"),
        src("gun", "Jahana Hayes for Congress: Gun Violence", "https://jahanahayes.com/issues/gun-violence/"),
        src("eco", "Jahana Hayes for Congress: Economy", "https://jahanahayes.com/issues/economy/"),
        src("edu", "Jahana Hayes for Congress: Education", "https://jahanahayes.com/issues/education/"),
        src("env", "Jahana Hayes for Congress: Environment", "https://jahanahayes.com/issues/environment/")],
    overview=[
        [T("Jahana Hayes, the incumbent, is the Democratic nominee in the 5th Congressional District.", "ballot")],
        [T("Her campaign website says she was "), Q("named National Teacher of the Year in 2016", "abt"), T(" before being elected to Congress in 2018.", "abt")],
    ],
    topics={
        "abortion": [[T("Her site says she "), Q("remains committed to codifying a woman’s right to choose", "rep"), T(".")]],
        "lgbtq": [[T("Her site says LGBTQ+ people "), Q("should have equal protection under the law", "lgbt"), T(" and that she supports "), Q("the Equality Act", "lgbt"), T(".")]],
        "healthcare": [[T("Her site says she is "), Q("supporting Medicare for All", "hc"), T(" and has "), Q("worked to curb surprise billing, cap prescription drug costs", "hc"), T(".")]],
        "immigration": [[T("Her site says "), Q("it is important to maintain strong borders and protect national security", "imm"), T(", and that "), Q("it is also imperative that all people in this country are treated with dignity and constitutional rights are protected", "imm"), T(". It says she supports a "), Q("path to citizenship for Dreamers", "imm"), T(".")]],
        "economy": [[T("The site says "), Q("we need an economy that works for all people, not just the ultra-wealthy", "eco"), T(".")]],
        "climate": [[T("The site says she "), Q("led legislation to support zero-emission school buses", "env"), T(" and "), Q("supported research on renewable energy sources", "env"), T(".")]],
        "guns": [[T("The site cites "), Q("advocating for red flag laws, expanded background checks, gun buyback programs, and raising the age to purchase an automatic weapon", "gun"), T(".")]],
        "education": [[T("The site says she supports "), Q("fully funding the Individuals with Disabilities Education Act", "edu"), T(".")]],
    }))

C.append(cand(
    id="ct-05-shea", name="Chris Shea", party="R", ticket="Republican",
    office="U.S. House", district="5", website="https://chrissheaforcongress.com", reviewed="iss",
    photo="https://chrissheaforcongress.com/wp-content/uploads/lt-shea-north-haven-fire-dept-3.webp", photoSource="https://chrissheaforcongress.com/",
    sources=[BALLOT,
        src("iss", "Chris Shea for Congress: Issues", "https://chrissheaforcongress.com/issues/"),
        src("ctm", "CT Mirror: CT’s GOP says it can win the 5th Congressional District race (Aug. 14, 2026)", "https://ctmirror.org/2026/08/14/cts-gop-says-it-can-win-the-5th-congressional-district-race/")],
    overview=[
        [T("Chris Shea is the Republican nominee in the 5th Congressional District.", "ballot")],
        [T("His campaign website says he has served "), Q("as a Navy SEAL, Pentagon leader, firefighter, paramedic, and advocate for veterans and first responders", "iss"), T(".")],
    ],
    topics={
        "lgbtq": [[T("CT Mirror reported that Shea has raised transgender people’s participation in sports as part of his platform.", "ctm")]],
        "taxes": [[T("The site says he will fight for policies that "), Q("lower energy costs, reduce the tax burden, and promote practical housing solutions", "iss"), T(".")]],
        "defense": [[T("The site says he "), Q("believes peace is secured through strength, not weakness", "iss"), T(" and that "), Q("America should stand with our ally Israel and support its right to self-defense", "iss"), T(".")]],
        "immigration": [[T("The site says he will "), Q("secure the border, enforce our immigration laws, and stop the flow of fentanyl and other deadly drugs into our neighborhoods", "iss"), T(".")]],
        "economy": [[T("The site says "), Q("Connecticut families are being squeezed from every direction by high electricity bills, heavy taxes, and rising housing costs", "iss"), T(".")]],
        "veterans": [[T("The site says he will "), Q("improve access to the VA, cut through bureaucratic delays", "iss"), T(".")]],
        "safety": [[T("The site says he will "), Q("fund border patrol, support law enforcement", "iss"), T(".")]],
    }))


import extra_candidates
C.extend(extra_candidates.build(T, Q, src, cand))

# ---------------- photo captions ----------------
# year, basis ("taken" = year in the image file's own metadata; "posted" = year in the image's upload path/name)
PHOTO = {
    "ct-gov-lamont": (None, None), "ct-gov-fazio": ("2023", "posted"), "ct-01-bronin": (None, None),
    "ct-01-chai": ("2026", "posted"), "ct-02-courtney": ("2023", "taken"), "ct-02-austin": ("2026", "posted"),
    "ct-03-delauro": ("2025", "posted"), "ct-04-himes": ("2023", "posted"), "ct-05-hayes": ("2018", "taken"),
    "ct-05-shea": ("2026", "posted"), "ct-04-goldstein": (None, None),
}
BYID = {c["id"]: c for c in C}
for cid, (yr, basis) in PHOTO.items():
    BYID[cid]["photoYear"], BYID[cid]["photoBasis"] = yr, basis
g = BYID["ct-04-goldstein"]
g["photo"] = "assets/photos/goldstein-instagram.jpg"
g["photoSource"] = "https://www.instagram.com/drmichaelgoldstein/"
g["photoKind"] = "his public Instagram profile"
g["photoLowRes"] = True

# ---------------- past-five-year statements (topics missing from a candidate's website) ----------------
def add_src(cid, key, title, url):
    BYID[cid]["sources"].append(src(key, title, url))

def said(cid, topic, when, context, *segs):
    """A dated statement from outside the candidate's website. segs are T()/Q() segments."""
    t = BYID[cid]["topics"]
    if isinstance(t.get(topic), list):  # topic also has website text
        t[topic] = {"gap": False, "paras": t[topic], "said": []}
    t.setdefault(topic, {"gap": True, "said": []})
    t[topic]["said"].append({"when": when, "context": context, "seg": list(segs)})

CTM = "CT Mirror"
# --- Fazio
cid = "ct-gov-fazio"
add_src(cid, "m24", "CT Mirror: In Greenwich, a state Senate race to define ‘extreme’ (Sept. 22, 2024)", "https://ctmirror.org/2024/09/22/ct-ryan-fazio-greenwich-2024-election/")
add_src(cid, "ad", "CT Mirror: Lamont’s first general-election ad targets Fazio on ICE (Sept. 9, 2026)", "https://ctmirror.org/2026/09/09/lamont-election-ad-fazio-ice-trump/")
add_src(cid, "ep", "CT Mirror: In an election year, CT’s electricity prices are falling (Sept. 17, 2026)", "https://ctmirror.org/2026/09/17/cts-electricity-prices-are-falling/")
add_src(cid, "aca", "CT Mirror: Lamont pledges to extend ACA subsidies. His opponents are split (July 23, 2026)", "https://ctmirror.org/2026/07/23/ned-lamont-ct-affordable-care-act-subsidies/")
add_src(cid, "sig", "CT Senate Republicans: Sen. Fazio, Greenwich Elected Officials Speak Out Against Homophobic, Transphobic Signs (June 6, 2023)", "https://www.ctsenaterepublicans.com/2023/06/sen-fazio-greenwich-elected-officials-speak-out-against-homophobic-transphobic-signs/")
said(cid, "abortion", "2024-09-22", "CT Mirror profile of his 2024 state Senate race in Greenwich. His Democratic opponent had cited Fazio’s votes on guns and abortion; Fazio responded that Democrats were using them as wedge issues.",
     Q("Easing gun laws in Connecticut or restricting abortion in Connecticut is never -- is not -- going to happen. And Republicans in the legislature are not in favor of it, and Democrats in the legislature are not in favor of it", "m24"))
said(cid, "guns", "2024-09-22", "Same CT Mirror profile; the article says Fazio voted in 2023 against a bill updating Connecticut’s gun law and that he said he objected to one section of it.",
     Q("Easing gun laws in Connecticut or restricting abortion in Connecticut is never -- is not -- going to happen.", "m24"))
said(cid, "immigration", "2026-09-09", "Reacting to Gov. Lamont’s first general-election ad, which criticized Fazio’s opposition to a 2026 bill limiting ICE arrests in schools and places of worship.",
     Q("I think that the governor was wrong and radical in tying the hands of state and federal law enforcement in communicating with federal authorities in the case of people who are here illegally, who have been convicted of Class C, D and E felonies like manslaughter and sexual abuse", "ad"))
said(cid, "defense", "2026-09-17", "CT Mirror article on electricity and energy prices, discussing how the war in Iran has affected oil and gas costs.",
     Q("The governor of Connecticut doesn’t have any constitutional responsibilities or input on issues of war and peace", "ep"), T(" and "), Q("I always am rooting for a just and lasting peace", "ep"), T("."))
said(cid, "healthcare", "2026-07-23", "CT Mirror article on whether Connecticut should use state funds to replace expired federal ACA subsidies; Fazio opposes doing so.",
     T("On using state money to offset the expired federal subsidies, he said it "), Q("is literally just taking from taxpayers and not solving problems", "aca"), T("."))
said(cid, "lgbtq", "2023-06-06", "Joint statement from Fazio and three Greenwich state representatives, issued under the headline “Speak Out Against Homophobic, Transphobic Signs.”",
     Q("We’re shocked and saddened by this despicable act.", "sig"))

# --- Lamont
cid = "ct-gov-lamont"
add_src(cid, "heat", "CT Mirror: Lamont to bolster heating assistance using CT contingency fund (Oct. 13, 2026)", "https://ctmirror.org/2026/10/13/lamont-to-bolster-heating-assistance-using-ct-contingency-fund/")
said(cid, "defense", "2026-10-13", "Press conference in New Haven on heating assistance, reported by CT Mirror.",
     T("CT Mirror reported that Lamont said families are paying the price for rising heating oil costs driven by the war in Iran, and that the state has to respond.", "heat"))

# --- Courtney
cid = "ct-02-courtney"
add_src(cid, "dobbs", "Rep. Courtney press release: Statement on Supreme Court Decision to Overturn Roe v. Wade (June 24, 2022)", "https://courtney.house.gov/media-center/press-releases/courtney-statement-supreme-court-decision-overturn-roe-v-wade")
add_src(cid, "rfma", "Rep. Courtney press release: Courtney Votes to Shield Americans’ Right to Same-Sex and Interracial Marriage (July 19, 2022)", "https://courtney.house.gov/media-center/press-releases/courtney-votes-shield-americans-right-same-sex-and-interracial-marriage")
add_src(cid, "awb", "Rep. Courtney press release: Courtney Votes to Reduce the Prevalence of Deadly Assault Weapons (July 29, 2022)", "https://courtney.house.gov/media-center/press-releases/courtney-votes-reduce-prevalence-deadly-assault-weapons-and-high")
add_src(cid, "dhs", "Rep. Courtney press release: Statement on House Passage of DHS Funding Bill (April 30, 2026)", "https://courtney.house.gov/media-center/press-releases/courtney-statement-house-passage-dhs-funding-bill")
add_src(cid, "mpi", "Rep. Courtney press release: Courtney, Perez Celebrate the Success of Eastern CT’s Manufacturing Pipeline Initiative (Sept. 22, 2026)", "https://courtney.house.gov/media-center/press-releases/courtney-perez-celebrate-success-eastern-cts-manufacturing-pipeline")
add_src(cid, "nurse", "Rep. Courtney press release: Courtney Slams McMahon’s “Insulting” Nursing Student Loan Caps (May 14, 2026)", "https://courtney.house.gov/media-center/press-releases/courtney-slams-mcmahons-insulting-nursing-student-loan-caps")
said(cid, "abortion", "2022-06-24", "Press statement issued the day the Supreme Court overturned Roe v. Wade.",
     Q("The decision released by the Supreme Court today overturning 50 years of settled law protecting the reproductive health decisions of women and families in the U.S. is a stunning step backwards for the privacy rights of all Americans", "dobbs"))
said(cid, "lgbtq", "2022-07-19", "Press release after the House passed the Respect for Marriage Act, which he voted for.",
     Q("As consenting adults, Americans have the right to love who they choose, and to marry who they love", "rfma"))
said(cid, "guns", "2022-07-29", "Press release after the House passed the Assault Weapons Ban Act of 2022 (217-213), which he voted for and co-sponsored.",
     Q("H.R. 1808 would restore the ban on military-style assault weapons that was formerly in place throughout our country during one of the most prosperous and low-crime points in American history.", "awb"))
said(cid, "immigration", "2026-04-30", "Press statement on House passage of a Department of Homeland Security funding bill that excluded ICE and CBP funding.",
     Q("For 76 days, critical DHS agencies that have nothing to do with the out of control lawless actions of ICE have taken the brunt of this shutdown.", "dhs"))
said(cid, "economy", "2026-09-22", "Press release marking ten years of the Manufacturing Pipeline Initiative in eastern Connecticut.",
     Q("we now need to double down on the Manufacturing Pipeline Initiative’s success for decades to come", "mpi"))
said(cid, "education", "2026-05-14", "Remarks to Education Secretary Linda McMahon, shared in a press release about a federal rule on nursing student-loan caps.",
     Q("Your own data in terms of analyzing this rulemaking process actually showed that for nurse anesthetists, at least 28% of them who are in education right now have costs that exceed the [student loan] caps.", "nurse"))

# --- DeLauro
cid = "ct-03-delauro"
add_src(cid, "rfma", "Rep. DeLauro press release: DeLauro Votes to Protect Same-Sex & Interracial Marriages (Dec. 8, 2022)", "https://delauro.house.gov/media-center/press-releases/delauro-votes-protect-same-sex-interracial-marriages")
add_src(cid, "ndaa", "Rep. DeLauro press release: DeLauro Votes “No” on President Trump’s Trillion-Dollar Defense Authorization Bill (July 22, 2026)", "https://delauro.house.gov/media-center/press-releases/delauro-votes-no-president-trumps-trillion-dollar-defense-authorization")
said(cid, "lgbtq", "2022-12-08", "Press release after a House vote to pass the Respect for Marriage Act.",
     Q("I applaud the Congress for moving on a bipartisan basis to protect same-sex marriages and interracial marriages under federal law.", "rfma"))
said(cid, "defense", "2026-07-22", "Press release explaining her “no” vote on the House defense authorization bill.",
     Q("Democrats were completely blocked from offering any substantive amendments focused on strengthening our industrial base, reforming procurement and acquisition processes, and supporting our allies around the world.", "ndaa"))

# --- Himes
cid = "ct-04-himes"
add_src(cid, "imm25", "CT Public: As political sands shift on immigration, some CT Congress members pivot (July 16, 2025)", "https://www.ctpublic.org/news/2025-07-16/trump-immigration-policy-ct-lawmakers")
said(cid, "immigration", "2025-07-16", "CT Public article on how Connecticut’s Democratic House members have responded to immigration measures; the first quote is from his statement on H.R. 875, the second about Trump administration actions.",
     Q("H.R. 875 would establish new grounds for deportation for non-citizens only after they’ve had their day in court and been convicted of a crime. I supported this legislation because it maintained clear procedural due process", "imm25"),
     T(". He also said actions such as masked ICE agents arresting international students "), Q("call into question the president’s commitment to faithfully executing laws as he is sworn to do", "imm25"), T("."))

# --- Hayes
cid = "ct-05-hayes"
add_src(cid, "ndaa", "Rep. Hayes statement on House passage of the FY2027 National Defense Authorization Act (July 23, 2026)", "https://hayes.house.gov/2026/7/hayes-statement-on-the-house-passage-of-the-national-defense-authorization-act-for-fiscal-year-2027")
add_src(cid, "iran", "Rep. Hayes statement on U.S. military action in Iran (Feb. 28, 2026)", "https://hayes.house.gov/2026/2/hayes-statement-on-u-s-military-action-in-iran")
said(cid, "defense", "2026-07-23", "Press statement explaining her vote against the FY2027 National Defense Authorization Act.",
     Q("Funneling over a trillion of taxpayer dollars in defense spending enables the President to move forward with his unconstitutional war and ultimately jeopardizes our military readiness.", "ndaa"))
said(cid, "defense", "2026-02-28", "Press statement after President Trump ordered a military operation inside Iran.",
     Q("Placing U.S. troops in immediate danger risks igniting a broader regional war in the Middle East and ultimately makes Americans less safe.", "iran"))

# --- Bronin
cid = "ct-01-bronin"
add_src(cid, "jns", "JNS: Former Hartford mayor beats AIPAC-endorsed congressman in Connecticut Dem primary (Aug. 2026)", "https://jns.org/news/u-s-news/former-hartford-mayor-beats-aipac-endorsed-congressman-seeking-15th-term-in-connecticut-dem-primary")
said(cid, "defense", "2026-08-11", "Jewish News Syndicate report on his primary win over Rep. John Larson (this is a paraphrase by the outlet, not a direct quote).",
     T("JNS reported that Bronin has said he would support Israel’s Iron Dome defensive system but opposes additional offensive weapons for Israel.", "jns"))

# --- Goldstein
cid = "ct-04-goldstein"
add_src(cid, "d24", "CT Mirror: U.S. Rep. Jim Himes, two challengers parry in 4th District debate (Oct. 29, 2024)", "https://ctmirror.org/2024/10/29/ct-4th-district-debate-jim-himes-michael-goldstein-benjamin-wesley/")
said(cid, "abortion", "2024-10-29", "CT Examiner–hosted debate with Rep. Jim Himes and Ben Wesley, asked about Congress’s role on abortion. CT Mirror reported he said it is up to each state and voters should be able to decide in a referendum.",
     Q("The decision has been made in Connecticut", "d24"))
said(cid, "defense", "2024-10-29", "Same debate, during an exchange about the Israel–Gaza war after an Oct. 2024 challenge from Ben Wesley; he also said he supports Israel’s right to defend itself.",
     Q("It happened once. It’s never going to happen again, so good luck with putting my people at risk of being exterminated", "d24"))

# --- Wesley (no website)
cid = "ct-04-wesley"
add_src(cid, "d24", "CT Mirror: U.S. Rep. Jim Himes, two challengers parry in 4th District debate (Oct. 29, 2024)", "https://ctmirror.org/2024/10/29/ct-4th-district-debate-jim-himes-michael-goldstein-benjamin-wesley/")
said(cid, "defense", "2024-10-29", "CT Examiner–hosted debate in Stamford with Rep. Jim Himes and Michael Goldstein (Wesley also ran as the Independent Party candidate in 2024).",
     Q("My opponents on the Democratic and Republican side will say the only way to solve the wars in Gaza and Lebanon or the Russian-Ukraine conflict or the tensions in China and Taiwan is to shovel more of your hard-earned tax dollars and more weaponry into the fight", "d24"))
said(cid, "economy", "2024-10-29", "Same debate, in his closing remarks on foreign policy and spending.",
     Q("American tax dollars should be prioritized for our own needs at home and diplomacy abroad instead of for foreign wars", "d24"))
said(cid, "abortion", "2024-10-29", "Same debate, asked about Congress’s role on abortion (reported by CT Mirror; not a direct quote).",
     T("CT Mirror reported that Wesley said he would support legislation to codify the protections once covered under Roe v. Wade into federal law.", "d24"))

# --- Austin
cid = "ct-02-austin"
add_src(cid, "conv", "CT Mirror: CT GOP opens convention, nominating down-ballot candidates (May 15, 2026)", "https://ctmirror.org/2026/05/15/ct-gop-opens-convention-fazio-mccaughey/")
said(cid, "abortion", "2026-05-15", "CT Mirror’s convention candidate guide, summarizing how Austin describes his campaign after being nominated by acclamation.",
     T("He says his campaign is about "), Q("standing up for families, protecting the unborn, defending the Second Amendment, and pushing back against oppressive taxes that make life unaffordable", "conv"), T("."))
said(cid, "guns", "2026-05-15", "Same CT Mirror convention guide.",
     Q("standing up for families, protecting the unborn, defending the Second Amendment, and pushing back against oppressive taxes that make life unaffordable", "conv"))

# ---------------- second research pass ----------------
BP = "Ballotpedia Candidate Connection survey (written by the candidate)"
# --- Shea
cid = "ct-05-shea"
add_src(cid, "bp", "Ballotpedia: Chris Shea (Candidate Connection survey, submitted Sept. 30, 2026)", "https://ballotpedia.org/Chris_Shea")
add_src(cid, "nj", "CT News Junkie: Navy SEAL Chris Shea Announces 5th District Congressional Campaign (Jan. 22, 2026)", "https://ctnewsjunkie.com/2026/01/22/navy-seal-chris-shea-announces-5th-district-congressional-campaign/")
said(cid, "lgbtq", "2026-09-30", "Ballotpedia Candidate Connection survey, in answer to a request to list three key messages of his campaign.",
     Q("Protect the rights and privacy of females by removing biological men from women’s sports and locker rooms.", "bp"))
said(cid, "climate", "2026-01-22", "Statement announcing his campaign, criticizing Rep. Jahana Hayes.",
     T("He said Hayes is "), Q("backing policies that drive up energy costs, undermine public safety, and leave working families like mine paying the price", "nj"), T("."))
# --- Austin
cid = "ct-02-austin"
add_src(cid, "bp", "Ballotpedia: George Austin (Candidate Connection survey, submitted Sept. 27, 2026)", "https://ballotpedia.org/George_Austin")
said(cid, "immigration", "2026-09-27", "Ballotpedia Candidate Connection survey, in answer to “What areas of public policy are you personally passionate about?”",
     Q("As a first-generation American, I believe in secure borders and a lawful immigration system that works.", "bp"))
# --- Lancia
cid = "ct-03-lancia"
add_src(cid, "nhi", "New Haven Independent: Cable Guy Runs (Shhh!) For Congress (Sept. 23, 2026)", "https://www.newhavenindependent.org/2026/09/23/cable-guy-runs-shhh-for-congress/")
add_src(cid, "wt", "Waterbury Times: Coast Guard Veteran Christopher Lancia Launches Bid for Congress (June 9, 2026)", "https://thewaterburytimes.com/2026/06/09/christopher-lancia-launches-connecticut-3rd-district-congressional-campaign/")
said(cid, "abortion", "2026-09-23", "Interview on WNHH FM’s “Dateline New Haven,” as reported by the New Haven Independent (a summary by the outlet, not a direct quote).",
     T("The New Haven Independent reported that Lancia personally opposes abortion and says states, not the federal government, should decide the issue, though he also said he respects Connecticut law on the matter.", "nhi"))
said(cid, "climate", "2026-06-09", "Radio appearance on WTIC’s “Reese on the Radio,” quoted when his campaign launched.",
     Q("We need affordability, we need better energy prices, we need to take care of our Social Security, and we need to take care of our veterans", "wt"))
# --- Chai
cid = "ct-01-chai"
add_src(cid, "nhi22", "New Haven Independent: Congressional Candidate Chai Eyes “4th Trimester” (Aug. 31, 2022)", "https://www.newhavenindependent.org/2022/08/31/congressional_candidate_chai_eyes_4th_trimester/")
said(cid, "abortion", "2022-08-31", "Interview during her 2022 run for Connecticut’s 3rd District as an Independent Party candidate (she is now the Republican nominee in the 1st District). This is the outlet’s summary, not a direct quote.",
     T("The New Haven Independent reported that she would support a federal law codifying the legality of “therapeutic” abortions to protect the life and health of the mother and in cases of rape, and would let states decide whether to permit “elective” abortions.", "nhi22"))
# --- Courtney taxes
cid = "ct-02-courtney"
add_src(cid, "taxno", "Rep. Courtney press release: Courtney Votes NO on the Largest Health Care Cut in U.S. History & A Tax Giveaway for the Rich (July 3, 2025)", "https://courtney.house.gov/media-center/press-releases/courtney-votes-no-largest-health-care-cut-us-history-tax-giveaway-rich")
said(cid, "taxes", "2025-07-03", "Press statement after he voted “no” on H.R. 1, the “One Big Beautiful Bill Act.”",
     Q("the Republican majority in Congress chose to jam through a partisan budget bill which gives a massive tax break to millionaires and billionaires and partially offsets it with the largest health care cut in U.S. history", "taxno"))
# --- Sanders (2022 Ballotpedia survey, same seat)
cid = "ct-01-sanders"
add_src(cid, "bp", "Ballotpedia: Mary Sanders (Candidate Connection survey, 2022)", "https://ballotpedia.org/Mary_Sanders")
SCTX = "Ballotpedia Candidate Connection survey she completed in 2022 for her earlier run for this seat; asked what public policy areas she is passionate about."
said(cid, "abortion", "2022", SCTX, T("She described herself as "), Q("a Pro-choice, Social Progressive and Fiscal Moderate", "bp"), T(" and listed "), Q("codifying Roe", "bp"), T(" among her policy priorities."))
said(cid, "healthcare", "2022", SCTX, T("She listed "), Q("universal healthcare/Medicare for All", "bp"), T(" among her policy priorities."))
said(cid, "climate", "2022", "Ballotpedia Candidate Connection survey she completed in 2022 for her earlier run for this seat; asked for three key campaign messages.",
     Q("I want to address climate change and save our melting planet.", "bp"))
said(cid, "defense", "2022", "Ballotpedia Candidate Connection survey she completed in 2022 for her earlier run for this seat; asked for three key campaign messages.",
     Q("The military budget has been out of control for a long time with impractical spending on weapons development, the establishment of bases in too many countries and for many of the wrong reasons.", "bp"))
said(cid, "education", "2022", SCTX, T("She listed "), Q("free community and state college", "bp"), T(" among her policy priorities."))
# --- Wesley (2024 Ballotpedia survey)
cid = "ct-04-wesley"
add_src(cid, "bp", "Ballotpedia: Benjamin Wesley (Candidate Connection survey, 2024)", "https://ballotpedia.org/Benjamin_Wesley")
said(cid, "defense", "2024", "Ballotpedia Candidate Connection survey he completed in 2024 for his earlier run for this seat; asked for three key campaign messages.",
     Q("America does not need the one trillion dollar plus annual defense budget that it currently has.", "bp"))
said(cid, "education", "2024", "Ballotpedia Candidate Connection survey he completed in 2024 for his earlier run for this seat; asked for three key campaign messages.",
     Q("The education of our children is critical to the betterment of our society.", "bp"))
BYID["ct-01-sanders"].pop("noInfo", None)
# --- Goldstein: his campaign Substack
G = "ct-04-goldstein"
add_src(G, "sue", "The Goldstein Substack: Sue Kathy - Connecticut’s Only Solution for the Energy Price Crisis (Sept. 30, 2026)", "https://drmichaelgoldstein4ct.substack.com/p/sue-kathy-connecticuts-only-solution")
add_src(G, "sen", "The Goldstein Substack: Speaking with Seniors in Stamford (Sept. 10, 2026)", "https://drmichaelgoldstein4ct.substack.com/p/speaking-with-seniors-in-stamford")
said(G, "climate", "2026-09-30", "Post on his campaign Substack, co-written with Jonathan Goldstein, about natural gas pipeline access.",
     Q("Connecticut does not have sufficient natural gas pipeline capacity to deliver a sufficient supply of domestic natural gas to meet it’s needs and currently has to purchase foreign natural gas at a significantly higher price.", "sue"))

# --- Lamont: governor's press releases and CT Mirror (fourth research pass)
L = "ct-gov-lamont"
add_src(L, "gun26", "Governor Lamont press release: Signs Legislation Prohibiting the Sale and Importation of Pistols That Can Easily Be Converted Into Machine Guns (June 2026)", "https://portal.ct.gov/governor/news/press-releases/2026/06-2026/governor-lamont-signs-legislation-prohibiting-the-sale-of-pistols-that-can-easily-be-converted")
add_src(L, "pride", "Governor Lamont press release: Issues Proclamation Declaring Pride Month (June 2026)", "https://portal.ct.gov/governor/news/press-releases/2026/06-2026/governor-lamont-issues-proclamation-declaring-pride-month")
add_src(L, "eb", "Governor Lamont press release: Applauds U.S. Navy’s $76.6 Billion Contract Awarded to General Dynamics Electric Boat (July 2026)", "https://portal.ct.gov/governor/news/press-releases/2026/07-2026/governor-lamont-applauds-contract-awarded-to-general-dynamics-electric-boat")
add_src(L, "ice", "CT Mirror: CT Gov. Lamont signs ICE law, defying Trump administration (May 4, 2026)", "https://ctmirror.org/2026/05/04/ice-bill-lamont-signing-ceremony/")
said(L, "guns", "2026-06", "Governor’s press release on signing legislation (Public Act 26-41) that prohibits the sale and importation of pistols that can easily be converted into machine guns.",
     Q("With the lack of action on gun violence prevention measures being passed by Congress, it is up to the individual states to enact laws like these", "gun26"))
said(L, "lgbtq", "2026-06", "Governor’s press release on his proclamation declaring June Pride Month in Connecticut.",
     Q("I am committed to ensuring that our laws and regulations continue to provide everyone with equal protection, and I vow to stand up to any efforts to turn back the clock on equality", "pride"))
said(L, "immigration", "2026-05-04", "Ceremony on the steps of the Connecticut Supreme Court where he signed SB 397, a law limiting ICE arrests at schools, churches and other sensitive places.",
     Q("There are a lot of folks who belong in this state, and that’s what this law is all about.", "ice"))
said(L, "defense", "2026-07", "Governor’s press release after the Navy awarded Electric Boat a $76.6 billion submarine contract.",
     Q("Electric Boat builds the best submarines in the world, and Connecticut has the best workforce in the world to build them", "eb"))

# --- Fazio: LWV Greenwich debate vs. Nick Simmons (Oct. 2024), read in a browser (page text is JavaScript-loaded)
add_src("ct-gov-fazio", "lwv", "Greenwich Free Press: 36th District State Senate Candidates Spar on Gun Safety, Abortion, Cost of Living, Taxes (Oct. 16, 2024)", "https://greenwichfreepress.com/news/government/36th-district-state-senate-candidates-spar-on-gun-safety-abortion-cost-of-living-taxes-222958/")
LWV = "League of Women Voters Greenwich debate with Democratic challenger Nick Simmons, in answer to a question about whether any gun safety regulations have gone too far. "
said("ct-gov-fazio", "guns", "2024-10-16", LWV + "Simmons had criticized Fazio’s vote against a 2023 gun bill.",
     Q("Connecticut has probably the second or third strongest guns safety laws in the country. I not only support those laws", "lwv"))
said("ct-gov-fazio", "abortion", "2024-10-16", "Same debate, asked about the Reproductive Freedom Defense Act (HB 5414), which he voted against.",
     Q("Like many complex regulatory issues, I could be wrong in the long run, and I am open to that possibility, but the evidence at that point made me concerned it would undermine health and safety", "lwv"))

# ---------------- third research pass ----------------
def web(cid, topic, *segs):
    """Content from the candidate's own website (shown as the main statement for the topic)."""
    t = BYID[cid]["topics"]
    para = list(segs)
    cur = t.get(topic)
    if isinstance(cur, dict):
        cur["paras"] = cur.get("paras", []) + [para]; cur["gap"] = False
    elif isinstance(cur, list):
        cur.append(para)
    else:
        t[topic] = [para]

# --- Wesley has a campaign website
w = BYID["ct-04-wesley"]
w["website"] = "https://benwesleyforcongress.com"
w["reviewed"] = "home"
w["sources"].append(src("home", "Ben Wesley for Congress (home page)", "https://benwesleyforcongress.com/"))
w["overview"].append([T("His campaign website says "), Q("Help us campaign today for a Peaceful World and Prosperous Connecticut!", "home"), T(" and calls for "), Q("leadership that fights for peace and prosperity", "home"), T(".")])
web("ct-04-wesley", "defense", T("The site says "), Q("We must demand leadership that fights for peace and prosperity!", "home"))
web("ct-04-wesley", "economy", T("The site opens by citing "), Q("A 40 Trillion dollar debt", "home"), T(" and saying "), Q("It's time we look to each other to speak out and fight for real solutions.", "home"))
w.pop("noInfo", None)
add_src("ct-04-wesley", "p24", "Patch: 4th Congressional District Race: Himes, Goldstein, Wesley (Oct. 15, 2024)", "https://patch.com/connecticut/across-ct/4th-congressional-district-race-himes-goldstein-wesley")
said("ct-04-wesley", "healthcare", "2024-10-15", "Statement quoted by Patch in its 2024 race overview, when he first ran for this seat.",
     Q("I'm looking forward to bringing a message of peace and development to my fellow man. This includes affordable housing, improved schools, health care for all, new infrastructure, and more social services for Congressional District 4", "p24"))
said("ct-04-wesley", "education", "2024-10-15", "Same Patch overview of the 2024 race, in the same statement.",
     Q("improved schools", "p24"), T(" were among the items he listed alongside "), Q("health care for all", "p24"), T("."))

# --- Austin: Patch candidate questionnaire (Oct. 14, 2026)
add_src("ct-02-austin", "pq", "Patch: 2026 Candidate Profiles: George Austin Is Running For Congress (Oct. 14, 2026)", "https://patch.com/connecticut/vernon/2026-candidate-profiles-george-austin-running-congress")
said("ct-02-austin", "climate", "2026-10-14", "Patch candidate questionnaire, answering “Energy costs have been soaring in Connecticut. What are your plans to help address this issue?”",
     Q("Our energy prices are soaring, and much of this is largely self-inflicted.", "pq"))
said("ct-02-austin", "economy", "2026-10-14", "Patch candidate questionnaire, answering “What do you believe is the No. 1 issue facing Connecticut?”",
     Q("Cost of living. One of the primary culprits is runaway inflation", "pq"))

# --- Egan: WNHH interview reported by CT News Junkie
cid = "ct-03-egan"
add_src(cid, "nj", "CT News Junkie: DeLauro Challenger Targets Insurers (Sept. 16, 2026)", "https://ctnewsjunkie.com/2026/09/16/delauro-challenger-targets-insurers/")
EG = "Interview on WNHH FM’s “Dateline New Haven,” as summarized by CT News Junkie (the outlet’s summary, not a direct quote)."
said(cid, "immigration", "2026-09-16", EG,
     T("CT News Junkie reported that Egan spoke of ending current federal immigration raids in favor of a pathway to citizenship for undocumented people already here.", "nj"))
said(cid, "economy", "2026-09-16", EG,
     T("CT News Junkie reported that Egan spoke of raising the $7.25 federal hourly minimum wage and of maintaining funding that helps people who struggle to pay rent.", "nj"))
BYID[cid].pop("noInfo", None)
BYID[cid]["noInfoNote"] = True

# --- debate quotes: Himes, Goldstein (2024), Hayes (2026)
add_src("ct-04-himes", "d24", "CT Mirror: U.S. Rep. Jim Himes, two challengers parry in 4th District debate (Oct. 29, 2024)", "https://ctmirror.org/2024/10/29/ct-4th-district-debate-jim-himes-michael-goldstein-benjamin-wesley/")
said("ct-04-himes", "taxes", "2024-10-29", "CT Examiner–hosted debate with Michael Goldstein and Ben Wesley, asked how Congress should respond to Trump-era tax cuts set to expire in 2025.",
     Q("I actually agree with the point of view of President Biden, which is that we will allow the tax cuts on the very wealthiest Americans to expire", "d24"))
said("ct-04-goldstein", "economy", "2024-10-29", "Same debate, answering the question about extending expiring tax cuts.",
     Q("In my opinion, keeping taxes low is a way to stimulating the economy", "d24"))
add_src("ct-05-hayes", "deb", "CT Public: Jahana Hayes, Chris Shea square off in CT 5th District debate (Oct. 14, 2026)", "https://www.ctpublic.org/news/2026-10-14/jahana-hayes-chris-shea-debate-congress-5th-district-ct")
said("ct-05-hayes", "taxes", "2026-10-14", "League of Women Voters of Litchfield County debate with Chris Shea, discussing the 2025 tax law (H.R. 1).",
     T("CT Public reported that Hayes said she supports tax relief provisions like those in the law but called the temporary tax breaks "), Q("crumbs on the table", "deb"), T(" while wealthier people and corporations benefit from permanent tax cuts."))


import plans
plans.build(BYID, T, Q, add_src)
import state_research
state_research.build(BYID, T, Q, add_src)

# every core topic is selectable for every candidate; fill the ones with nothing
CORE = ["abortion", "lgbtq", "taxes", "defense", "healthcare", "immigration", "economy", "climate", "guns", "education"]
for c in C:
    for t in CORE:
        c["topics"].setdefault(t, {"gap": True, "said": []})
    for t, v in list(c["topics"].items()):
        if isinstance(v, list):
            c["topics"][t] = {"gap": False, "paras": v, "said": []}
    for v in c["topics"].values():
        v.setdefault("plan", [])
    c["noWebsite"] = c.get("website") is None

out = {
    "state": "CT",
    "updated": ACCESSED,
    "note": "Generated by tools/build_data.py. Do not edit by hand.",
    "candidates": C,
}
path = pathlib.Path(__file__).resolve().parent.parent / "data" / "candidates.json"
path.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print(f"wrote {len(C)} candidates -> {path}")

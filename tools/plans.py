"""Plans of action: concrete proposals each candidate says they will pursue, by topic.

Imported by build_data.py (which provides C, BYID, T, Q, src, add_src). Every item cites a source;
direct quotes are checked by verify_quotes.py. A topic with no entry shows "no specific plan found".
"""

def build(BYID, T, Q, add_src):
    def plan(cid, topic, *paras):
        t = BYID[cid]["topics"]
        cur = t.get(topic)
        if isinstance(cur, list):
            cur = t[topic] = {"gap": False, "paras": cur, "said": []}
        if cur is None:
            cur = t[topic] = {"gap": True, "said": []}
        cur.setdefault("plan", []).extend(paras)

    # ---------------- Lamont ----------------
    c = "ct-gov-lamont"
    plan(c, "abortion", [T("His healthcare agenda says that means continuing to "), Q("Protect reproductive freedom and abortion access", "pri"), T(".")])
    plan(c, "healthcare",
        [T("Listed steps include "), Q("Lower prescription drug costs", "pri"), T(", "), Q("Expand access to high-quality healthcare coverage with the CT Option", "pri"), T(" and "), Q("Strengthen preventative and mental healthcare services", "pri"), T(".")],
        [T("His “Fair Share Healthcare Initiative” would require employers with more than 100 employees (and nonprofits with more than 1,000) whose workers are enrolled in HUSKY to contribute up to $1,000 per employee, and would ", "pri"), Q("Invest more than $100 million annually into Connecticut’s health insurance exchange and Covered Connecticut program", "pri"), T(".")],
        [T("He also lists "), Q("Explore bold solutions that move Connecticut toward universal affordable healthcare", "pri"), T(".")])
    plan(c, "climate",
        [T("On climate, the site lists "), Q("A continued push for energy efficiency. This starts with weatherization, deploying highly efficient heat pumps, and moving towards electrification, while updating our building codes to include higher energy efficiency standards.", "pri")],
        [T("On utility costs: "), Q("Hold utilities accountable through stronger oversight, transparency requirements, and regular reviews of their performance.", "pri"), T(" and "), Q("Strengthen the Office of Consumer Counsel’s ability to investigate utility practices and challenge unjustified rate increases.", "pri")],
        [Q("Increase competition by allowing more private investment in energy infrastructure, microgrids, and innovative technologies.", "pri")])
    plan(c, "economy", [T("Listed steps include "), Q("Expanding housing supply near transit and job centers", "pri"), T(", "), Q("Supporting workforce and middle-income housing", "pri"), T(" and "), Q("Supporting working parents and strengthening paid family leave protections", "pri"), T(".")])
    plan(c, "education", [T("Listed steps include "), Q("Build a sustainable long-term funding structure for early childhood education", "pri"), T(", "), Q("Increasing state support for special education", "pri"), T(" and "), Q("Supporting teachers and school staff", "pri"), T(".")])

    plan(c, "guns", [T("He signed a 2026 law that prohibits the sale and importation of pistols that can easily be converted into machine guns; he said it "), Q("holds manufacturers to a basic safety standard requiring firearms not to be designed in a way that enables them to be converted into machine guns", "gun26"), T(".")])
    plan(c, "lgbtq", [Q("I am committed to ensuring that our laws and regulations continue to provide everyone with equal protection, and I vow to stand up to any efforts to turn back the clock on equality", "pride")])
    plan(c, "immigration", [T("He signed SB 397, which CT Mirror described as a law drafted to curtail ICE roundups at schools, churches and other sensitive places, require federal agents to be identifiable by name tag or badge number, and give the state inspector general jurisdiction to review ICE’s use of lethal force.", "ice")])
    plan(c, "defense", [Q("That’s why we’re investing in affordable housing, transportation, and great schools, so that the families moving to the New London area to build the future of our Navy have every reason to put down roots and stay", "eb")])

    # ---------------- Fazio ----------------
    c = "ct-gov-fazio"
    add_src(c, "elec", "Ryan Fazio for Governor: Plan to cut electricity bills", "https://ryanfazio.com/reduce-electricity-bills-20/")
    add_src(c, "prop", "Ryan Fazio for Governor: Four-part plan to cap property taxes", "https://ryanfazio.com/ryans-four-part-plan-to-cap-property-taxes/")
    add_src(c, "house", "Ryan Fazio for Governor: Housing affordability and local control", "https://ryanfazio.com/housing-affordability-local-control/")
    add_src(c, "m922", "CT Mirror: Ryan Fazio pledges unprecedented CT income tax cut (Sept. 22, 2026)", "https://ctmirror.org/2026/09/22/ryan-fazio-pledges-unprecedented-ct-income-tax-cut/")
    plan(c, "taxes",
        [T("Cut income tax rates by about 2 percentage points for most families, worth roughly $2.5 billion a year by the fourth year of his term (for example, 4.5% to 2.5% and 5.5% to 3.5%).", "tax")],
        [T("Pay for it by reducing "), Q("wasteful and politically oriented spending by about $1 billion per year by 2031", "tax"), T(", including ending political earmarks and over-budgeting for agencies.")],
        [Q("Cap property tax increases at no greater than 2% or the rate of inflation", "house"), T(", and "), Q("Require a 60% vote of the legislature for any legislation that creates new mandates or imposes additional costs on municipalities", "prop"), T(".")],
        [Q("Full expensing of capital expenditures to incentivize building factories, offices, buying machinery and plants", "tax")],
        [T("CT Mirror reported that the plan relies partly on spending and revenue estimates from last November, and that the legislature’s nonpartisan analysts now project operating deficits.", "m922")])
    plan(c, "healthcare", [T("CT Mirror reported that his relief plan would end state-sponsored healthcare for undocumented adults and children, impose a “managed care” system to cap Medicaid assistance, and cut Medicaid spending by about $336 million a year by 2031.", "m922")])
    plan(c, "climate",
        [T("Eliminate the Public Benefits Charge: end or sunset most of the 50-plus programs funded through it and move a small portion of the rest into the state budget.", "elec")],
        [T("End the Renewable Portfolio Standard and Regional Greenhouse Gas Initiative charges in the supply portion of bills, or let nuclear and hydropower count toward the standard.", "elec")],
        [Q("Expand natural gas pipeline capacity from Pennsylvania", "elec"), T(", and "), Q("Have Connecticut officially intervene through the federal regulatory process at FERC or sue the State of New York if it continues to block pipeline expansion proposals", "elec"), T(".")],
        [Q("Limit any long-term contract for electricity to no more than a nominal difference from the wholesale market price of electricity", "elec"), T(", and "), Q("Eliminate special tax subsidies for data centers, EV chargers, and heat pump installations", "elec"), T(".")])
    plan(c, "economy",
        [T("Housing: "), Q("Streamline permitting processes to make them more rules-based, speedy, and predictable", "house"), T(", "), Q("Incentivize small-scale housing development and other housing with more community support, including Accessory Dwelling Units, residential in mixed-use areas, and more", "house"), T(", and "), Q("Eliminate or roll back 8-30(g) and H.B. 8002 in a way that gives towns and cities more flexibility", "house"), T(".")])
    plan(c, "education",
        [Q("Materials must be oriented around proven Science of Reading", "edu"), T(", "), Q("High-dosage tutoring for students who fall behind as a systematic intervention", "edu"), T(", "), Q("No more social promotion: High schools cannot graduate students without teaching them how to read", "edu"), T(", and "), Q("Adequate, transparent, student-centered funding", "edu"), T(".")])
    add_src(c, "gfp", "Greenwich Free Press: Senator Fazio Proposes Legislation to Repeal “Radical” 2019 Trust Act (Feb. 2, 2025)", "https://greenwichfreepress.com/news/government/senator-fazio-proposes-legislation-to-repeal-radical-2019-trust-act-greenwich-schools-prepares-for-possibility-of-ice-visits-227219/")
    plan(c, "immigration",
        [T("He introduced Senate Bill 684, “An Act Repealing the Trust Act,” in the 2025 session; it was referred to the Judiciary Committee.", "gfp")],
        [Q("My proposal is to repeal parts of the more radical version in 2019", "gfp"), T(", so that police could "), Q("detain and leverage federal authorities to protect our community from serious criminals in our country illegally", "gfp"), T(". He added: "), Q("It’s not about knocking on every door, schools, or anything like that.", "gfp")])
    plan(c, "guns", [Q("I spoke on the Senate floor that night, simply introducing three amendments that would strengthen that gun law. It would provide a state support system for School Resources Officers", "lwv"), T(", and "), Q("reintroduce policies like consent searches that have taken hundreds of illegal guns off the street in Connecticut", "lwv"), T(". The Greenwich Free Press also reported he said he supports enforcing the existing assault weapons ban.", "lwv")])
    plan(c, "abortion", [T("The Greenwich Free Press reported he said he supports keeping abortion legal in Connecticut and would do more to expand access to oral contraceptives; he said "), Q("I co-authored and passed a new law that will expand access to oral contraceptives in Connecticut", "lwv"), T(".")])
    plan(c, "healthcare", [Q("I have a proposal with 3 Democrats and 2 Republicans that would reform certificate of need laws", "lwv"), T(", which he said has "), Q("reduced healthcare costs by four to 10% and improved access", "lwv"), T(" in other states.")])
    plan(c, "safety", [Q("reforms the 2020 anti-police legislation, closes parole loopholes for violent offenders, and reinstates proactive policing", "iss")])
    plan(c, "veterans", [Q("streamline veteran services, reduce costs, cut fees, recognize out-of-state licenses", "iss")])

    # ---------------- Bronin ----------------
    c = "ct-01-bronin"
    for k, t, u in [("bimm", "Immigration", "immigration"), ("brep", "Safeguarding Reproductive Freedom", "safeguarding-reproductive-freedom"),
                    ("bhr", "Protecting LGBTQ+ Rights", "protecting-human-rights"), ("bgun", "Reducing Gun Violence", "reducing-gun-violence"),
                    ("bclim", "Taking Climate Change Seriously", "climate-change"), ("bedu", "Educating Our Kids", "educating-our-kids"),
                    ("bhc", "Protecting Medicare, Medicaid, & Pushing for Universal Healthcare", "protecting-medicare-medicaid-and-pushing-for-universal-healthcare"),
                    ("btax", "Creating a Fair Tax Code", "affordability"), ("bcost", "Bringing Down Costs", "Reforma")]:
        add_src(c, k, f"Luke Bronin for Congress: {t}", f"https://www.broninforcongress.com/issues/{u}")
    plan(c, "abortion", [Q("Congress must pass federal protections for abortion access nationwide.", "brep"), T(" He says that as mayor he led an ordinance on crisis pregnancy centers that "), Q("became a model for legislation in the state of Connecticut", "brep"), T(".")])
    plan(c, "lgbtq", [Q("In Congress, I’ll fight to pass the Equality Act", "bhr"), T(", enshrine protections for marriage equality, and support the Global Respect Act.", "bhr")])
    plan(c, "taxes",
        [T("Close loopholes such as carried interest, "), Q("increasing the estate tax and ending dynastic trusts", "btax"), T(".")],
        [Q("adding two new top income tax brackets", "btax"), T(", "), Q("Make the capital gains tax more progressive", "btax"), T(", and "), Q("restoring the corporate tax rate back to the pre-Trump rate of 35% or at minimum to 28%", "btax"), T(".")])
    plan(c, "healthcare",
        [Q("We need a strong public option so that any American who wants to participate in Medicare can do so.", "bhc")],
        [Q("In the near term, we must pass the Break Up Big Medicine Act", "bhc"), T(", a bipartisan bill to break up healthcare monopolies.", "bhc")])
    plan(c, "immigration",
        [Q("Democrats must condition support for the Homeland Security Department budget on meaningful immigration reforms", "bimm"), T(", including a ban on masks, warrant requirements and visible identification for officers.", "bimm")],
        [Q("Abolish ICE, which has only existed since 2003.", "bimm"), T(" Then pursue comprehensive reform with "), Q("secure borders, fair and timely asylum processing, citizenship for DACA recipients, legal pathways that encourage more legal immigration", "bimm"), T(".")])
    plan(c, "economy", [Q("We need to build more housing, produce cheaper renewable energy, and make sure markets actually work to give consumers real choices.", "bcost")])
    plan(c, "climate", [Q("We need a massive commitment to more affordable, clean energy. Solar, wind, hydro, fuel cells, nuclear, and building better batteries.", "bclim"), T(" He says that means "), Q("streamlining red tape that makes it too hard and costly to build", "bclim"), T(".")])
    plan(c, "guns",
        [Q("universal background checks, an assault weapons ban, safe storage laws, red-flag laws, firearms education", "bgun")],
        [Q("I’ll support vital community violence prevention work like violence interrupters and hospital-based violence intervention programs.", "bgun"), T(" He also says he would "), Q("reverse the Trump administration’s damaging cuts to ATF", "bgun"), T(".")])
    plan(c, "education", [Q("we should ban phones in schools. Period.", "bedu"), T(" He also lists "), Q("smaller class sizes, stronger teacher training and recruitment, better teacher pay", "bedu"), T(".")])

    # ---------------- Chai ----------------
    c = "ct-01-chai"
    add_src(c, "bp", "Ballotpedia: Amy Chai (Candidate Connection survey, 2025)", "https://ballotpedia.org/Amy_Chai")
    plan(c, "abortion", [T("In 2022 she told the New Haven Independent she would support a federal law codifying the legality of “therapeutic” abortions and let states decide on “elective” abortions.", "nhi22")])
    plan(c, "taxes", [Q("Property taxes must be capped.", "iss"), T(" "), Q("The self-employment tax (FICA at 15%) must be eliminated if fairness is to be restored.", "iss"), T(" "), Q("More tax on financial industry and less tax on earned income will help to offset this harsh imbalance", "iss"), T(".")])
    plan(c, "healthcare",
        [Q("A few laser-targeted laws could substantially reduce costs nationwide.", "iss")],
        [Q("With caps on profits for VCs that own healthcare conglomerates, we can immediately put the next 2.6 trillion back in your pocket.", "bp")])
    plan(c, "immigration", [Q("I do not believe that a US Representative should impede the enforcement of border security, ever.", "bp")])
    plan(c, "economy", [Q("we must prepare the next generation to be flexible and skilled", "iss")])
    plan(c, "education", [Q("Real science should be used to determine the best teaching and learning strategies.", "iss"), T(" "), Q("Disruptive and non-English speaking students should be placed in separate learning environments when possible", "iss"), T(".")])

    # ---------------- Courtney ----------------
    c = "ct-02-courtney"
    plan(c, "taxes", [Q("Like any law, it can be overturned, and over time, the will of the majority will ensure that it is.", "taxno"), T(" (on H.R. 1)")])
    plan(c, "defense", [T("His biography credits him with "), Q("leading the call for increased submarine production", "bio"), T(", and a 2026 press release says "), Q("we now need to double down on the Manufacturing Pipeline Initiative’s success for decades to come", "mpi"), T(".")])
    plan(c, "healthcare", [Q("Congress should pass the Lowering Drug Costs for American Families Act into law", "op"), T(", a bill that would let Medicare negotiate drug prices for people on employer-based and ACA marketplace plans, not only those 65 and older.", "op")])
    plan(c, "immigration", [Q("I cosponsored a bill to fully fund all DHS agencies except for ICE and CBP", "dhs")])
    plan(c, "economy", [Q("we now need to double down on the Manufacturing Pipeline Initiative’s success for decades to come", "mpi")])
    plan(c, "guns", [T("He co-sponsored and voted for the Assault Weapons Ban Act of 2022, which would prohibit the sale, manufacture, transfer or possession of semiautomatic assault weapons and high-capacity magazines.", "awb")])

    # ---------------- Austin ----------------
    c = "ct-02-austin"
    plan(c, "taxes", [Q("In Congress, I will fight for full deductibility of state and local taxes, tax relief for overtime earnings, and a larger capital-gains exclusion when people sell their primary home.", "bp")])
    plan(c, "defense", [Q("I’ll fight to direct federal funds toward apprenticeships, job training, and technical education", "opp"), T(", building "), Q("strong partnerships with Connecticut’s manufacturers, defense industries, and small businesses", "opp"), T(".")])
    plan(c, "economy", [Q("I support a first-time homebuyer tax credit, a larger capital-gains exclusion on primary-home sales, and removing unnecessary barriers to building starter homes and reasonably priced rentals.", "bp")])
    plan(c, "climate", [Q("I would take steps to make sure FERC has policies with teeth to disallow other states from infringing upon our ability to access affordable energy", "pq"), T(".")])
    plan(c, "education", [Q("reintroducing classes like wood & metal shop into high schools", "opp"), T(", expanding "), Q("technical programs like on the job learning", "opp"), T(", and creating "), Q("new training centers", "opp"), T(".")])

    # ---------------- DeLauro ----------------
    c = "ct-03-delauro"
    plan(c, "abortion", [Q("I am leading the effort to codify the protections of Roe v. Wade into federal law", "hc"), T(".")])
    plan(c, "taxes", [T("On the expanded Child Tax Credit: "), Q("I am fighting every day to make it permanent", "col"), T(".")])
    plan(c, "defense", [T("She says Democrats should be able to offer amendments on "), Q("strengthening our industrial base, reforming procurement and acquisition processes, and supporting our allies around the world", "ndaa"), T(".")])
    plan(c, "healthcare", [T("She says she fights for "), Q("policies that will strengthen the Affordable Care Act, Medicare, and Medicaid", "hc"), T(" and to reduce costs.")])
    plan(c, "economy", [T("Her listed commitments include "), Q("Protect the right to organize.", "col"), T(" and "), Q("Defend Social Security and Medicare.", "col")])
    plan(c, "climate", [Q("I am working to attract investment for offshore wind energy, advanced battery manufacturing, and green hydrogen technology", "clim"), T(".")])
    plan(c, "guns", [T("She "), Q("authored and introduced Ethan’s Law", "gv"), T(" and wants to keep "), Q("weapons of war off our streets", "gv"), T(" while "), Q("investing in community-based solutions that prevent violence before it starts", "gv"), T(".")])
    plan(c, "education", [Q("I fight everyday to deliver federal resources directly to our schools", "edu"), T(".")])

    # ---------------- Lancia ----------------
    c = "ct-03-lancia"
    plan(c, "taxes", [Q("an end to the reckless spending that’s driving up inflation", "home"), T(", alongside lower taxes and a balanced budget.")])
    plan(c, "immigration", [Q("We must control our borders to stop the flow of drugs and crime into our towns.", "home")])
    plan(c, "education", [Q("Schools should focus on academics, not agendas.", "home")])

    # ---------------- Himes (quotes verified locally when his site blocks the checker) ----------------
    c = "ct-04-himes"
    plan(c, "taxes", [Q("I actually agree with the point of view of President Biden, which is that we will allow the tax cuts on the very wealthiest Americans to expire", "d24")])
    plan(c, "lgbtq", [T("On the Equality Act, which he co-sponsored: he "), Q("won’t stop fighting until it is signed into law", "lgbt"), T(".")])
    plan(c, "healthcare", [T("His site says he works to "), Q("make Medicare sustainable for future generations, improve the Affordable Care Act", "hc"), T(" and "), Q("put Social Security on a path to long-term stability", "hc"), T(".")])
    plan(c, "defense", [T("He "), Q("has advocated for legislation to increase private-public partnerships", "nat"), T(" on security technology, and "), Q("introduced legislation to improve intelligence community oversight", "nat"), T(".")])
    plan(c, "immigration", [T("CT Mirror reported that he said he wants more border patrol and more judges to adjudicate asylum cases, and pointed to his support for the bipartisan border bill brokered in part by Sen. Chris Murphy.", "d24")])
    plan(c, "economy", [T("His site says he is "), Q("turning his efforts towards reforming the mortgage finance industry", "eco"), T(" to lower living costs and increase affordable housing.")])
    plan(c, "climate", [Q("we need to speed up this process to achieve true sustainability for future generations", "env"), T(".")])
    plan(c, "education", [Q("pushing for legislation that gives states and local districts more flexibility without losing accountability", "edu"), T(", and he is "), Q("committed to ensuring that all students can get an affordable college education", "edu"), T(".")])

    # ---------------- Goldstein ----------------
    c = "ct-04-goldstein"
    plan(c, "abortion", [T("CT Mirror reported he said abortion policy is up to each state and that voters should be able to decide it in a referendum.", "d24")])
    plan(c, "lgbtq", [T("His platform lists "), Q("Ban gender-affirming surgery until adulthood", "home"), T(".")])
    plan(c, "taxes", [T("His platform lists "), Q("Keep taxes low", "home"), T(".")])
    plan(c, "healthcare",
        [Q("I will fight to slash regulatory burden, restore real market competition, and bring healthcare costs down for every Connecticut family.", "home")],
        [T("He also says he will "), Q("break the stranglehold that bureaucracy, PBMs, insurance middlemen, and patent manipulation have on healthcare costs", "home"), T(".")])
    plan(c, "immigration", [T("His platform lists "), Q("Close border to illegal aliens and drugs", "home"), T(".")])
    plan(c, "economy", [T("His platform lists "), Q("Reduce regulatory burdens on small businesses", "home"), T(" and "), Q("Unleash American innovation", "home"), T(".")])
    plan(c, "climate", [Q("I will fight for federal legislation that unblocks pipeline expansion, embraces an all-of-the-above energy strategy", "home"), T(" including natural gas, nuclear and renewables.")])
    plan(c, "climate", [Q("The State of Connecticut should sue the State of New York for violation of the Sherman Antitrust Act and Clayton Act for unfairly restraining trade.", "sue"), T(" He adds that "), Q("Connecticut should ask the Supreme Court for Injunctive Relief invalidating Governor Hochul’s Constitution Pipeline veto", "sue"), T(".")])
    plan(c, "education", [Q("There is also a need for expansion of Trade Schools.", "sen")])
    plan(c, "education", [Q("Vocational training vouchers. Technical high schools. Career academies.", "home"), T(" He also proposes "), Q("Graduate from CT college, work here 5 years, we forgive up to $25,000", "home"), T(".")])

    # ---------------- Hayes ----------------
    c = "ct-05-hayes"
    plan(c, "abortion", [Q("remains committed to codifying a woman’s right to choose", "rep")])
    plan(c, "lgbtq", [T("She is "), Q("supporting the Equality Act", "lgbt"), T(".")])
    plan(c, "taxes", [T("CT Public reported that Hayes said she would prioritize trying to rescind some of the cuts to programs like Medicaid and SNAP made by the 2025 tax law (H.R. 1).", "deb")])
    plan(c, "defense", [T("CT Public reported that she said she has voted five times for war powers resolutions that would rein in military action until the president seeks congressional approval, and that she supports impeaching Defense Secretary Pete Hegseth.", "deb")])
    plan(c, "healthcare", [Q("supporting Medicare for All", "hc"), T(" and "), Q("worked to curb surprise billing, cap prescription drug costs, and support legislation to lower the cost of life-saving care", "hc"), T(".")])
    plan(c, "immigration", [Q("comprehensive legislation to offer a path to citizenship for Dreamers and address the current flaws in the immigration system", "imm")])
    plan(c, "economy", [Q("Expanding access to high-quality jobs and lowering the cost of groceries, gas, and energy", "eco")])
    plan(c, "climate", [Q("led legislation to support zero-emission school buses", "env"), T(" and "), Q("supported research on renewable energy sources", "env"), T(".")])
    plan(c, "guns", [Q("advocating for red flag laws, expanded background checks, gun buyback programs, and raising the age to purchase an automatic weapon", "gun")])
    plan(c, "education", [Q("supporting teacher preparation and pipeline programs and fully funding the Individuals with Disabilities Education Act", "edu")])

    # ---------------- Shea ----------------
    c = "ct-05-shea"
    add_src(c, "deb", "CT Public: Jahana Hayes, Chris Shea square off in CT 5th District debate (Oct. 14, 2026)", "https://www.ctpublic.org/news/2026-10-14/jahana-hayes-chris-shea-debate-congress-5th-district-ct")
    plan(c, "lgbtq", [Q("removing biological men from women’s sports and locker rooms", "bp")])
    plan(c, "taxes", [Q("Make the Working Families Tax Cut Permanent", "bp"), T(". CT Public reported he said he wants the 2025 tax law’s relief measures strengthened or made permanent.", "deb")])
    plan(c, "defense", [Q("advocate for American Military strength, support our troops and veterans", "iss"), T(". On Iran, he said "), Q("If we're going to go to full war with them, then yeah, Congress has to authorize it.", "deb")])
    plan(c, "immigration", [Q("fund border patrol, support law enforcement", "iss"), T(", and in his Ballotpedia survey: "), Q("Close the border.", "bp")])
    plan(c, "economy", [T("His site says he will "), Q("reduce red tape", "iss"), T(" and "), Q("cut wasteful spending in Washington", "iss"), T(".")])
    plan(c, "defense", [T("CT Public reported that he said he would like to serve on a committee with jurisdiction over veterans and defense issues.", "deb")])
    plan(c, "veterans", [T("CT Public reported that he said he would like to serve on a committee with jurisdiction over veterans and defense issues.", "deb")])
    plan(c, "safety", [Q("support law enforcement", "iss")])
    plan(c, "veterans", [Q("improve access to the VA, cut through bureaucratic delays, and make it easier for veterans to get quality healthcare, job opportunities, and the benefits they have earned", "iss")])

    # ---------------- Sanders ----------------
    c = "ct-01-sanders"
    plan(c, "abortion", [Q("codifying Roe", "bp")])
    plan(c, "healthcare", [Q("universal healthcare/Medicare for All", "bp")])
    plan(c, "defense", [T("She says she would be "), Q("advocating for nuclear disarmament, working towards improving relations with other countries, including those seen as our adversaries, ending cruel sanctions and blockades on Cuba and around the world", "bp"), T(".")])
    plan(c, "education", [Q("free community and state college", "bp")])

    # ---------------- Wesley ----------------
    c = "ct-04-wesley"
    plan(c, "defense",
        [Q("Let's identify what savings in military spending can be made and return that money to the People!", "bp"), T(" He also lists "), Q("Retool and diversify our military contractors for a peacetime economy", "bp"), T(".")],
        [T("CT Mirror reported that at a 2024 debate he called for an arms embargo of U.S. weapons to Israel and an immediate ceasefire.", "d24")])
    plan(c, "taxes", [Q("This can be either in the form of lower taxes or investments in affordable housing, improved schools, new infrastructure, and better social services.", "bp")])
    plan(c, "healthcare", [Q("health care for all", "p24"), T(" is among the items he listed in 2024.")])

    # ---------------- Egan ----------------
    c = "ct-03-egan"
    plan(c, "immigration", [T("CT News Junkie reported that he favors ending current federal immigration raids in favor of a pathway to citizenship for undocumented people already here.", "nj")])
    plan(c, "economy", [T("CT News Junkie reported that he spoke of raising the $7.25 federal hourly minimum wage and maintaining funding that helps people who struggle to pay rent.", "nj")])

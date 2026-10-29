"""The Connecticut bills and U.S. House roll calls whose recorded votes appear on candidate pages.

Selection rules (published in the site's method note):
  * one or more floor votes per topic, spread across the last ten legislative sessions (2017-2026);
  * only final-passage roll calls, never amendments or procedural motions;
  * the same list for every legislator, so any two voting records can be compared directly;
  * a bill's description is its official title, with no added characterization.
Each entry: (year, bill, topic id or "other", short label). The vote itself is read from the
official tally, never typed in by hand.
"""

STATE_BILLS = [
    (2017, "SB-1502", "taxes", "State budget for the biennium ending June 30, 2019"),
    (2017, "HB-6695", "lgbtq", "Protection of youth from conversion therapy"),
    (2018, "HB-5542", "guns", "Bump stocks and other means of enhancing the rate of fire of a firearm"),
    (2019, "HB-7424", "taxes", "State budget for the biennium ending June 30, 2021"),
    (2019, "HB-5004", "economy", "Increasing the minimum fair wage"),
    (2019, "SB-1", "economy", "Paid family and medical leave"),
    (2019, "HB-7218", "guns", "Safe storage of firearms in the home and firearm safety programs in public schools"),
    (2019, "HB-7219", "guns", "Ghost guns"),
    (2019, "SB-992", "immigration", "The Trust Act"),
    (2020, "HB-6004", "safety", "Police accountability"),
    (2021, "SB-1201", "other", "Responsible and equitable regulation of adult-use cannabis"),
    (2021, "SB-1", "healthcare", "Equalizing comprehensive access to mental, behavioral and physical health care in response to the pandemic"),
    (2021, "SB-1202", "taxes", "Revenue and other items to implement the state budget for the biennium ending June 30, 2023"),
    (2022, "HB-5414", "abortion", "Protections for persons receiving and providing reproductive health care services and access to those services"),
    (2022, "SB-10", "climate", "Climate change mitigation"),
    (2022, "SB-4", "climate", "The Connecticut Clean Air Act"),
    (2022, "HB-5506", "taxes", "Adjusting the state budget for the biennium ending June 30, 2023"),
    (2022, "HB-5001", "healthcare", "Children's mental health"),
    (2023, "HB-6941", "taxes", "State budget for the biennium ending June 30, 2025"),
    (2023, "HB-6667", "guns", "Addressing gun violence"),
    (2023, "SB-1", "education", "Transparency in education"),
    (2024, "SB-1", "healthcare", "The health and safety of Connecticut residents"),
    (2024, "HB-5005", "economy", "Expanding paid sick days in the state"),
    (2025, "HB-7287", "taxes", "State budget for the biennium ending June 30, 2027"),
    (2025, "SB-1", "education", "Increasing resources for students, schools and special education"),
    (2025, "HB-5002", "economy", "Housing and the needs of homeless persons"),
    (2026, "HB-5043", "guns", "Convertible pistols, unfinished frames or unfinished lower receivers, and voluntary relinquishment"),
    (2026, "SB-397", "immigration", "Democracy and government accountability, and the use and retention of automated license plate reader data"),
    (2026, "HB-5001", "other", "Absentee voting for all and other reforms related to the administration of elections"),
]

# Where a bill's official title does not say why it sits under a topic, a sourced note explains it.
NOTES = {
    (2026, "SB-397"): ("Listed under immigration because, as passed by the Senate, it also bars civil immigration arrests at schools, hospitals and churches without a judicial warrant and restricts ICE use of license plate reader data.",
                       "WFSB: Connecticut Senate passes bill limiting immigration enforcement", "https://www.wfsb.com/2026/04/14/lawmakers-debate-bill-limiting-immigration-enforcement/"),
}

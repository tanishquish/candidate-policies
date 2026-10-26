# Candidate Policies

A static website for the 2026 U.S. midterms. Pick a state on the map, choose a race from the district grid
(or look up districts by ZIP code), compare the candidates side by side, then open a candidate for their
positions, plans of action and past statements. Every statement carries a superscript link to its source, and
every direct quote is itself a link to the page it came from.

Connecticut is complete for the governor, the other statewide offices, the five U.S. House districts and all
36 State Senate districts. Other states show "coming soon".

## Run
```
python3 -m http.server 8000
```
Open http://localhost:8000. No build step or install is needed for the site itself. The map loads two small
libraries from the jsDelivr CDN (a pinned `topojson-client` with an integrity hash, and a pinned `us-atlas`
data file), so it needs an internet connection.

## Compare Candidates agent
Race pages with two or more candidates have a **Compare Candidates** button. It needs an Anthropic API key and
the bundled server, which replaces `http.server`:
```
ANTHROPIC_API_KEY=your-key python3 tools/serve.py
```
The key is read from the environment on your computer and is never sent to the page. Set `COMPARE_MODEL` to
change the model and `PORT` to change the port. Without a key the rest of the site works and the button explains
what is missing.

The agent sees only the cited overview, positions, plans and past statements for that race. Every point it
returns must reference those facts, and the server drops any point that does not, so each superscript opens a
vetted source. The output is AI-generated and can still be wrong, which the page says.

## Data workflow
`data/candidates.json` is generated; edit the Python sources instead.

| File | Purpose |
|---|---|
| `tools/build_data.py` | Main build. Defines the governor and U.S. House candidates, photo captions, then calls the modules below |
| `tools/plans.py` | "Plan of action" entries for the original 15 candidates |
| `tools/extra_candidates.py` | Other statewide offices and State Senate candidates (lists, websites, optional survey quote) |
| `tools/state_research.py`, `research_a` to `research_f.py` | Positions, plans and statements researched per candidate |
| `tools/social_links.json` | Website and social media links (from each candidate's site and Ballotpedia) |
| `tools/rendered/` | Text of JavaScript-loaded news pages, copied from a browser so quotes can be checked |
| `data/zip_districts.json` | Connecticut ZIP area to district lookup, built from U.S. Census relationship files |

```
python3 tools/build_data.py      # regenerate data/candidates.json
python3 tools/lint_data.py       # structural checks (no network)
python3 tools/verify_quotes.py   # re-fetch every cited page and confirm each direct quote appears
```
`verify_quotes.py` skips pages that show a bot check instead of failing; re-run later or check those by hand.

## Rules the data follows
- Nothing is invented. Positions come from a candidate's own website where possible, otherwise from dated,
  linked sources (news, official press releases, Ballotpedia surveys the candidate wrote).
- Statements from outside the candidate's website are limited to the past five years and show their context.
- A topic with nothing found says so instead of guessing.
- Photos come from the candidate's own website (or a public social profile) and are hotlinked, except one saved locally.
- Profiles marked "in progress" have not had their positions reviewed yet.

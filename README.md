# Candidate Policies

A static website for the 2026 U.S. midterms: pick your state, see who is running (name, party, photo), open a candidate for an overview of their policies and values, then drill into topics (abortion, LGBTQ+ rights, taxes, defense, …).

## Run
```
python3 -m http.server 8000
```
Open http://localhost:8000.

## Data
- `data/candidates.json` – candidates (schema described in the file). Photos should link to the candidate's own website; every topic summary should cite sources.
- `data/topics.json` – topic list.
- `data/states.json` – states.

## Connecticut data workflow
- `tools/build_data.py` is the source of truth; it writes `data/candidates.json`.
- `tools/verify_quotes.py` re-fetches each cited page and confirms every direct quote appears there.
- The map loads `us-atlas` and `topojson-client` from the jsDelivr CDN at runtime.

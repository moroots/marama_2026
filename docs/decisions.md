# Decisions (from the author, 2026-11-02)

- **Organization:** Mid-Atlantic Regional Air Management Association (MARAMA).
- **Format:** 4 sessions x 90 min = ~30 min lecture / ~30 min hands-on / ~30 min buffer (questions, discussion, interruptions). Live, with some virtual attendees. Bring your own laptop.
- **Audience:** comfortable with math; not proficient in Python; likely OK in Excel or R.
- **Environment:** every notebook must run in **both Google Colab and a local install**.
- **Tooling:** a mix of `atmoz` (data access) and hand-crafted code (analysis, so people learn the mechanics).
- **Source material:** prior bootcamp is *inspiration*, not drop-in. Weeks 6 and 8 never happened (course issues).
- **Data:** small pre-packaged subsets; no live downloads or accounts required in-session.

## Round 2 (2026-11-02)
- **Add pyrsig** (EPA RSIG client) alongside `atmoz` as a data-access tool.
- **Session 1 stance:** *reading* Python is the priority skill (especially in the AI era): read, predict, run, modify, verify. Writing from scratch is secondary.
- **Helpers:** two TAs/helpers during hands-on blocks.
- **Compliance depth (Session 2) and Session 3 hero dataset:** delegated to research; see `docs/research-notes.md` for the recommendation.

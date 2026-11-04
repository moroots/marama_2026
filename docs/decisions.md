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

## Round 3 (2026-11-02)
- **Session 3 episode:** June 2025. TEMPO continues, so it is safe to teach with.
- **pyrsig prototype:** approved and run; AirNow, AQS, and TEMPO L3 all retrieve without credentials (see `research-notes.md`).
- **AI-assistant mini-segment in Session 1:** keep. Attendees "should know."
- **Audience lens:** design for what state/local agency staff and managers actually do; see `docs/audience-needs.md`.

## Round 4 (2026-11-04)
- **Delivery platform: Google Colab.** Primary for all four sessions; local install (conda/`uv`) remains the documented backup. No hosted JupyterHub.
- **Consequence:** Colab must be able to fetch the notebooks and data. The repo currently lives on a private Tailscale host, so a public mirror (or other public hosting) is required. Open decision.
- **Consequence:** every notebook needs a first "setup" cell that detects Colab, installs missing packages (`pyrsig`, `atmoz`, `cartopy`), and fetches bundled data from a public URL.
- **Python version:** support 3.11 and 3.12 only (3.10 and older are deprecated). Recommend and test **3.12**; `pyrsig` is vetted only on 3.12. All local-install commands pin 3.12.

## Round 5 (2026-11-04): Teaching design for the "Before the Course" guide
Based on a review of *Teaching Tech Together* (Wilson), Carpentries guidance, and Knowles (evidence quality is mixed; see the memory note). The user approved all eight changes:
1. Lead with job-relevant outcomes (design value, TEMPO overlay, one-command rerun, reading AI code), not chores.
2. Setup notebook should end with a first win: a plot of real ozone data. **[BUILD, needs bundled data]**
3. Practice the signature skill pre-course: a read-predict-run-change-check warm-up with a planted AI bug.
4. Three paths: never coded / Excel or R / already writes Python.
5. Colab-first front page; local installs moved to an appendix; 15 minutes of setup help scheduled at the start of Session 1, plus an optional drop-in clinic.
6. Replace 4.5-hour generic videos with short, session-tied items; long videos move to "after the course".
7. Bring one real task (non-confidential); used in discussion time and as the start of the Session 4 automation exercise.
8. Make the career boost visible: take-home episode-report notebook, manager one-pager, supervisor note, between-session 15-minute micro-tasks. **[BUILD]**
- **Language:** avoid "just", "easy", "simple" in learner-facing text.
- **Lesson-plan follow-ups (not yet applied):** 15-minute setup block in Session 1; Excel/R translation table; stretch task per exercise; episode-report deliverable in Session 4; micro-tasks; decide whether the three-year design value is a core outcome or a stretch.

## Round 6 (2026-11-04): Notebook exercise design (from the user's review of the V3 prototype)
- **Attendees write real code.** Fill-in-a-token blanks (`sep="___"`) are not enough. "Write it" cells ask for whole lines, loops and tables, with scaffolding that fades as the notebook goes on (first exercises give most of the line, later ones give only the goal).
- **Checks look at results, not text.** `check()` examines what the attendee's code produced (shapes, values, line counts), so many different correct answers pass, and no answer is visible in the cell.
- **Predictions must be reasoned, not guessed numbers.** Use yes/no or multiple-choice calls, locked in before the code runs. Dropped: guessing counts such as the number of missing values (the attendee now *writes the code that counts them*).
- **Helper plumbing is not in the notebook.** `check`, `lock`, `reveal` and `scorecard` live in `marama_helpers.py` next to the notebook; the notebook has one import line. On Colab the file must be uploaded alongside the data (public hosting is out of scope for now).
- **Note:** this adds more writing than the Session 1 "reading first" stance. The balance between reading and writing needs to be settled in the lesson plan.

## Round 7 (2026-11-04): Rebuilt PM2.5 notebook for a live room of 30 plus 150 virtual
- **Not a Session 1 notebook.** Likely Session 2 or later (which session is still to be settled). Staffing: the instructor plus two student helpers.
- **Three self-contained blocks** (A: clean table, B: plot it, C: regulatory question). Blocks B and C open with a **checkpoint cell** (`load_clean_table`) so anyone who is stuck or arrives late can join cleanly.
- **Payoff first.** Opens with the alarming June plot and a locked-in yes/no prediction that is resolved at the end of Block C.
- **Fewer, better-faded writing exercises.** 14 write cells (was 18): worked example, then a similar write. Three optional ⭐ stretch cells.
- **Self-service for a high attendee-to-helper ratio:** tiered hints, checkpoints, and a chat convention (✅ finished a block, ❓ stuck or used a checkpoint).
- **Virtual-friendly:** "neighbor" prompts also say what to do in chat; four prompts are marked as live polls.
- **Reading AI-written code:** an exercise where an AI-written completeness rule (`> 18`) is tested against ours (`>= 18`).
- **Fewer colors:** blue (goal, why), orange (write, stretch), purple (discuss, poll), red (watch out).

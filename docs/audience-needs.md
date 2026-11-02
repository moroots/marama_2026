# What agency staff and managers need from Python (working analysis)

**Status: my inference, not researched with MARAMA members. Author to correct.**

## Who is in the room (assumed)
1. **Analysts / monitoring staff:** produce seasonal summaries, design values, exceedance lists; now do it in Excel/SAS/R/Access.
2. **Planners / modelers (SIP, attainment demos):** pair monitors with models and met; make maps and figures.
3. **Managers / supervisors:** don't write code daily but *approve, review, and defend* analyses done by staff, contractors, or now AI tools.

## Recurring agency jobs Python can plausibly help with
- Pull AirNow/AQS data without manual downloads; refresh each season.
- Ozone/PM2.5 season summaries: MDA8, exceedance days, 4th-highest, design values, trends.
- Event analysis (wildfire smoke, ozone transport, exceptional-events support): event vs typical days, maps, satellite context.
- Monitor-vs-model or monitor-vs-satellite comparisons; maps for reports and public/legislative questions.
- Replace fragile Excel macros / copy-paste workflows with something repeatable and checkable.
- Review and QA of other people's (or an AI's) analysis.

## What that implies they must *learn* (priority order)
1. **Read and review code:** know the inputs, units, time zone, filters, missing-data handling, and aggregation in a script. (Matches your "reading Python" priority.)
2. **Excel/R-to-pandas mental model:** tables, filters, groupby, pivots; where Python is better and where Excel is fine.
3. **Get data programmatically** (`atmoz`, `pyrsig`) and keep a record of exactly what was pulled.
4. **Compute regulatory-flavored metrics correctly** and know the limits of a teaching implementation vs an official determination.
5. **Make clean, defensible figures** for reports.
6. **Repeatability:** same script, same answer next season; documented inputs; basic version control.
7. **Know what to ask for:** scope a task for staff/contractors/AI; sanity-check results.

## Practical constraints to design around
- Locked-down agency laptops (no admin rights, restricted installs, firewalls to external data services) -> Colab and bundled data are the safety net; document a no-install path.
- Agency policies on cloud tools and AI assistants vary; don't assume permission to upload data to external services. All tutorial data is public.
- Mixed skill levels and attention: managers may attend for the "reading and judging" content more than hands-on coding.

## Proposed changes to the lesson plan (NOT yet applied; for author decision)
1. **Reviewer's checklist handout** (one page, used in all four sessions): inputs? units? time zone? filters? missing data? aggregation? rounding? Does the number match a known check?
2. **Excel/R crosswalk cheat sheet** (VLOOKUP/pivot/filter/AVERAGEIF to pandas).
3. **Session 3: reframe the episode as an event analysis** (June 2025): event days vs typical days in AQS/AirNow, with TEMPO NO2/HCHO context. It mirrors real exceptional-events/episode work, not just a pretty map.
4. **Session 4 capstone = "ozone season summary for every site"**: the deliverable agencies produce every year (fetch from AQS, MDA8, 4th-highest, figure per site, one summary table), run with one command.
5. **A "no-install / locked-down laptop" path** documented and tested (Colab only).
6. **Manager track within each hands-on:** a short "review this analysis" task for people who don't want to code (find the issue in a provided notebook).

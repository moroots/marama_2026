# Lesson plan (v0, draft for author review)

Format per session: 90 min = **0:00-0:30 lecture/live-code, 0:30-1:00 hands-on, 1:00-1:30 buffer**.
Running dataset (working assumption, not yet chosen): Mid-Atlantic hourly ozone + PM2.5 from AQS/AirNow for one summer, centered on a notable event (e.g. June 2023 Canadian wildfire smoke).
**Teaching stance: read first.** Attendees can already lean on AI assistants to *write* code; the scarce skill is *reading* code well enough to know what it does, run it, change it, and catch when it's wrong. Every session therefore trains a loop: **read -> predict -> run -> modify -> verify**.
Tools: `atmoz` and `pyrsig` for *getting* data (shown as readable recipes, with bundled data as the safety net); hand-crafted pandas/xarray/matplotlib for *analysis*.
Staffing: instructor + **two helpers** (one in-room, one covering virtual attendees / chat).
Conventions: **[Demo]** instructor live-codes; **[Do]** attendees type; **[Check]** quick question to the room (and virtual chat); **Cut** = drop first if behind.

---
## Session 1: Overview of Python and Simple Statistics

**Learning objectives.** By the end, attendees can:
1. Open and run a notebook (Colab or local) and explain cell vs. kernel.
2. **Read** a short block of Python and say in plain English what each line does (variables, lists/dicts, loops, functions, indexing, method chains).
3. **Predict** a snippet's output, then run it to check.
4. Load an air quality CSV into a pandas DataFrame; filter, and compute mean, median, percentiles, counts, and grouped summaries.
5. **Modify** working code to ask a new question (new site, threshold, percentile).
6. **Sanity-check** a result (row counts, units, plausible range), including code written by a colleague or an AI assistant.

**Prerequisite.** `00_setup_check` run before the session (emailed 1 week ahead).

### Run of show
| Time | Segment | Detail |
|------|---------|--------|
| 0:00-0:05 | Orientation | Who we are; Excel/R to Python mapping (column = Series, sheet = DataFrame, filter = boolean mask). Confirm everyone's notebook runs. **[Check]** Colab vs local? |
| 0:05-0:12 | How to read Python | **[Demo]** one 15-line annotated snippet read aloud line-by-line: variables, list/dict, `for` over sites, a small function (ppm to ppb), `df[...]`, a method chain. Rule of thumb: read top to bottom, name the inputs, name the output. **[Check]** "What does this print?" before running |
| 0:12-0:20 | First data + data-access recipes | **[Demo]** `pd.read_csv`; `.head()`, `.shape`, `.dtypes`, `.describe()`. Then *read* (not run) short `atmoz` and `pyrsig` fetch snippets: find the site, pollutant, dates, bbox. Switch to bundled CSV for everything after |
| 0:20-0:30 | Summarize | **[Demo]** boolean filter, `.mean()`, `.median()`, `.quantile()`, `.groupby("site").agg(...)`. **[Check]** "Why is mean > median here?" (right skew) |
| 0:30-1:00 | Hands-on | Exercise 1 below; two helpers circulate; one covers virtual attendees in chat/breakout |
| 1:00-1:30 | Buffer | Q&A, setup rescue. **Mini-segment (10 min):** working with an AI assistant: give it context, ask it to explain each line, test on a case where you know the answer, check units/time zones, follow your agency's data policy. **Stretch:** correlation, `scipy.stats.linregress`; R², RMSE, bias |

### Hands-on: Exercise 1 ("Read, predict, modify")
- **Part A, read and predict (10 min):** four short snippets; write the predicted output, run to check.
- **Part B, modify (10 min):** given working code that summarizes one site, change it to (i) another site, (ii) the 95th percentile, (iii) hours above 70 ppb.
- **Part C, spot the bug (10 min):** an "AI-generated" snippet with a planted flaw (e.g. mean where it should be max; ppm/ppb mix-up; wrong column). Find it using sanity checks.
- *Challenge:* summarize every site in one `groupby`.
Solutions released afterwards.

### Likely stumbling blocks
- Kernel not restarted / cells out of order -> teach "Restart & Run All" early.
- Column-name case/whitespace; units (ppm vs ppb).
- `=` vs `==`.
- Colab reset losing files -> setup cell re-fetches.

### Cut list
Function demo, live `atmoz`/`pyrsig` reading, stretch regression, AI mini-segment (move to Session 4 buffer).
---
## Session 2: Data Analysis Techniques and Simple Plotting

**Learning objectives.** Attendees can:
1. Parse timestamps, set a datetime index, and handle time zones (UTC vs local standard time).
2. Resample hourly data to daily/monthly and explain the aggregation choice.
3. Identify missing values and flagged data, and say what the handling does to a statistic.
4. Compute a rolling 8-hour mean and daily MDA8 **with a validity rule**, then find the annual 4th-highest MDA8.
5. Explain how a design value is built (4th-highest MDA8, averaged over 3 years, plus completeness) and reproduce it from a small multi-year file.
6. Build a labeled, readable matplotlib figure (fig/ax, dates on axis, threshold line, subplots).

### Compliance depth (decided from research)
Teach the **mechanics, in code**, as far as a monitor-level design value:
- MDA8 per day; a day is valid if >=13 of the 17 8-hour periods (starting 7:00 to 23:00 local) are valid, *or* the MDA8 exceeds the standard.
- Annual 4th-highest MDA8; 3-year average = design value, compared to 70 ppb.
- Name (do not implement) the completeness test: >=90% of monitoring-season days on average over 3 years, >=75% in any single year; a DV above the standard is always valid.
Not covered: rounding/truncation conventions, exceptional-events exclusions, area-level design values. Say so explicitly and point to 40 CFR 50 Appendix U. This is a teaching aid, not an official determination.

### Run of show
| Time | Segment | Detail |
|------|---------|--------|
| 0:00-0:03 | Recap | One Session 1 answer; show today's goal figure |
| 0:03-0:10 | Time handling | **[Demo]** `pd.to_datetime`, `set_index`, `tz_convert`; why local standard time matters for daily metrics |
| 0:10-0:16 | Missing data and resampling | **[Demo]** `isna().sum()`, `.resample("D").mean()`, `min_count`. **[Check]** "Report a daily mean with 12 of 24 hours?" |
| 0:16-0:26 | MDA8 and 4th-highest | **[Demo]** `rolling(8)`, daily max, 13-of-17 validity, `nlargest(4)` per year; compare against `atmoz` output as a cross-check (verification habit from Session 1) |
| 0:26-0:30 | Plot anatomy | **[Demo]** `fig, ax = plt.subplots()`, labels, `axhline`, date formatter, save |
| 0:30-1:00 | Hands-on | Exercise 2 |
| 1:00-1:30 | Buffer | Q&A. **Stretch:** 3-year design value from the multi-year file; seaborn boxplots; diurnal profile |

### Hands-on: Exercise 2 ("Season at a glance")
1. Daily MDA8 (with validity) for two sites over one summer.
2. Plot both with the 70 ppb line; mark exceedance days.
3. Title, labeled axes with units, legend; save PNG.
4. Print each site's annual 4th-highest MDA8.
5. *Challenge:* three-year design value for one site; two-panel figure with PM2.5 below, event shaded.

### Likely stumbling blocks
- Rolling-window alignment (trailing vs centered; hour-beginning vs hour-ending).
- Mixed time zones, DST.
- `.resample(...)` without an aggregation.
- `plt.plot` vs object-oriented API.

### Cut list
Time-zone deep dive, seaborn, design-value stretch.

### To verify before teaching
Valid 8-hour average rule (how many hours needed), rounding/truncation of MDA8, and 8-hour period labeling convention, all from the current Appendix U text and EPA's guidance.

> **Data need:** 3 summers of hourly ozone for 2-3 Mid-Atlantic sites (small CSV).
---
## Session 3: Python Tools for Atmospheric Science

**Learning objectives.** Attendees can:
1. Choose a tool for a given data source/file type (CSV: pandas; NetCDF: xarray; HDF: h5py/pyhdf; data services: `atmoz`, `pyrsig`).
2. Read a `pyrsig` request (dataset key, bounding box, dates) and say what comes back.
3. Open a NetCDF/xarray Dataset and describe dims, coords, variables, attributes.
4. Subset by time/region and compute a mean.
5. Plot a gridded satellite field on a cartopy map and overlay monitor observations on the same color scale.

### Hero dataset (recommendation, pending your OK)
**TEMPO satellite NO2 (or HCHO) vs AirNow monitors for a summer ozone episode**, retrieved with `pyrsig`. Reasons: it is the new tool agencies are actively being trained on; `pyrsig` is built for exactly this pairing (its gallery has an "AirNow vs TEMPO" example); and it connects to the Session 1-2 ozone story (NO2/HCHO are ozone precursors). The June 2023 smoke event predates usable TEMPO data, so pick an episode inside the TEMPO record (e.g. June 2025, which your TOLNet/HUBC material already covers). PM2.5 NetCDF from your old course can remain a stretch/alternative.
Risk to test first: whether TEMPO via `pyrsig` needs credentials, and how big the subset is.

### Run of show
| Time | Segment | Detail |
|------|---------|--------|
| 0:00-0:05 | Recap, ecosystem map | Which tool for which source; surface data = tables, satellite/model = N-D arrays |
| 0:05-0:12 | pyrsig | **[Demo]** read a request (bbox, dates, dataset key); show data arriving as DataFrame (point data) and as gridded dataset; `atmoz` vs `pyrsig`: when to use which |
| 0:12-0:20 | xarray | **[Demo]** open, print Dataset, `.sel`, `.mean("time")`, attributes/units |
| 0:20-0:28 | Maps | **[Demo]** cartopy `PlateCarree`, coastlines, states, `pcolormesh`, colorbar; `transform=` vs `projection=` |
| 0:28-0:30 | Combine | scatter AirNow monitors on the same axes, same color scale |
| 0:30-1:00 | Hands-on | Exercise 3 |
| 1:00-1:30 | Buffer | Q&A. **Stretch:** HDF read; TOLNet lidar curtain; ERA5 winds |

### Hands-on: Exercise 3 ("Satellite meets monitor")
1. Open the bundled TEMPO subset; list variables and dims.
2. Select the episode window; compute a mean; map over the Mid-Atlantic with state borders.
3. Overlay AirNow monitor values on the same color scale.
4. *Challenge:* episode minus baseline difference map.

### Likely stumbling blocks
- Lon 0-360 vs -180-180; lat ordering in slices.
- Forgetting `transform=ccrs.PlateCarree()`.
- Cartopy install locally (Colab fine); provide tested conda path.
- `pyrsig` needs `pandas<3`, so pin the environment.
- Network/server availability during a live session -> bundled fallback is mandatory.

### Cut list
Overlay step, all stretch items.

> **Dependency:** small gridded subset cut in advance (a few MB if possible).
---

## Session 4: Analysis Workflows and Pipelines

**Learning objectives.** Attendees can:
1. Turn repeated notebook code into a function with parameters and a docstring.
2. Loop over many sites/files with `pathlib` and collect outputs into one table.
3. Save and reuse intermediate results (parquet/CSV) instead of recomputing.
4. Describe how to make an analysis reproducible (environment file, fixed inputs, version control).
5. Run a script from the command line that produces figures and a summary table.

### Run of show
| Time | Segment | Detail |
|------|---------|--------|
| 0:00-0:05 | Recap, motivation | The "final_v3_REAL.ipynb" problem; the goal of today: run one command, get all outputs |
| 0:05-0:12 | Notebook to function | **[Demo]** take Session 2 figure cells, wrap as `plot_season(site, df, out_dir)`; parameters not hard-coded paths |
| 0:12-0:20 | Batch | **[Demo]** a `fetch -> cache -> analyze` pattern (`atmoz`/`pyrsig` fetch with bundled-file fallback); `Path.glob`, loop over sites, collect summary rows into a DataFrame, write CSV; simple `try/except` so one bad site doesn't stop the run |
| 0:20-0:26 | Scripts and CLI | **[Demo]** move into `analysis.py` with `argparse` (site list, year, output dir); run from terminal/`!python` in Colab |
| 0:26-0:30 | Reproducibility | Environment file, pinned versions, git in one slide; where this repo lives |
| 0:30-1:00 | Hands-on | Exercise 4 below |
| 1:00-1:30 | Buffer | Discussion: "what's one task at your agency you'd automate?"; resources and next steps. **Stretch:** logging, config files (YAML), scheduling |

### Hands-on: Exercise 4 ("One command")
1. Given a half-finished `pipeline.py`, finish the function that computes MDA8 exceedance counts for a site.
2. Run it across all bundled sites; produce `summary.csv` and one PNG per site.
3. *Challenge:* add a `--threshold` argument and rerun at 65 ppb.

### Likely stumbling blocks
- Relative paths differ between Colab and local -> use a project-root helper.
- Terminal vs. notebook confusion for first-time CLI users.
- Over-engineering; keep it to one script and one function.

### Cut list
`argparse` (just run a function in a loop), git slide.

---

## Cross-cutting
- **Attendee materials:** student notebook (blanks), solutions notebook released after, one-page cheat sheet per session (pandas, matplotlib, xarray/cartopy).
- **Virtual attendees:** a designated chat monitor/TA; every **[Check]** gets a chat poll; notebooks shared by link, not screen only.
- **Pacing safeguard:** a "checkpoint cell" at the start of each hands-on that loads the right state, so anyone behind can catch up.
- **Assessment:** none formal; the exercise is the check. Optional end-of-series feedback form.

## Open design questions
1. Confirm Session 3 hero: TEMPO NO2/HCHO vs AirNow via `pyrsig` (and which episode?).
2. Confirm Session 2 depth: monitor-level design value in code; completeness only named.
3. Handouts and cheat sheets in scope? (I'd include one page per session.)
4. Agency AI-use policies vary; is the Session 1 AI mini-segment appropriate for this audience?

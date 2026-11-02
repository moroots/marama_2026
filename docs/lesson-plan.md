# Lesson plan (v0, draft for author review)

Format per session: 90 min = **0:00-0:30 lecture/live-code, 0:30-1:00 hands-on, 1:00-1:30 buffer**.
Running dataset (working assumption, not yet chosen): Mid-Atlantic hourly ozone + PM2.5 from AQS/AirNow for one summer, centered on a notable event (e.g. June 2023 Canadian wildfire smoke).
Conventions: **[Demo]** instructor live-codes; **[Do]** attendees type; **[Check]** quick question to the room (and virtual chat); **Cut** = drop first if behind.

---

## Session 1: Overview of Python and Simple Statistics

**Learning objectives.** By the end, attendees can:
1. Open and run a notebook (Colab or local) and explain cell vs. kernel.
2. Read an air quality CSV into a pandas DataFrame and describe its shape, columns, and types.
3. Select rows/columns and filter by condition (site, parameter, threshold).
4. Compute and interpret mean, median, percentiles, counts, and grouped summaries.
5. Say why the mean can mislead for skewed pollutant data.

**Prerequisite.** `00_setup_check` run before the session (emailed 1 week ahead).

### Run of show
| Time | Segment | Detail |
|------|---------|--------|
| 0:00-0:05 | Orientation | Who we are, what we'll do; "Excel/R to Python" mapping slide (column = Series, sheet = DataFrame, filter = boolean mask). Confirm everyone's notebook runs. **[Check]** hands up: Colab vs local? |
| 0:05-0:12 | Python in 7 minutes | **[Demo]** variables, numbers/strings, a list, a dict, `for` loop over sites, a 3-line function (e.g. ppm to ppb). Mention indentation. Everything else is deferred ("you'll pick it up as we go") |
| 0:12-0:20 | First data | **[Demo]** `pd.read_csv`; `.head()`, `.shape`, `.dtypes`, `.describe()`. Brief `atmoz` fetch of the same data, then use bundled CSV for the rest |
| 0:20-0:30 | Selecting and summarizing | **[Demo]** `df["col"]`, boolean filter (`df[df.site == ...]`), `.mean()`, `.median()`, `.quantile()`, `.groupby("site").agg(...)`. **[Check]** "Why is mean > median here?" (right skew, high-ozone days) |
| 0:30-1:00 | Hands-on | **[Do]** Exercise 1 below, with instructor/TA circulating; virtual attendees get a breakout/chat helper |
| 1:00-1:30 | Buffer | Q&A, setup rescue, share-outs. **Stretch (only if on time):** correlation between two sites, scatter, `scipy.stats.linregress`; R², RMSE, bias in 3 lines each |

### Hands-on: Exercise 1 ("Know your monitor")
1. Load the bundled ozone file; report rows, date range, number of sites.
2. For one site: mean, median, 95th percentile, max of the hourly ozone.
3. How many hours exceed 70 ppb? Which site has the most?
4. *Challenge:* repeat step 2 for every site in one `groupby`.
Solution notebook provided afterwards (not during).

### Likely stumbling blocks
- Kernel not restarted / cells run out of order -> teach "Restart & Run All" early.
- Case/whitespace in column names; units (ppm vs ppb).
- `=` vs `==`; `df[df.site = ...]`.
- Colab session reset losing the downloaded file -> setup cell re-fetches.

### Cut list
Function demo, `atmoz` live fetch, stretch regression.

---

## Session 2: Data Analysis Techniques and Simple Plotting

**Learning objectives.** Attendees can:
1. Parse timestamps, set a datetime index, and handle time zones (UTC vs local standard time).
2. Resample hourly data to daily/monthly and explain the aggregation choice.
3. Identify and handle missing values and flagged data, and say what the choice does to a statistic.
4. Compute a rolling 8-hour mean and daily MDA8, and count exceedance days vs. a threshold.
5. Build a labeled, readable matplotlib figure (fig/ax, dates on axis, threshold line, subplots).

### Run of show
| Time | Segment | Detail |
|------|---------|--------|
| 0:00-0:03 | Recap | One Session 1 exercise answer; today's goal figure shown up front |
| 0:03-0:10 | Time handling | **[Demo]** `pd.to_datetime`, `set_index`, `tz_localize`/`tz_convert`; why AQS "local standard time" matters for daily metrics |
| 0:10-0:18 | Missing data and resampling | **[Demo]** `isna().sum()`, `.resample("D").mean()`, `min_count`; show how 1 missing hour vs. 20 changes a daily mean. **[Check]** "Would you report a daily mean with 12 of 24 hours?" (ties to completeness criteria, no right answer asserted here) |
| 0:18-0:25 | Regulatory-style metric | **[Demo]** `rolling(8).mean()`, daily max = MDA8, compare to `atmoz` output as a check; flag exceedance days |
| 0:25-0:30 | Plot anatomy | **[Demo]** `fig, ax = plt.subplots()`; plot, labels, `axhline`, date formatter; save figure |
| 0:30-1:00 | Hands-on | Exercise 2 below |
| 1:00-1:30 | Buffer | Q&A. **Stretch:** seaborn boxplots by month/site, style/colorblind-safe palettes, diurnal profile by site with `groupby(hour)` |

### Hands-on: Exercise 2 ("Season at a glance")
1. Compute daily MDA8 for two sites over the summer.
2. Plot both as lines with the 70 ppb line; mark exceedance days with markers.
3. Add title, axis labels with units, legend; save as PNG.
4. *Challenge:* two-panel figure, ozone MDA8 on top, PM2.5 daily mean below, shared x axis, event dates shaded.

### Likely stumbling blocks
- Rolling-window alignment (trailing vs. centered; hour-beginning vs. hour-ending conventions).
- Mixed time zones and DST.
- Resampling object vs. result; forgetting `.mean()`.
- `plt.plot` vs. object-oriented API confusion.

### Cut list
Time-zone deep dive (just state "use UTC or LST consistently"), seaborn, diurnal.

> **Author check:** how formal should the MDA8/NAAQS math be? A reviewer from a state agency may care about data-completeness rules (e.g. 75%). I propose teaching the mechanics and naming the completeness rules without implementing the full design value calculation.

---

## Session 3: Python Tools for Atmospheric Science

**Learning objectives.** Attendees can:
1. Choose a tool for a given file type (CSV: pandas; NetCDF: xarray; HDF: h5py/pyhdf).
2. Open a NetCDF file in xarray and describe its dimensions, coordinates, variables, and attributes.
3. Subset by time and region, and compute a time mean.
4. Plot a gridded field on a map with cartopy (projection, coastlines, state lines, colorbar).
5. Overlay monitor locations on a gridded field and make a qualitative comparison.

### Run of show
| Time | Segment | Detail |
|------|---------|--------|
| 0:00-0:05 | Recap, ecosystem map | One-slide "which tool for which file"; why surface data is 1-D tables and satellite/model data is N-D arrays |
| 0:05-0:15 | xarray | **[Demo]** `xr.open_dataset`; print the Dataset; `.sel(time=..., lat=slice, lon=slice)`; `.mean("time")`; attributes/units. Compare to a DataFrame |
| 0:15-0:25 | Maps | **[Demo]** `ccrs.PlateCarree()`, `ax.coastlines()`, `cfeature.STATES`, `pcolormesh`/`contourf`, colorbar, extent. Projection note: `transform=` vs. `projection=` (the #1 cartopy confusion) |
| 0:25-0:30 | Combine | **[Demo]** scatter monitor lat/lon on the same axes colored by observed value |
| 0:30-1:00 | Hands-on | Exercise 3 below |
| 1:00-1:30 | Buffer | Q&A. **Stretch:** HDF read with h5py; TOLNet lidar curtain; ERA5 winds as quiver on the map |

### Hands-on: Exercise 3 ("Where was the smoke?")
1. Open the bundled PM2.5 (or TEMPO O3) subset; list variables and dims.
2. Select the event week; compute its mean; plot over the Mid-Atlantic with state borders.
3. Overlay monitor PM2.5 averaged over the same period using the same color scale.
4. *Challenge:* a before/during difference map.

### Likely stumbling blocks
- Lon 0-360 vs. -180-180; lat ordering when slicing.
- Forgetting `transform=ccrs.PlateCarree()`.
- Installing cartopy locally (Colab is fine); provide conda path, tested.
- Large files: subset is pre-cut; explain lazy loading conceptually.

### Cut list
Overlay step (do separately), all stretch items.

> **Dependency:** needs a small gridded subset chosen and cut in advance (tens of MB at most; ideally under a few MB).

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
| 0:12-0:20 | Batch | **[Demo]** `Path.glob`, loop over sites, collect summary rows into a DataFrame, write CSV; simple `try/except` so one bad site doesn't stop the run |
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
1. Do you want a TA/helper for hands-on? (affects how much troubleshooting can happen in 30 min)
2. Teach the full NAAQS design value, or only daily MDA8 and exceedances?
3. Is PM2.5 (wildfire event) the right Session 3 hero, or should it be TEMPO ozone?
4. Handouts and cheat sheets in scope?

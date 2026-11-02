# Draft outline (v1)

Each session = 90 min: **~30 lecture / ~30 hands-on / ~30 buffer** (Q&A, discussion, catch-up for virtual attendees).
Lecture is live-coding in a notebook, not slides. The buffer is real: each session has a *stretch* section that can be dropped without breaking the next session.

**Audience:** math-comfortable, new to Python, some Excel/R. Use "in Excel/R you'd..." comparisons.
**Through-line:** one Mid-Atlantic ozone/PM2.5 season story, same small dataset family across all four sessions.
**Design rules:** runs in Colab and locally (first cell detects environment and installs/fetches data); small data bundled; solutions notebooks kept separate; `atmoz` for *getting* data, hand-crafted pandas/numpy/matplotlib for *analysis*.

## Session 1: Overview of Python and Simple Statistics
Outcome: open a notebook, load an AQ file, compute and interpret summary statistics.

| Block | Min | Content |
|-------|-----|---------|
| Lecture | 30 | Why Python (vs Excel/R); notebook tour; just-enough syntax (variables, lists/dicts, a loop, a function); first pandas load of AirNow/AQS data via `atmoz` and from CSV; select/filter; mean, median, percentiles, groupby site/month |
| Hands-on | 30 | Summarize ozone for one site; count days above a threshold; compare two sites |
| Buffer | 30 | Setup troubleshooting, questions. *Stretch:* correlation and linear fit (R², RMSE, bias) between two sites |

## Session 2: Data Analysis Techniques and Simple Plotting
Outcome: raw hourly data to a defensible, readable figure.

| Block | Min | Content |
|-------|-----|---------|
| Lecture | 30 | Datetimes and time zones; resample hourly to daily; missing data and flags; rolling 8-hr average, MDA8, exceedance days (hand-crafted, with a sanity check against the atmoz result); matplotlib fig/ax model; labels, date axes, subplots |
| Hands-on | 30 | Build a season figure: daily MDA8 time series with the NAAQS line and exceedances marked; diurnal cycle by site |
| Buffer | 30 | Questions. *Stretch:* seaborn quick looks, box plots by site/month, styling |

## Session 3: Python Tools for Atmospheric Science
Outcome: know which tool opens which file, and put data on a map.

| Block | Min | Content |
|-------|-----|---------|
| Lecture | 30 | Ecosystem map (pandas / xarray / netCDF4 / h5py / cartopy / atmoz); gridded data in xarray (dims, coords, slicing, time mean) with a small PM2.5 or TEMPO subset; cartopy projections and features |
| Hands-on | 30 | Map a gridded field over the Mid-Atlantic and overlay monitor locations |
| Buffer | 30 | Questions. *Stretch:* lidar curtain (TOLNet) or ERA5 meteorology (pre-downloaded subset); HDF files |

## Session 4: Analysis Workflows and Pipelines
Outcome: turn a notebook into something repeatable and shareable.

| Block | Min | Content |
|-------|-----|---------|
| Lecture | 30 | Notebook to script to functions; `pathlib` batch over many files/sites; config/parameters; caching (parquet); reproducible environments; git basics |
| Hands-on | 30 | Refactor the Session 2 figure code into a function and run it across all sites, writing figures plus a summary table |
| Buffer | 30 | Questions, wrap-up, where to go next. *Stretch:* logging/error handling, scheduling |

## Repo layout (proposed)
```
notebooks/session1_python_stats.ipynb   (+ solutions/)
notebooks/session2_analysis_plotting.ipynb
notebooks/session3_atmos_tools.ipynb
notebooks/session4_workflows.ipynb
notebooks/00_setup_check.ipynb          # Colab/local check, data fetch
data/                                   # small subsets only
src/marama/                             # helpers reused in Session 4
environment.yml / pyproject.toml        # local install
```

## Still open
See chat.

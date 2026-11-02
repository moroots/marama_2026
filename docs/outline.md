# Draft outline (v0): for discussion, not final

**Audience assumption (to confirm):** air agency staff: modelers, planners,
monitoring and data analysts. Comfortable with Excel and maybe R/SAS, little or no Python.
**Through-line:** one running regional story (Mid-Atlantic ozone/PM2.5 season) used in all four sessions.

## Session 1: Overview of Python and Simple Statistics
Goal: leave able to open a notebook, load an AQ file, and compute summary stats.
1. Why Python for air quality work (vs Excel/R/SAS); environments (Colab / local, `uv`/conda)
2. Notebook tour; the 20% of syntax that matters (variables, lists/dicts, loops, functions)
3. Pandas first contact: load AirNow/AQS CSV, inspect, select, filter
4. Simple stats: mean/median/percentiles, counts, groupby by site/month
5. Relationships: correlation, linear fit (scipy/sklearn), R², RMSE, bias; outliers
6. Exercise: summarize ozone for one Mid-Atlantic site

## Session 2: Data Analysis Techniques and Simple Plotting
Goal: go from raw monitor data to a defensible, readable figure.
1. Datetimes, time zones, resampling (hourly→daily→monthly)
2. Missing data and QA flags; merging multiple sites/parameters
3. Regulatory-flavored calcs: rolling 8-hr avg → MDA8, NAAQS exceedance days, diurnal cycles
4. Matplotlib fundamentals (fig/ax, labels, date axes, subplots, styles)
5. Seaborn/pandas plotting for quick looks; exceedance bar/time series; box plots by site
6. Exercise: reproduce a season summary figure

## Session 3: Python Tools for Atmospheric Science
Goal: know which tool opens which file, and make a map.
1. The ecosystem map: pandas / xarray / netCDF4 / h5py / cartopy / atmoz / cdsapi
2. Gridded data: NetCDF with xarray (dims, coords, slicing, time means), e.g. PM2.5 or TEMPO O3
3. Maps with cartopy: projections, features, state borders, overlaying monitors on a grid
4. Profiles and curtains: lidar/sonde (TOLNet) as 2D/vertical data (optional)
5. Reanalysis (ERA5/cdsapi) to add meteorology; pre-downloaded subset
6. Exercise: map monitor vs satellite/model for one event

## Session 4: Analysis Workflows and Pipelines
Goal: turn a notebook into something repeatable.
1. Notebook → script → functions → small module
2. Batch processing many files/sites (`pathlib`/`glob`), caching (parquet vs pickle)
3. Parameterization/config; reproducible environments; logging/error handling
4. Version control with git; sharing with colleagues
5. Capstone: end-to-end pipeline (download → clean → compute → figure → report)
6. Where to go next; resources

## Open questions: see chat

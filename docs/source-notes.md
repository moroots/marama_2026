# Source notes: prior 9-week Python Bootcamp

Extracted (outside this repo) to `../_source/bootcamp/` from the Google Drive zip.
~475 MB of data, so it is deliberately **not** committed.

## Inventory

| Week | Topic | Format | Reuse value for MARAMA |
|------|-------|--------|------------------------|
| 1 | Python basics | `Python_Basics.ipynb` (154 cells, generic syntax: types, loops, ifs), `PythonBootCamp_1.ipynb` (pandas + ozonesonde plot), slides | Syntax is generic; condense hard. Pandas/sonde cells are a good "first real data" example. Includes PM2.5 NetCDF (~250 MB) |
| 2 | Accessing data (atmoz) | `atmoz_tutorial_surface.ipynb` (AirNow/AQS ozone, Mid-Atlantic slice, diurnal, NAAQS exceedances), `atmoz_tutorial_TOLNET.ipynb` (lidar curtains), `pythonbootcamp_W2*.ipynb` (+ answers) | **Highest value.** Surface tutorial is nearly the Session 1/2 story already. Check how stable the `atmoz` API is |
| 3 | Multidimensional data | `pythonbootcamp_W3.ipynb`: HDF (h5py, pyhdf), NetCDF (netCDF4, xarray), cartopy; TEMPO O3 (135 MB), TOLNet HDF, PM2.5 NetCDF | Core of Session 3. `pyhdf` install is painful; may swap for xarray-only paths |
| 4 & 5 | Reanalysis + stats | `pythonbootcamp_W4_W5.ipynb`: cdsapi (ERA5), xarray slicing, linear fit, R/R², correlation matrix, multi-regression, RMSE, bias, outliers | Stats half → Session 1; ERA5 → Session 3. Needs Copernicus account, so likely pre-download |
| 6 | (missing from zip) | n/a | Ask: what was covered? |
| 7 | Graphics 1 | `pythonbootcamp_W7.ipynb`: matplotlib fundamentals, subplots, styles, date tickers, markers (code only, no prose) | Session 2 plotting. Needs prose added |
| 8 | Graphics 2 | **folder empty** | Ask if there's a copy elsewhere |
| 9 | Cartopy (Dr. Kylie Hoffman) | `pythonbootcamp_W9.ipynb`: projections, features, shaded polygons, activities | Session 3 mapping. Credit the author; confirm permission to reuse |

## Observations

- Notebooks assume **Google Colab** (`google.colab.drive`) in places. Decide Colab vs local.
- Several notebooks credit other authors (Zhibo Zhang, Joshua Richards, Dr. Hoffman). Attribution/permission needed before republishing.
- Typos and Colab-only cells throughout; treat as raw material, not drop-in.
- Datasets are large. For a live session, plan on small subsets.
- Slides reference account setup (AirNow Tech, NASA Earthdata, Copernicus): fine for a 9-week course, too heavy for a short tutorial.

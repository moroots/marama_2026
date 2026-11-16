# Session 4 data

| File | What it is | Source | Window and subsetting |
|------|-----------|--------|-----------------------|
| `asos_midatlantic_june2023.parquet` | Hourly airport weather (ASOS): temperature, dew point, humidity, wind direction and speed, visibility and present-weather codes (`wxcodes`, where FU = smoke and HZ = haze) at PHL, BWI, DCA, IAD and RIC | Iowa Environmental Mesonet, `https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py`, regular hourly reports (`report_type=3`), UTC | 2023-06-05 to 2023-06-11 (the notebook's `start_date` and `end_date`); 720 rows, 144 per station; columns exactly as the server returns them (`valid` is still text). The notebook falls back to this copy when the live request fails, for example when the server answers 429 (too many requests). |
| `Boulder_8hrOzoneDF.parquet` | Daily 8-hour ozone at Boulder, Colorado, with the ENSO phase of each day | Contributed by Joshua Richards for `MARAMA_ENSO_Ozone.ipynb` | Unchanged copy, moved here from the notebook folder. |

PyRSIG's `metar.*` fields have no present-weather code, so they cannot replace this file for the smoke and haze flag.

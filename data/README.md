# Course data

Small subsets of real data. Nothing is simulated. Load them with `from marama_2026 import sample_datasets as sd`.

| Folder or file | Used in | Loader | Details |
|---|---|---|---|
| `session_2/AMP501_2420560-0.txt` | Session 2 | `sd.load_aqs_pm25()` | EPA AQS hourly PM2.5, 2025, 8 Allegheny County, PA monitors (pipe-separated text, with a junk second header row and a footer) |
| `epa_daily_pm25_2025_midatlantic.parquet` | Sessions 2 and 3 | `sd.load_epa_daily_pm25()` | EPA pre-generated daily PM2.5 file for 2025, eight Mid-Atlantic states (AQS parameter 88101) |
| `session_3/` | Session 3 | `sd.load_*()` | Eight files: model, monitors, sounding, ARM, ASOS, TEMPO, TOLNet. See [`session_3/README.md`](session_3/README.md). |
| `session_4/` | Session 4.1 | `sd.load_asos_smoke()` | Airport weather for the June 2023 smoke case study. See [`session_4/README.md`](session_4/README.md). |
| `Session_4_…/Boulder_8hrOzoneDF.parquet` | Session 4.2 | none (read next to the notebook) | Daily 8-hour ozone with ENSO phase, used by Joshua Richards' notebook. It sits beside that notebook, not in `data/`. |

The loaders read from this folder in a repository checkout. Otherwise they download the file from GitHub into `~/.cache/marama_2026` the first time.

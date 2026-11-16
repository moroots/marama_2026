# MARAMA 2026: Python for Air Quality Professionals

Four hands-on sessions for the Mid-Atlantic Regional Air Management Association (MARAMA) community. Every notebook uses real air quality data (EPA monitors, airport weather, satellite, lidar, HRRR smoke model).

> Status: draft in progress.

## Start here

1. **Get set up.** Read [Before the Course](docs/before-the-course.pdf) ([source](docs/before-the-course.md)).
2. **Open a notebook in Colab** with a button below, or read it on GitHub with the notebook link.

| Session | Notebook | Open in Colab |
|---|---|---|
| 1.1 | [Python Basics](Session_1_Overview_of_Python_and_Simple_Statistics/Session_1_1_Python_Basics.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/moroots/marama_2026/blob/main/Session_1_Overview_of_Python_and_Simple_Statistics/Session_1_1_Python_Basics.ipynb) |
| 1.2 | [Simple Statistics](Session_1_Overview_of_Python_and_Simple_Statistics/Session_1_2_Simple_Statistics.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/moroots/marama_2026/blob/main/Session_1_Overview_of_Python_and_Simple_Statistics/Session_1_2_Simple_Statistics.ipynb) |
| 2 | [Data Analysis and Plotting](Session_2_Data_Analysis_Techniques_and_Simple_Plotting/Session_2_1_Data_Analysis_and_Plotting.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/moroots/marama_2026/blob/main/Session_2_Data_Analysis_Techniques_and_Simple_Plotting/Session_2_1_Data_Analysis_and_Plotting.ipynb) |
| 3 | [Python Tools for Atmospheric Science](Session_3_Python_Tools_for_Atmospheric_Science/Session_3_1_Python_Tools_for_Atmospheric_Science.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/moroots/marama_2026/blob/main/Session_3_Python_Tools_for_Atmospheric_Science/Session_3_1_Python_Tools_for_Atmospheric_Science.ipynb) |
| 4.1 | [Smoke from the Ground and a Model (ASOS + HRRR)](Session_4_Analysis_Workflows_and_Pipelines/MARMA_ASOS_HRRR.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/moroots/marama_2026/blob/main/Session_4_Analysis_Workflows_and_Pipelines/MARMA_ASOS_HRRR.ipynb) |
| 4.2 | [Ozone and ENSO](Session_4_Analysis_Workflows_and_Pipelines/MARAMA_ENSO_Ozone.ipynb) (by Joshua Richards) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/moroots/marama_2026/blob/main/Session_4_Analysis_Workflows_and_Pipelines/MARAMA_ENSO_Ozone.ipynb) |

Each notebook ends with a button that opens the next one.

## In Colab

1. Click **Open in Colab**. Choose **Runtime → Change runtime type → Runtime Version 2026.07** (Python 3.12).
2. Run the notebook's **first code cell** ("Colab setup"). It downloads all the course files and installs what that notebook needs. Sessions 3 and 4 take a few minutes. If Colab asks to restart the session, restart and run that cell again.
3. Click the **folder icon** on the left to browse every file in the course.

Colab forgets everything when the session ends, so repeat step 2 each visit and use **File → Save a copy in Drive** to keep your work.

## On your own computer

Download the repository (green **Code** button → **Download ZIP**), unzip it, and in a terminal inside that folder run:

```bash
uv venv --python 3.12
source .venv/bin/activate              # Windows: .venv\Scripts\Activate.ps1
uv pip install -e ".[all]" jupyterlab
jupyter lab
```

Full instructions, `pip` instead of `uv`, and troubleshooting are in [Before the Course](docs/before-the-course.md). To install for one session only, use `".[session3]"` or `".[session4]"` instead of `".[all]"` (Sessions 1 and 2 need no extra).

## Data

The sample data loads with `from marama_2026 import sample_datasets as sd`, for example `sd.load_epa_daily_pm25()`. The first call downloads the file from this repository and saves it; later calls read it from disk. Every file, with its source and how it was subset, is listed in [`data/README.md`](data/README.md).

Cells marked **OPTIONAL** can fetch fresh data live (set `USE_LIVE = True`). They fall back to the sample files if the server is slow, refuses the request, or you are offline.

## What is in the repository

| Folder | Contents |
|---|---|
| `Session_*` | The notebooks, one folder per session |
| `data/` | Sample datasets, one folder per session |
| `docs/` | [Before the Course](docs/before-the-course.md) (and its PDF, built with `docs/build_pdf.py`) |
| `src/marama_2026/` | `sample_datasets.py` (data loaders) and `marama_helpers.py` (exercise checkers) |
| `extra/` | Scratch demo of the `atmoz` package. Not part of the course. |

Questions: [mroots1@umbc.edu](mailto:mroots1@umbc.edu)

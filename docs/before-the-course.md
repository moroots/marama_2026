# Before the Course

**MARAMA Python Tutorial Series, 2026**
*Python for air quality data: four 90-minute sessions*

> **Draft.** Items marked **[TBD]** are waiting on details from the instructor (Dr. Maurice Roots). Everything else was checked against the official pages linked below.

This guide has two parts. **Part A is for attendees**: what to do before Session 1. **Part B is for MARAMA organizers**: what to send, and when.

---

# Part A. For attendees

## A1. The short version

Do these five things before Session 1. They take about 20 minutes in total.

1. Sign in to a **Google account** (a personal one is fine).
2. Open the Colab practice page and **run one cell** (section A4).
3. *Optional but recommended:* install Python on your own computer as a backup (section A5).
4. Skim the one-page "what to expect" (section A3).
5. Bring a **laptop, charger and a mouse if you like one**. A phone or tablet will not work for the hands-on parts.

If step 2 works, you are ready. Everything else is optional.

## A2. What the course is, and who it is for

- **Four sessions, 90 minutes each.** About 30 minutes of instruction, 30 minutes of hands-on work, and 30 minutes of discussion and questions.
- **Live, with some people joining virtually.** Helpers are available during hands-on time. Virtual attendees can ask for help in chat.
- **The sessions:**
  1. Overview of Python and simple statistics
  2. Data analysis techniques and simple plotting
  3. Python tools for atmospheric science
  4. Analysis workflows and pipelines
- **Who it is for.** Air quality staff and managers who are comfortable with numbers and may use Excel or R, but who are **not expected to know Python**. You do not need to have written any code before.
- **The main skill we teach is reading Python.** Today a lot of code is written with AI assistants. The most useful skill is looking at a script and telling what it does, what it will produce, and whether it is right. You will practice reading, predicting, running and changing code before you write much of your own.

### What you should already know
- Basic statistics: mean, median, percentiles, standard deviation.
- What a time series and a data table are.
- A rough sense of ozone and the 8-hour standard helps for Session 2, but we explain it.

You do **not** need to know Python, programming, the command line, or Git.

## A3. What to expect in a session

| Time | What happens |
|---|---|
| About 30 min | **Live coding.** The instructor walks through examples on screen. You follow along, or just watch. |
| About 30 min | **Hands-on.** You work through a short exercise in your notebook. Helpers circulate. |
| About 30 min | **Discussion and questions.** Interrupting is welcome. |

- Notebooks are **Jupyter notebooks**: documents that mix text and code cells. You press **Shift+Enter** to run a cell.
- Data is **small and pre-packaged**. You will not need accounts, API keys or big downloads during class.
- **Solutions are shared after each session**, so you can fall behind in class and catch up later.
- It is fine to get stuck. Getting stuck on purpose, then reading the error message, is part of the plan.

## A4. Primary route: Google Colab (no installation)

**Colab** is a free service from Google that runs Python notebooks in your web browser. We use it for all four sessions because it needs nothing installed and works the same on Windows, Mac and Linux.

**You need:** a Google account, a current browser (Chrome, Edge, Firefox or Safari), and an internet connection.

**Check it works:**
1. Go to [colab.research.google.com](https://colab.research.google.com) and sign in.
2. Choose **File → New notebook**.
3. In the first cell, type `print("Hello, MARAMA")` and press **Shift+Enter**.
4. You should see `Hello, MARAMA` appear under the cell.
5. In a new cell, run the next line. It confirms that the libraries we use in class are present.

```python
import numpy, pandas, matplotlib
print(numpy.__version__, pandas.__version__, matplotlib.__version__)
```

If you see three version numbers, you are ready.

**Things to know about Colab:**
- Each session you open starts with a **fresh computer**. Anything you installed or downloaded disappears when the session ends. Our notebooks have a first "setup" cell that reinstalls what they need. Run it every time.
- Colab can disconnect after a period of inactivity. If it does, choose **Runtime → Run all**, or re-run the setup cell and carry on.
- Save your own copy with **File → Save a copy in Drive** so your edits are kept.
- **If your organization blocks Google sign-in or Colab,** use the local install in section A5 and tell the organizer in advance.

**Notebook links.** You will receive the notebook links by email before Session 1. **[TBD: instructor to confirm when and how.]**

**Optional first look.** Google's own [Overview of Colaboratory Features](https://colab.research.google.com/notebooks/basic_features_overview.ipynb) is a short notebook that shows how cells, text, and running code work.

## A5. Backup route: run Python on your own computer

Do this if you want to work offline, if Colab is blocked at your organization, or if you want to keep using Python after the course. **It is optional.** Pick **one** of the three methods below. If you are unsure, use **Method 1 (Miniconda)**.

### What you are installing

| Package | What it is for |
|---|---|
| `numpy`, `pandas` | numbers and data tables |
| `matplotlib` | plots |
| `scipy` | statistics |
| `xarray`, `netCDF4` | gridded data such as satellite and model files |
| `cartopy` | maps |
| `pyrsig` | downloading EPA RSIG data (AirNow, AQS, TEMPO) |
| `atmoz` | atmospheric science tools used in Session 3 |
| `jupyterlab` | the notebook interface |

Python version: **3.12 is the safest choice.** Several of these packages now need Python 3.11 or newer. Python 3.9 and 3.10 will not work. *[Instructor: confirm the version I tested before sending. I have not tested 3.14 with cartopy.]*

> **Windows tip:** after installing, use the program called **Anaconda Prompt** (Method 1) or **PowerShell** (Methods 2 and 3). On Mac and Linux, use **Terminal**.

### Method 1 (recommended): Miniconda

Miniconda installs Python and a package manager called `conda`. It is the easiest route for map and satellite-data packages because `conda` handles the hard-to-install parts.

1. Download and install Miniconda for your operating system from the official guide: [Miniconda installation](https://www.anaconda.com/docs/getting-started/miniconda/install/overview). Use the graphical installer unless you are comfortable with a terminal.
2. Open **Anaconda Prompt** (Windows) or **Terminal** (Mac/Linux).
3. Create an environment for the course. An environment is a separate folder of packages, so nothing you do here can break other software.

```bash
conda create -n marama python=3.12
conda activate marama
```

4. Install the packages.

```bash
conda install -c conda-forge numpy "pandas<3" matplotlib scipy xarray netcdf4 cartopy jupyterlab git
pip install pyrsig
pip install git+https://github.com/moroots/atmoz
```

   `pyrsig` currently needs `pandas<3`, which is why the version is limited.
   `git` is included in the first command because the `atmoz` install pulls code from GitHub.

5. Start the notebook interface and test it.

```bash
jupyter lab
```

   Your browser opens. Create a new Python notebook and run the check from section A6.

**Next time:** open Anaconda Prompt or Terminal, run `conda activate marama`, then `jupyter lab`.

Official references: [conda getting started](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html), [Miniconda installers](https://docs.conda.io/projects/miniconda).

### Method 2: uv

`uv` is a newer, very fast Python tool that installs Python itself and your packages. It works well if you are comfortable with a terminal. Geospatial packages usually install smoothly from wheels, but if `cartopy` fails, use Method 1.

1. Install `uv` using the [official installation page](https://docs.astral.sh/uv/getting-started/installation/).
   - **Mac / Linux:** `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - **Windows (PowerShell):** `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
   - Close and reopen your terminal afterward.
2. Create a project folder and environment.

```bash
mkdir marama && cd marama
uv venv --python 3.12
```

3. Activate it.
   - **Mac / Linux:** `source .venv/bin/activate`
   - **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
4. Install the packages. You need **Git** installed for the `atmoz` line ([git-scm.com](https://git-scm.com/downloads)).

```bash
uv pip install numpy "pandas<3" matplotlib scipy xarray netcdf4 cartopy pyrsig jupyterlab
uv pip install git+https://github.com/moroots/atmoz
```

5. Start the notebook interface: `jupyter lab`

### Method 3: Python's standard tools (`venv` and `pip`)

This uses only what comes with Python. It is the most universal and the most manual.

1. Install Python 3.12 from [python.org/downloads](https://www.python.org/downloads/). **On Windows, tick "Add python.exe to PATH" on the first screen of the installer.** Install [Git](https://git-scm.com/downloads) too.
2. Open a terminal and create an environment.

```bash
python -m venv marama-env
```

   (On some Mac/Linux systems the command is `python3`.)

3. Activate it.
   - **Mac / Linux:** `source marama-env/bin/activate`
   - **Windows (PowerShell):** `marama-env\Scripts\Activate.ps1`
   - If Windows blocks the script, run `Set-ExecutionPolicy -Scope Process RemoteSigned` and try again.
4. Install the packages.

```bash
python -m pip install --upgrade pip
python -m pip install numpy "pandas<3" matplotlib scipy xarray netcdf4 cartopy pyrsig jupyterlab
python -m pip install git+https://github.com/moroots/atmoz
```

5. Start the notebook interface: `jupyter lab`

Official reference: [Python Tutorial: Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html).

## A6. Check that everything works

Paste this into a notebook cell, in Colab or locally, and run it. In Colab, put `!pip install pyrsig git+https://github.com/moroots/atmoz` on its own line first, then run it, then run the check cell.

```python
import importlib

for name in ["numpy", "pandas", "matplotlib", "scipy", "xarray", "netCDF4", "cartopy", "pyrsig", "atmoz"]:
    try:
        mod = importlib.import_module(name)
        print(f"OK       {name:12s} {getattr(mod, '__version__', '(no version)')}")
    except Exception as err:
        print(f"MISSING  {name:12s} {type(err).__name__}: {err}")
```

Every line should start with `OK`. If something says `MISSING`, see the table below. Note which ones are missing and email the contact in section A9. **A missing `cartopy` or `atmoz` will not stop you in Sessions 1 and 2.**

## A7. Troubleshooting

| Problem | What to try |
|---|---|
| `conda` or `uv` is "not found" | Close and reopen the terminal. On Windows with Miniconda, use **Anaconda Prompt**, not regular Command Prompt. |
| `python` is "not found" (Windows) | Reinstall and tick **Add python.exe to PATH**, or try `py` instead of `python`. |
| `pip install git+https://...` fails with "git not found" | Install Git ([git-scm.com](https://git-scm.com/downloads)) or, in a conda environment, run `conda install git`. |
| `cartopy` fails to install | Use Method 1 (Miniconda). Cartopy is the most common failure with pip. |
| `ModuleNotFoundError` for a package you installed | You are probably in a different environment. Activate the course environment, then run `jupyter lab` from the same window. |
| Packages install but the notebook cannot see them | Start `jupyter lab` from the activated environment, not from a different Python. |
| Colab says "Session crashed" or disconnected | **Runtime → Restart session**, then re-run the setup cell. |
| Work computer will not let you install software | Use Colab. It needs only a browser. |
| Colab or Google sign-in is blocked | Install locally on a personal computer, or contact the organizer ahead of time. |

## A8. Optional learning resources

None of this is required. Pick one or two items if you want a head start, and ignore the rest.

### Videos (YouTube)
Checked 2026-11-04: each link opens a live video with the title shown.

| Video | Length | Why watch it |
|---|---|---|
| [Learn Python – Full Course for Beginners](https://www.youtube.com/watch?v=rfscVS0vtbw) (freeCodeCamp.org) | About 4.5 hours | Complete beginner introduction. Watch the first hour or so for variables, lists and loops, which is all Session 1 assumes. |
| [Python for Beginners – Full Course](https://www.youtube.com/watch?v=eWRfhZUzrAc) (freeCodeCamp.org) | About 4.5 hours | An alternative if the first one does not suit you. It reads two programs line by line, which matches our "read first" approach. |
| [Python Pandas Tutorial (Part 1): Getting Started with Data Analysis](https://www.youtube.com/watch?v=ZyhVh-qRZPA) (Corey Schafer) | About 30 minutes | Good preview for Session 2. He also covers selecting, filtering and grouping data in the following parts of the series, which map onto what Excel and R users already do. |

*[Instructor: add any videos you recommend. I could not verify a Colab intro video or an xarray/cartopy video, so I left those out rather than guess.]*

### Free written guides
| Resource | Good for |
|---|---|
| [Overview of Colaboratory Features](https://colab.research.google.com/notebooks/basic_features_overview.ipynb) | Learning the notebook interface in 10 minutes |
| [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) (python.org) | The official, authoritative introduction. Sections 3 to 5 are enough. |
| [Programming with Python: Gapminder](https://swcarpentry.github.io/python-novice-gapminder/) (Software Carpentry) | Slow, careful beginner lessons with exercises |
| [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) | A short tour of data tables, the main Python tool for Session 2 |
| [xarray](https://xarray.dev) | Docs for the gridded-data library in Session 3 |
| [Cartopy documentation](https://scitools.org.uk/cartopy/docs/latest/) | Mapping library for Session 3 |

### If you know R or Excel
You already know most of the *ideas*. The learning is mostly vocabulary. In Session 1 we show a short translation table (columns, filters, group-by, pivot tables, plots). If you want a head start, the pandas tutorial and Corey Schafer's series above focus on exactly those tasks.

## A9. Logistics

| | |
|---|---|
| **Dates and times** | **[TBD: Session 1–4 dates, start time and time zone]** |
| **Location (in person)** | **[TBD]** |
| **Virtual link** | **[TBD]** |
| **Contact for help before the course** | **[TBD: name, email]** |
| **During class** | Ask a helper in the room, or post in the chat if you are virtual. |

**What to bring:** a laptop and charger. Set your screen so you can see the instructor's screen and your notebook at the same time (a second monitor helps, but is not required).

**Before each session:** you will get an email with that session's notebook link. Open it and run the first cell to confirm everything loads.

**After each session:** solutions and any notebook updates will be shared. **[TBD: where and how.]**

---

# Part B. For MARAMA organizers

## B1. What to send, and when

| When | What | To whom |
|---|---|---|
| About 3 weeks before Session 1 | Part A of this guide, plus the dates, times, venue and virtual link | All registrants |
| About 1 week before | Reminder: "Run the Colab check (section A4) now." Include the help contact | All registrants |
| 1 to 2 days before | Session 1 notebook link and final logistics | All registrants |
| After each session | Solutions and the next session's notebook link | All registrants |

**[TBD: confirm the exact timing and the delivery channel (email list, event page, or other).]**

## B2. What the instructor needs from you

- **Registration list** with emails, and a way to flag virtual versus in-person attendees.
- **A room** with reliable Wi-Fi sized for the whole room at once. Everyone is downloading a few small files on a shared network at the same time.
- **Power strips.** Laptops will be open for 90 minutes.
- **A projector or large display** and, for virtual attendees, a meeting platform with screen sharing and chat. **[TBD]**
- **Two helpers** present during the hands-on blocks, ideally with some Python experience. They should do the section A4 check themselves first.
- **A contact person** for attendees' setup questions before the course. **[TBD]**

## B3. Expected attendee problems, from most to least likely

1. **Work computers that block software installs.** This is why Colab is the primary route and the local install is optional.
2. **Organizations that block Google sign-in or Colab.** Ask registrants in advance, for example with one line on the registration form, "Can you sign in to Google and open colab.research.google.com from the device you'll bring?"
3. **Windows PATH and activation problems** in the local install (see section A7).
4. **Network limits on a shared room Wi-Fi.** The notebooks use small bundled files for this reason.
5. **People who arrive without doing the check.** Allow about 10 minutes of the first session for catch-up, which the schedule already has in its buffer.

## B4. Suggested pre-course question for the registration form

> 1. Can you sign in to a Google account and open colab.research.google.com on the computer you'll bring? (Yes / No / Not sure)
> 2. Have you used Python, R, or Excel for data analysis? (Python / R / Excel / None)
> 3. Will you attend in person or virtually?
> 4. Is there anything we should know to make the sessions accessible for you?

---

## Open items before this guide is sent

- **[TBD]** Dates, times, location, virtual link, contact, and how solutions and notebooks are delivered.
- **[TBD]** Where the notebook links will be hosted. The Colab links depend on a public location, which is currently out of scope.
- **To verify:** the local install steps for all three methods were written from the official documentation. I have not run them on Windows, Mac and Linux, or run the section A6 check against a fresh install of each.
- **To verify:** that `atmoz` installs from GitHub on a clean machine and in Colab. It does not appear on PyPI under that name, so the guide uses `pip install git+https://github.com/moroots/atmoz`, which is what the earlier bootcamp notebooks used.
- **To verify:** the Python version to recommend (the guide says 3.12).
- **Optional:** add recommended videos from the instructor.

# 🐍 Before the Course

**MARAMA Python Tutorial Series, 2026**

<div class="box goal">

**🎯 The goal**

Get a working Python setup before Session 1. You have two options: **Google Colab** (recommended, runs in your browser, nothing to install) or **your own computer**.

</div>

## The course will cover

| Session | Topic |
|---|---|
| 1 | Overview of Python and Simple Statistics in Python |
| 2 | Data Analysis Techniques and Simple Plotting |
| 3 | Python Tools for Atmospheric Science |
| 4 | Analysis Workflows and Pipelines |

## You will need

- **A laptop and charger.** Windows, Mac or Linux all work.
- **An internet connection.**
- For Colab: **a Google account** (a personal one is fine) and a current browser (Chrome, Edge, Firefox or Safari).

## Option 1: Google Colab

**Colab** is a free Google service that runs Python in your browser.

1. Go to the course page, [github.com/moroots/marama_2026](https://github.com/moroots/marama_2026), and click the **Open in Colab** button next to the notebook you want.
2. **Choose the Python version.** Colab defaults to Python 3.13, but the course is tested on Python 3.12. Choose **Runtime → Change runtime type**, set **Runtime Version** to **2026.07** (it ships Python 3.12), and click **Save**. Connecting can take 2 to 3 minutes. That is normal.
3. **Check the version.** Run this in a cell with **Shift+Enter**:

   ```python
   import sys
   print("Python", sys.version.split()[0])
   print("✅ Correct version." if sys.version_info[:2] == (3, 12) else "❌ Wrong version. Repeat step 2.")
   ```

4. **Run the notebook's first code cell, "Colab setup".** It downloads every course file and installs what that notebook needs. Session 3 and 4 notebooks take a few minutes the first time. If Colab shows a **Restart session** button, click it, then run that cell again.
5. Click the **folder icon** on the left to see all the course files.

<div class="box why">

**💡 Colab forgets everything between visits**

Each visit starts on a fresh computer, so the setup cell downloads and installs again. About 10 minutes before each session, open the notebook and run the version check and the setup cell. To keep your own work, use **File → Save a copy in Drive**.

</div>

### If something goes wrong in Colab

| Problem | What to try |
|---|---|
| The version check says **❌ Wrong version** | Repeat step 2, wait for it to connect, then check again. |
| The **Runtime Version** dropdown is missing, or 2026.07 is not listed | Email us a screenshot of the dropdown. |
| The setup cell prints a lot of red text | Often only warnings. If the last lines say `Successfully installed`, you are fine. If they say `ERROR`, run the cell once more. |
| Colab shows "Session crashed" or disconnected | **Runtime → Restart session**, then run the setup cell again. |
| A cell says `ModuleNotFoundError` | Run the **setup cell** (the first code cell) first. |
| You cannot sign in to Google, or Colab is blocked at work | Use a personal device, or use Option 2. |
| Nothing here helps | Email mroots1@umbc.edu with a screenshot. **Please do this before the course,** not during the session. |

## Option 2: your own computer

Use this if Colab is blocked for you, you prefer to work offline, or you want to keep using Python after the course. You set it up once.

**Use Python 3.12**, the version we tested. Check yours with `python --version` (or `python3 --version`). If it is not 3.12, the steps below set up 3.12 inside a separate environment and do not change your existing Python.

> **Windows tip:** use **PowerShell**. On Mac and Linux, use **Terminal**.

**Words used below.** A *terminal* is a window where you type commands. An *environment* is a separate folder of packages, so nothing you do here can break other software on your computer.

**First, get the course files.** On the [course page](https://github.com/moroots/marama_2026) click the green **Code** button, then **Download ZIP**, and unzip it. Open a terminal **inside the unzipped folder**. (If you know git, `git clone https://github.com/moroots/marama_2026` works too.)

### Method 1 (recommended): uv

`uv` is a fast tool that installs Python and packages and keeps environments tidy. It downloads Python 3.12 for you if needed.

1. Install `uv` from the [official page](https://docs.astral.sh/uv/getting-started/installation/), then close and reopen your terminal.
   - **Mac / Linux:** `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - **Windows (PowerShell):** `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. In the course folder, create the environment:

   ```bash
   uv venv --python 3.12
   ```

3. Activate it. You should see `(.venv)` at the start of your prompt.
   - **Mac / Linux:** `source .venv/bin/activate`
   - **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
   - If Windows blocks the script, run `Set-ExecutionPolicy -Scope Process RemoteSigned` and try again.
4. Install the course and everything it needs:

   ```bash
   uv pip install -e ".[all]" jupyterlab
   ```

5. Start the notebook interface with `jupyter lab`. Your browser opens. Open a notebook from the file list on the left.

**Next time:** open a terminal in the course folder, activate the environment (step 3), then run `jupyter lab`.

### Method 2: Python's standard tools (`venv` and `pip`)

1. Install **Python 3.12** from [python.org/downloads](https://www.python.org/downloads/) (a 3.12.x release, not the newest version on the front page). **On Windows, tick "Add python.exe to PATH" on the first screen of the installer.**
2. In the course folder, create the environment (on Mac/Linux the command may be `python3`):

   ```bash
   python -m venv .venv
   ```

3. Activate it:
   - **Mac / Linux:** `source .venv/bin/activate`
   - **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
4. Install the course and everything it needs:

   ```bash
   python -m pip install --upgrade pip
   python -m pip install -e ".[all]" jupyterlab
   ```

5. Start `jupyter lab`. **Next time:** open a terminal in the course folder, activate the environment (step 3), then run `jupyter lab`.

Official reference: [Python Tutorial: Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html).

**Only taking some sessions?** Install `".[session3]"` or `".[session4]"` instead of `".[all]"`. Sessions 1 and 2 need just `"."`.

### Check that everything works

Paste this into a notebook cell and run it with **Shift+Enter**:

```python
import sys, importlib
print("Python", sys.version.split()[0])
names = ["numpy", "pandas", "scipy", "matplotlib", "pyarrow", "xarray", "netCDF4", "geopandas",
         "cartopy", "metpy", "plotly", "act", "pyrsig", "atmoz", "requests", "herbie", "cfgrib", "sklearn"]
missing = []

for name in names:
    try:
        mod = importlib.import_module(name)
        print(f"OK       {name:12s} {getattr(mod, '__version__', '')}")
    except Exception as err:
        missing.append(name)
        print(f"MISSING  {name:12s} {type(err).__name__}")

print()
if not missing:
    print("✅ Ready. You are set for the course.")
else:
    print("❌ Not ready yet. Missing:", ", ".join(missing))
    print('Run this in your terminal (environment activated, inside the course folder), then check again:')
    print('    uv pip install -e ".[all]"        (or: python -m pip install -e ".[all]")')
```

### Local install troubleshooting

| Problem | What to try |
|---|---|
| `uv` is "not found" | Close and reopen the terminal. |
| `python --version` is not 3.12 | With uv, create the environment with `uv venv --python 3.12`. With plain `venv`, install 3.12 from python.org and use its full name, such as `py -3.12 -m venv .venv` (Windows) or `python3.12 -m venv .venv` (Mac/Linux). |
| `python` is "not found" (Windows) | Reinstall and tick **Add python.exe to PATH**, or try `py` instead of `python`. |
| The install says it cannot find `pyproject.toml` | Your terminal is not inside the course folder. `cd` into the unzipped folder and try again. |
| A package fails to install | Read the last lines of the error and email them to us. Colab is a good fallback in the meantime. |
| `ModuleNotFoundError` for a package you installed | You are probably in a different environment. Activate the course environment, then run `jupyter lab` from the same window. |
| Your work computer will not let you install software | Use Colab (Option 1). It needs only a browser. |

---

Questions? Email [mroots1@umbc.edu](mailto:mroots1@umbc.edu)

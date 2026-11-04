# 🐍 Before the Course

**MARAMA Python Tutorial Series, 2026** · Four 90-minute sessions · You leave with analysis you can show your supervisor.

*Whether you have never typed a line of code or you live in R, this guide gets you ready in 15 minutes.*

<div class="legend">

🎯 **Blue**: the goal and why it matters · ✍️ **Orange**: your turn · 💬 **Purple**: talk about it · 💡 **Green**: tip · ⚠️ **Red**: watch out

</div>

This guide has three parts:

- **Part A is for you, the attendee.** Fifteen minutes of preparation, then everything you might want to look up.
- **Part B is for MARAMA organizers:** what to send, when, and what to arrange. *(Attendees can skip it.)*
- **Part C is a short note you can forward to your supervisor.**

The optional local Python install lives in the **Appendix**. You do not need it to take the course.

---

# Part A. For attendees

## A1. What you will be able to do

<div class="box goal">

**🎯 The goal**

You already know how to think about air quality data. This course gives you a tool that does the repetitive part for you, and lets you check other people's work, including work written by AI.

</div>

By the end of Session 4 you will be able to:

1. **Take a raw monitor file to a regulatory answer yourself.** Clean it, plot it, and test it against a standard, step by step, and explain the result to a colleague. *(Sessions 1 and 2)*
2. **Put TEMPO satellite NO₂ on a map next to ground monitors** for a real episode, June 2025. *(Session 3)*
3. **Re-run a whole analysis with one command** when new data arrives, instead of redoing it by hand. *(Session 4)*
4. **Read a Python script, including one an AI assistant wrote, and say what it does, what it will output, and whether it is right.** *(every session)*

### What you take home

- A notebook that analyzes real monitor data, built by **you**, that you can show your supervisor.
- A short "episode report" notebook: you pick a pollution episode, and the notebook pulls the data, maps it and summarizes it.
- A first draft of automating **one task from your own job** (see A6).
- A one-page cheat sheet and the solutions to every exercise.

<div class="box why">

**💡 Why this course is different**

You will not watch someone else's code scroll by. In every session you **write real code on real data**, you **predict before you run**, and you **practice catching mistakes**, the skill that matters most when AI writes a growing share of the code. Expect to say "wait, I did that?" at least once.

</div>

## A2. Your 15-minute preparation

Three things, in this order. Each one is short.

| Step | Time | What |
|---|---|---|
| 1 | 5 min | **Open Colab and run one cell** (A4). If this works, your setup is done. |
| 2 | 5 min | **Try the read-and-predict warm-up** (A5). It shows you the main skill we teach. |
| 3 | 5 min | **Tell us about one real task** from your job that you would like to speed up (A6). |

<div class="box turn">

**✍️ That is all that is required.**

Everything else in this guide is for reference, or optional. Done with all three? You are ready. Go get coffee.

</div>

## A3. Pick your path

You do not all start in the same place, and the course is built for that. Choose the row that sounds like you. You can change your mind at any time.

| If you say... | Your path |
|---|---|
| **"I've never written code."** | You are who the course is built for. Do steps 1 to 3 above and skip the rest. In class, every exercise starts with a worked example you can copy from. Ask the helpers freely. Nobody is keeping score. |
| **"I use Excel or R."** | You already know the ideas: columns, filters, group-by, pivot tables, plots. The work is vocabulary. We will give you an Excel/R-to-Python translation table. To preview, try [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html). |
| **"I already write some Python."** | Every exercise has a ⭐ stretch task for you. Bring a harder real problem (A6). Please try the warm-up anyway: the course is about reading code carefully, which experienced coders often skip. |
| **"I'm joining virtually."** | You get the same course, and it is designed for you too. Questions, polls and "I'm stuck" signals all run through the chat (A7). Run steps 1 to 3 on the computer you will use that day. |

## A4. Step 1: Open Colab and run one cell

**Colab** is a free Google service that runs Python notebooks in your browser. We use it for all four sessions. Nothing to install, and it works the same on Windows, Mac and Linux.

You need a Google account (a personal one is fine), a current browser, and an internet connection.

1. Go to [colab.research.google.com](https://colab.research.google.com) and sign in.
2. Choose **File → New notebook**.
3. In the first cell, type `print("Hello, MARAMA")` and press **Shift+Enter**.
4. `Hello, MARAMA` should appear under the cell.
5. In a new cell, run this and check that you see three version numbers:

```python
import numpy, pandas, matplotlib
print(numpy.__version__, pandas.__version__, matplotlib.__version__)
```

<div class="box goal">

**🎯 See three version numbers? You are done with setup.**

You have run Python. Everything from here is the fun part.

</div>

<div class="box why">

**💡 Four things to know about Colab**

- Each time you open a notebook, you get a **fresh computer**. Anything you installed disappears when the session ends. Our notebooks start with a setup cell that reinstalls what they need. **Run it first, every time.**
- Colab can disconnect when idle. If it does, choose **Runtime → Run all**, or re-run the setup cell.
- Use **File → Save a copy in Drive** so your edits are kept.
- **If your organization blocks Google sign-in or Colab,** tell us now (A9). We will help you with the local install in the Appendix, or pair you with a partner.

</div>

## A5. Step 2: Read and predict (5 minutes)

The main skill in this course is **reading** Python. Code is increasingly written by AI assistants, and the people who benefit most are the ones who can look at a script and tell whether it is right.

Here is the method we use all the time: **read → predict → run → change → check.**

<div class="box turn">

**✍️ Your turn: read this code. Do not run it yet.**

The numbers are made-up hourly ozone readings, in parts per billion.

</div>

```python
ozone_ppb = [38, 52, 61, 74, 69, 45]
threshold_ppb = 60

above = [x for x in ozone_ppb if x > threshold_ppb]

print(len(above), "readings above the threshold")
print("highest:", max(ozone_ppb))
print("average:", sum(ozone_ppb) / len(ozone_ppb))
```

1. **Predict.** Write down, on paper or in your head, what the three lines of output will be. A guess is fine. Being wrong is useful, because it shows you where your picture of the code differs from what the computer does.
2. **Run it** in a Colab cell. Compare with your prediction.
3. **Change it.** Before you run, predict what happens if you set `threshold_ppb = 70`. Then try it.
4. **Check it.** An AI assistant wrote this line to compute the average:

```python
print("average:", sum(ozone_ppb) / 5)
```

<div class="box watch">

**⚠️ Spot the bug**

It runs without any error. **Is the number right? How would you find out?** Think for a minute before you open the answers.

</div>

<details>
<summary><b>Answers (open after you have tried)</b></summary>

- **Output:** `3 readings above the threshold`, then `highest: 74`, then `average: 56.5`. The readings above 60 are 61, 74 and 69.
- **With a threshold of 70:** only the 74 is above it, so you get `1 readings above the threshold`. (The grammar is off. That is a small thing you could fix. How?)
- **The bug:** the list has **six** values, but the code divides by `5`. It prints `67.8`, not `56.5`. It looks plausible, runs without an error, and is wrong. Hard-coded numbers are a common failure in generated code. A hand calculation (339 ÷ 6 = 56.5) or `len()` is the fix.

If you got most of it, good. If you did not, you are exactly where the course starts.

</details>

## A6. Step 3: Bring one real task

Adults learn fastest from their own problems. Before Session 1, think of **one thing you do repeatedly** that you wish were faster or less error-prone. Some examples from air quality work:

- Pulling monitor data and building the same summary table every month.
- Checking which monitors exceeded a level, and by how much.
- Making the same plot for a report again and again.
- Comparing this year's season with the last five.
- Taking the output of a model run and checking it against monitors.

We will ask for it on the registration form or by email **[TBD: delivery]**. One sentence is plenty: *"Every week I ___ in Excel, and it takes ___."* We will use these (anonymously) for examples and for discussion time, and in Session 4 you will start automating your own.

<div class="box watch">

**⚠️ Please do not bring sensitive or confidential data.**

Describe the task. We will practice on public data such as AirNow and AQS, and you can apply the same steps to your own files later at work.

</div>

## A7. What a session looks like

Each session is 90 minutes, with about 30 of lecture, 30 of hands-on and 30 of buffer, discussion and catch-up. The room is about 30 people, joined by about 150 online. We keep that many people moving with a few habits.

| Time | What happens |
|---|---|
| About 30 min | **Live coding.** The instructor writes code on screen, makes mistakes, and fixes them. You follow along, or watch and type later. Both are fine. We stop often and ask you to predict what comes next. |
| About 30 min | **Hands-on.** You work through a notebook in your own Colab. Helpers move around the room and watch the chat. Every exercise has a worked example, a ⭐ stretch version, and hints. |
| About 30 min | **Buffer, discussion and questions.** Interrupting is welcome. This is where your real-world tasks come in. |

### How the hands-on notebooks work

Our notebooks look like this, so nothing surprises you:

<div class="box goal">

**🎯 Blue: the goal.** Each block opens by telling you what you will have at the end and why it matters.

</div>

<div class="box turn">

**✍️ Orange: your turn.** You write real code here: a line, a loop, a table. Every one follows a worked example, so you are never starting from a blank cell.

</div>

<div class="box discuss">

**💬 Purple: talk about it.** Turn to a neighbor, or answer in the chat if you are virtual. The instructor's take stays folded until you have talked.

</div>

<div class="box watch">

**⚠️ Red: watch out.** A common trap, flagged before you fall in.

</div>

And a few more things worth knowing:

- **Predictions are locked in.** Before a result appears, you commit to a yes/no or A/B/C call. Then the notebook tells you how your call did. You never guess numbers, only reason about what the code will do.
- **Checks judge your result, not your wording.** If your code gives the right answer, you get a ✅. If not, you get a nudge, and a hint that gets more specific each time you open the next one.
- **Checkpoints are built in.** If you fall behind or something breaks, a checkpoint cell gives you a ready-made table so you can rejoin the next block. **There is no shame in using one.** Using it means you saw it was time to catch up, which is what experienced analysts do.
- **Polls.** A few questions per session are live polls. If you are in the room, answer in the poll like everyone else.
- **Two chat signals.** Type **✅** in the chat when you finish a block. Type **❓** when you are stuck or used a checkpoint. A helper watches for ❓ and comes to you. You never have to interrupt to ask for help.
- **Notebooks come with files.** Each session notebook has a data file and a small helper file (`marama_helpers.py`) that does the behind-the-scenes work. You drag them into Colab (the 📁 folder icon on the left) before you start. The email with the notebook link says which files and exactly how. **[TBD: how files are delivered]**
- **Solutions are shared after each session**, so you can fall behind in class and catch up later.
- **Setup help is built in.** The first 15 minutes of Session 1 are for getting everyone working, with helpers beside you. Do the preparation anyway, because it makes this faster.
- **It is fine to get stuck.** Reading an error message is part of the plan.

## A8. Between sessions

Learning sticks when it is spread out. Between sessions you get a **15-minute micro-task**:

- **After Session 1:** change one thing in an example and predict the result.
- **After Session 2:** run the same analysis on a different monitor.
- **After Session 3:** swap in a different pollutant or date.
- **After Session 4:** apply the pipeline pattern to your own task from A6.

These are optional and short. **[TBD: weekly gap between sessions. If the sessions are on consecutive days, this section changes.]**

## A9. Logistics

| | |
|---|---|
| **Dates and times** | **[TBD: Session 1–4 dates, start time and time zone]** |
| **Location (in person)** | **[TBD]** |
| **Virtual link** | **[TBD]** |
| **Contact for help before the course** | **[TBD: name, email]** |
| **Optional drop-in setup clinic** | **[TBD: date and time, virtual, before Session 1]** |
| **During class** | Ask a helper in the room, or put ❓ in the chat if you are virtual. |

**What to bring:** a laptop and charger. A second screen helps, so you can see the instructor and your notebook together, but you do not need one. If you join virtually, a second screen or a second device is the best upgrade you can make.

**Before each session** you will get an email with that session's notebook link. Open it and run the first cell to confirm it loads. **After each session,** solutions are shared **[TBD: where and how]**.

## A10. Resources

Optional. Don't try to do all of this.

### If you want a head start (each is short)
| For | Resource | Time |
|---|---|---|
| Before Session 1 | Google's [Overview of Colaboratory Features](https://colab.research.google.com/notebooks/basic_features_overview.ipynb): how cells and notebooks work | 10 min |
| Before Session 2 | [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html): the data-table tool we use | 10 min |
| Before Session 2 | [Python Pandas Tutorial (Part 1)](https://www.youtube.com/watch?v=ZyhVh-qRZPA) by Corey Schafer (video) | About 30 min |
| Before Session 3 | [xarray](https://xarray.dev) and [Cartopy](https://scitools.org.uk/cartopy/docs/latest/) docs. Browse the gallery only, to see what is possible | 10 min |

### After the course, if you want to go deeper
- [Programming with Python: Gapminder](https://swcarpentry.github.io/python-novice-gapminder/) (Software Carpentry): careful beginner lessons with exercises.
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) (python.org): the official reference. Sections 3 to 5 cover most of what you will use.
- Long beginner videos on YouTube, if you prefer watching: freeCodeCamp's [Learn Python – Full Course for Beginners](https://www.youtube.com/watch?v=rfscVS0vtbw) and [Python for Beginners – Full Course](https://www.youtube.com/watch?v=eWRfhZUzrAc) (each about 4.5 hours). These are general Python, not air quality, so they work better after the course than before it.

*Links checked on 2026-11-04.*

## A11. If something goes wrong with Colab

| Problem | What to try |
|---|---|
| Colab shows "Session crashed" or disconnected | **Runtime → Restart session**, then re-run the setup cell. |
| A cell says `ModuleNotFoundError` | Run the notebook's first (setup) cell, then try again. |
| You cannot sign in to Google, or Colab is blocked at work | Tell us (A9). Use a personal computer, or the Appendix, or sit with a neighbor for the first session. |
| Your work computer will not open Colab | Same as above. A personal device works. |
| Nothing here helps | Email the contact in A9 with a screenshot. We would rather hear from you now than see you stuck in Session 1. |

---

# Part B. For MARAMA organizers

*Not for attendees. Send Part A (A1 to A11), Part C and the Appendix. Keep this part.*

<div class="box watch">

**⚠️ Before you send: everything still open**

Placeholders in the text are marked **[TBD]**. Search for that word to find them.

**Details only the instructor can fill in**
- Dates, start time and time zone for all four sessions (A9)
- In-person location and virtual link (A9)
- Help contact: name and email (A9)
- Drop-in setup clinic date (A9)
- How the registration answers are collected (A6)
- How notebook files (data and `marama_helpers.py`) reach attendees (A7)
- Where solutions are shared (A9)
- The gap between sessions (A8). Consecutive days would change the micro-tasks.
- Cost, for the supervisor note (Part C)

**Things the course team still has to build**
- The setup notebook that ends with a first-win plot. The opener of the PM2.5 example notebook (`test/test_file_v3.ipynb`) could serve.
- The four between-session micro-tasks (A8).
- The one-page cheat sheet and the manager one-pager, "What to ask your analyst, and how to check AI-written code."
- The episode-report notebook for Session 4. A1 promises it, so confirm it first.
- The Excel/R translation table promised in A3.

**Things to confirm against the lesson plan**
- A1 outcome 1 is written generally ("raw monitor file to a regulatory answer"). The lesson plan names the ozone design value, which it lists as a stretch.
- Which session the example notebook belongs to. It is not Session 1.

</div>

## B1. What to send, and when

| When | What | To whom |
|---|---|---|
| About 3 weeks before Session 1 | Part A of this guide, the dates, times and links, and the registration form (B5) | All registrants |
| About 2 weeks before | Part C (the supervisor note), as a separate short message | Registrants, to forward |
| About 1 week before | Reminder: "Do the 15-minute preparation now." Include the drop-in setup clinic details and the help contact | All registrants |
| 1 to 2 days before | Session 1 notebook link, its files, and the first-win setup notebook | All registrants |
| After each session | Solutions, the next notebook, and the micro-task | All registrants |

**Format.** This guide builds to a styled web page (`docs/before-the-course.html`). Colors and boxes show best as an attached HTML file or a PDF printed from the browser. Many email programs strip styling from pasted HTML, so attach rather than paste. **[TBD: confirm delivery channel.]**

## B2. Staffing for about 180 people

The room has about 30 people and about 150 attend online. The staff is the instructor and **two student helpers**. Community practice for online teaching is about one helper per five participants, so this ratio is far thinner. The notebooks are therefore built to be **mostly self-service**:

- **Tiered hints** that get more specific each time, so most stuck moments end without a human.
- **Checkpoint cells** so no one is ever stranded.
- **A two-emoji chat signal**: ✅ means finished, ❓ means stuck or used a checkpoint. Helpers watch the chat for ❓ and ignore the rest.
- **Live polls** for the four or so yes/no or A/B/C calls in each notebook, so the instructor sees the room's thinking at a glance. The polls are set up in the meeting tool, not in the notebook.

**Suggested roles for the two helpers.** One watches the chat for ❓ and answers in writing. One walks the room and handles in-person questions. The instructor teaches, and does not field individual problems during the hands-on block. Both helpers should do the A4 check, the A5 warm-up and the example notebook beforehand, so they have seen what attendees will see.

## B3. What the instructor needs from you

- **Registration list** with emails, an in-person or virtual flag, and answers to the form in B5.
- **A room** with reliable Wi-Fi sized for the whole group using it at once.
- **Power strips.** Laptops will be open for 90 minutes.
- **A projector or large display.** For virtual attendees, a meeting platform with screen sharing, chat and polls. **[TBD]**
- **Two helpers** present during every hands-on block (B2).
- **A contact person** for setup questions before the course. **[TBD]**
- **15 minutes at the start of Session 1 for setup help.** The first session's agenda should show it. The people who struggle most with installation are also the least likely to come to an optional help session, so setup help has to be part of the class itself.
- **An optional drop-in clinic** the week before. **[TBD]** Offer it, but don't depend on it.

## B4. Expected problems, from most to least likely

1. **Work computers that block software.** Colab is the main route for this reason.
2. **Organizations that block Google sign-in or Colab.** Find these out early with the form.
3. **Attendees who arrive without doing the preparation.** The 15-minute setup block in Session 1 handles this.
4. **Uploading the data and helper file to Colab.** Expect this to be the most common stuck point in a notebook session. Show it once on screen, and put a one-line reminder in the notebook email.
5. **Shared Wi-Fi limits.** Small bundled data is the mitigation.
6. **Windows PATH problems** for anyone doing the local install (Appendix).

## B5. Registration form questions

1. Can you sign in to a Google account and open colab.research.google.com on the computer you will bring? (Yes / No / Not sure)
2. Which sounds most like you? (I have never written code / I use Excel or R / I already write some Python)
3. Will you attend in person or virtually?
4. **What is one task you do repeatedly that you wish were faster?** (One sentence. Please don't include confidential details.)
5. Is there anything we should know to make the sessions work for you?

## B6. Still to verify

- **Colab.** Nothing in this guide or in the example notebook has been run in Colab yet. Run A4, A5 and the example notebook there once, including the file upload.
- **Colab's Python version** on the day. Attendees cannot choose it, and `pyrsig` is vetted only on 3.12.
- **The A5 warm-up** was run locally and the outputs match the answers.
- **The local install steps** (Appendix) were written from official documentation and have not been run on Windows, Mac and Linux.
- **Rendering.** The styled HTML has not been viewed in Outlook or Gmail. Open the file in a browser and print a PDF to check it.
- **Regulatory numbers** used in the notebooks (24-hour PM2.5 standard of 35 µg/m³, annual standard of 9.0 µg/m³) should be re-checked against current EPA pages before the course.

---

# Part C. A note for supervisors

*(Attendees can forward this. Edit freely.)*

**Subject: Why I'd like to attend the MARAMA Python tutorial series**

I'd like to attend four 90-minute sessions run by Dr. Maurice Roots for MARAMA. The course teaches Python for air quality work, aimed at staff who use Excel or R and have not written Python.

It matters for our work because analyses that take hours by hand can be repeated automatically each time data arrives, and because more of the code we receive is now written by AI. The course trains people to read and check that code, not only write it.

By the end I should be able to compute an ozone design value from monitor data, map satellite NO₂ next to ground monitors for a real episode, and rerun an analysis with one command. I will bring back a short episode-report notebook and a first draft of automating one of my own recurring tasks.

Time commitment: four 90-minute sessions **[TBD dates]**, plus about 15 minutes of preparation and a short optional task between sessions. Cost: **[TBD]**.

---

# Appendix. Optional: run Python on your own computer

Do this only if you want to work offline, if Colab is blocked for you, or if you want to keep using Python after the course. **It is not needed for the course.** Pick **one** method. If you are unsure, use **Method 1 (Miniconda)**.

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

**Python version: use 3.12.** The course supports **Python 3.11 and 3.12 only**. Python 3.10 and older are deprecated. Do not use 3.13 or newer. `pyrsig`, the package that downloads EPA data, has only been vetted on **3.12**, so that is the version we recommend and test. Use 3.11 only if you already have it and cannot change it.

**Check which Python you have:** run `python --version` (or `python3 --version`). If it shows anything other than 3.11 or 3.12, the steps below install 3.12 inside a separate environment. They do not change your existing Python.

> **Windows tip:** after installing, use **Anaconda Prompt** (Method 1) or **PowerShell** (Methods 2 and 3). On Mac and Linux, use **Terminal**.

### Method 1 (recommended): Miniconda

Miniconda installs Python and a package manager called `conda`. It handles the hard-to-install map and satellite-data packages well.

1. Download and install Miniconda from the official guide: [Miniconda installation](https://www.anaconda.com/docs/getting-started/miniconda/install/overview). Use the graphical installer unless you are comfortable with a terminal.
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

`pyrsig` currently needs `pandas<3`, which is why the version is limited. `git` is in the first command because the `atmoz` install pulls code from GitHub.

5. Start the notebook interface with `jupyter lab`. Your browser opens. Create a new Python notebook and run the check in the last section of this appendix.

**Next time:** open Anaconda Prompt or Terminal, run `conda activate marama`, then `jupyter lab`.

Official references: [conda getting started](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html), [Miniconda installers](https://docs.conda.io/projects/miniconda).

### Method 2: uv

`uv` is a newer, very fast tool that installs Python and packages. It suits you if you are comfortable with a terminal. If `cartopy` fails to install, use Method 1.

1. Install `uv` from the [official installation page](https://docs.astral.sh/uv/getting-started/installation/). Close and reopen your terminal afterward.
   - **Mac / Linux:** `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - **Windows (PowerShell):** `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Create a project folder and environment.

```bash
mkdir marama && cd marama
uv venv --python 3.12
```

3. Activate it.
   - **Mac / Linux:** `source .venv/bin/activate`
   - **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
4. Install the packages. You need **Git** for the `atmoz` line ([git-scm.com](https://git-scm.com/downloads)).

```bash
uv pip install numpy "pandas<3" matplotlib scipy xarray netcdf4 cartopy pyrsig jupyterlab
uv pip install git+https://github.com/moroots/atmoz
```

5. Start the notebook interface: `jupyter lab`

### Method 3: Python's standard tools (`venv` and `pip`)

This uses only what comes with Python. It is the most universal and the most manual.

1. Install **Python 3.12** from [python.org/downloads](https://www.python.org/downloads/) (choose a 3.12.x release, not the newest version on the front page). **On Windows, tick "Add python.exe to PATH" on the first screen of the installer.** Install [Git](https://git-scm.com/downloads) too.
2. Create an environment. On some Mac/Linux systems the command is `python3`.

```bash
python -m venv marama-env
```

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

### Check that everything works

Paste this into a notebook cell and run it. In Colab, first run `!pip install pyrsig git+https://github.com/moroots/atmoz` on its own, then run the check.

```python
import importlib

for name in ["numpy", "pandas", "matplotlib", "scipy", "xarray", "netCDF4", "cartopy", "pyrsig", "atmoz"]:
    try:
        mod = importlib.import_module(name)
        print(f"OK       {name:12s} {getattr(mod, '__version__', '(no version)')}")
    except Exception as err:
        print(f"MISSING  {name:12s} {type(err).__name__}: {err}")
```

Every line should start with `OK`. A missing `cartopy` or `atmoz` will not stop you in Sessions 1 and 2.

### Local install troubleshooting

| Problem | What to try |
|---|---|
| `conda` or `uv` is "not found" | Close and reopen the terminal. With Miniconda on Windows, use **Anaconda Prompt**, not regular Command Prompt. |
| `python --version` shows 3.13 or newer, or 3.10 or older | Make the environment with 3.12 explicitly (`conda create -n marama python=3.12`, or `uv venv --python 3.12`). With plain `venv`, install Python 3.12 from python.org and use its full name, such as `py -3.12 -m venv marama-env` on Windows or `python3.12 -m venv marama-env` on Mac/Linux. |
| `python` is "not found" (Windows) | Reinstall and tick **Add python.exe to PATH**, or try `py` instead of `python`. |
| `pip install git+https://...` fails with "git not found" | Install Git ([git-scm.com](https://git-scm.com/downloads)), or in a conda environment run `conda install git`. |
| `cartopy` fails to install | Use Method 1 (Miniconda). Cartopy is the most common failure with pip. |
| `ModuleNotFoundError` for a package you installed | You are probably in a different environment. Activate the course environment, then run `jupyter lab` from the same window. |
| Packages install but the notebook cannot see them | Start `jupyter lab` from the activated environment, not a different Python. |
| Your work computer will not let you install software | Use Colab. It needs only a browser. |

**To verify:** the local install steps were written from the official documentation. They have not been run on Windows, Mac and Linux, nor has the check above been run against a fresh install of each.

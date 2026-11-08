"""marama_helpers.py: helpers for the MARAMA tutorial notebooks.

Keep this file in the same folder as the notebook. It checks your work without showing you the answer,
runs the predict-then-reveal routine, and can load a ready-made clean table if you get stuck.
"""
import hashlib
import numpy as np
import pandas as pd

_KEY = {"sep": "cbe5cfdf7c21", "sep_read": "59e19706d51d", "clean": "bcd6d8cc5bd5", "datetime": "a938adc37b86", "numeric": "661aa146449a", "stretch_a": "2bbe7750e548", "sites": "cad90b433739", "loop": "2c624232cdd2", "hourly": "0bf6e2b11690", "labels": "3cbc87c7681f", "june": "6827d8c699db", "stretch_b": "4723cfec8520", "ai_diff": "d4735e3a265e", "naaqs24": "9f14025af006", "exceed": "5feceb66ffc8", "p98": "a86d4cb8b7e0", "bar": "2c624232cdd2", "annual": "19581e27de7c", "annual_top": "e0b04046fbfb", "peaks": "e7cb4ddbad67", "flagged": "03d856e68a24", "fix_add": "61182f398518", "names": "c7bf4bbdbcd8", "swap": "58a9904c9ca4", "float_conv": "ceaa3d6a2fea", "label_text": "e81278219320", "county": "842d0b270c03", "site_number": "bd6ecf2f23cc", "copy": "aea92132c4cb", "unpack": "f727996d73d5", "season11": "e85a6413c1bd", "dict_add": "7f440f59d02b", "divmod": "ea4d5893b205", "case_cmp": "60a33e6cf515", "valid_range": "5d5be987d596", "wind_band": "fa6cff0bff3a", "total_high": "fc56dbc6d465", "first_over_70": "eb624dbe56eb", "countdown": "c57c465c8537", "is_over": "3cbc87c7681f", "rounded": "28b20fd0a8b3", "label": "12300417a49b", "columns": "2b89ffce0dca", "name_of_c": "9e843db53797", "second_reading": "de13561a65c3", "highest": "f1a6bcf1f6ab", "n_over_12": "4e07408562be", "lowest_site": "559aead08264", "n_high": "d4735e3a265e", "kw_args": "d4735e3a265e"}
_HINTS = {"sep": ["Look at the first line again. What sits between the column names?", "It is not a comma, a tab or a space. It is on the same key as the backslash."], "sep_read": ["pandas is still splitting on the wrong character, so you get the wrong number of columns. Check your sep=."], "clean": ["Row 0 should be a real reading and the footer should be gone. Look at df.head(2) and df.tail(2).", "Both junk rows have to go: the second header line at the top and the footer at the bottom. One slice can do both.", "Did you keep Date and Start Time as text with dtype=? Compare with the worked example above."], "datetime": ["pandas could not parse it, or parsed it wrong. Compare your format to the glued text, character by character.", "Every piece of the text needs a code from the table, and the colon is typed as a colon."], "numeric": ["Sample Value should be numbers, with blanks as NaN. to_numeric() has an errors= option for values that are not numbers.", "You want anything that is not a number to become NaN. Then count the NaNs with .isna().sum()."], "stretch_a": ["Group by Site ID, then count the missing readings (isna().sum()) inside each group. Then find the largest."], "sites": ["You want each Site ID exactly once. Try a pandas method whose name means 'one of a kind'."], "loop": ["The plot should have one line per site. Is your loop plotting every site, or only one?"], "hourly": ["For the hourly mean, group by the full timestamp column itself, then take the mean of Sample Value.", "Compare with the daily mean in the worked example above. What do you group by instead of the date?"], "labels": ["An unlabeled axis is the most common mistake in air quality charts. Give the y-axis a label with units, and the plot a title."], "june": ["The plot is not zoomed to June. set_xlim() takes two timestamps.", "The end is the first day AFTER the month you want."], "stretch_b": ["Find the row of hourly_mean with the largest Sample Value. idxmax() gives you its position."], "ai_diff": ["The two rules only disagree for days that sit exactly on the boundary. How would you count the days where the two answers differ?"], "naaqs24": ["It is a whole number between 30 and 40, in µg/m³.", "Look for the primary 24-hour PM2.5 standard in the EPA NAAQS table."], "exceed": ["Keep the rows of daily_valid where daily_mean is greater than your standard, then count them."], "p98": ["quantile() takes a fraction of 1, not a percent. For each site, take the quantile of its daily means, then look at the highest one.", "Compare with the named aggregation in the worked example above."], "bar": ["There should be one bar per site. Did you plot every row of site_summary?"], "annual": ["It is a single-digit number, lower than the 24-hour one.", "Look for the primary annual PM2.5 standard in the EPA NAAQS table."], "annual_top": ["The annual mean is the average of each site's valid daily means. Group by Site ID, take the mean of daily_mean, and look at the highest."], "is_over": ["The pattern is name = value. For the last line, the right side is a comparison with >.", "A comparison gives back True or False."], "rounded": ["round() takes two arguments: the number, then how many decimal places."], "label": ["The text goes on the left of the dot, then .replace(...). Inside the parentheses: what to find, then what to put there.", "Copy the µ character from the question."], "columns": ["It has the same shape as .replace(), with one argument: text.split(\"...\")"], "name_of_c": ["A dictionary takes the label in quotes: site_names[...]"], "second_reading": ["A list takes a position with no quotes, and the first position is 0."], "highest": ["Start from df[\"Sample Value\"]. Which method gives the largest value?"], "n_over_12": ["Filter first: df[df[\"Sample Value\"] > 12]. Then put that inside len(...)."], "lowest_site": ["idxmax() returns the label of the largest. What is the matching method for the smallest?"], "n_high": ["Start n_high at 0 outside the loop. Inside: for x in pm_readings, then an if x > 35, then add 1.", "Each level of indentation means inside the line above it."], "kw_args": ["A keyword argument has the shape name=value. Count those.", "The two things before them are positional: the x values and the y values."], "fix_add": ["int(\"365\") turns the text into the number 365.", "Put that where the text was: 365 + int(...)."], "names": ["Test them: run 2nd_site = 1 in a new cell and read the message.", "Rule out names that start with a digit, contain a symbol or a space, or are reserved words."], "swap": ["The right side is worked out before anything is stored. What does (high, low) give you?", "Assign both names at once: low, high = ..., ..."], "float_conv": ["float(\"41.2\") gives the number 41.2.", "Add 10 to that."], "label_text": ["+ joins text to text. A number has to be converted first: str(value).", "The pieces are \"Site \", site, \": \" and str(value)."], "county": ["Count the positions: 2 is the first dash, so the county starts at position 3.", "stop is the first item you do not want. The county ends before the second dash, at position 6."], "site_number": ["A negative start counts from the end: site_id[-4:]. Then convert it with int()."], "copy": ["Lists carry a method that makes a copy. Its name says what it does.", "readings.copy()"], "unpack": ["You met this in 3.1: several names on the left of the =.", "The right side is the tuple itself."], "season11": ["Only one line of the loop depends on the month. Which one?", "Use a new name for the answer (season11) so it does not overwrite found."], "dict_add": ["Assigning to a key that does not exist yet creates it: site_names[\"...\"] = ..."], "divmod": ["// gives the whole days. % gives what is left over."], "case_cmp": ["A comparison with == gives True or False. Text comparisons are case sensitive."], "valid_range": ["Two comparisons joined by and: reading >= 0 and reading <= 500.", "Write the pattern once for reading_a, then again for reading_b."], "wind_band": ["The shape is the worked example's: if, then elif, then else, each ending with a colon and followed by an indented line.", "Check the order: the smaller threshold must come first."], "total_high": ["Set total_high = 0 before the loop, outside it.", "Inside the loop, the if tests the reading and the indented line under it adds it to the total."], "first_over_70": ["Loop over episode. Inside, test x > 70.", "When the test is True: store x, then break. Both lines go inside the if."], "countdown": ["range() takes a third argument, the step. A negative step counts down.", "The stop is the first number you do not want, so what should it be to include 1?"], "peaks": ["Start with an empty dictionary, then loop over readings.items().", "Inside the loop, store max(values) under the key site."], "flagged": ["Start with an empty list. Loop over report.items().", "Inside the loop, an if tests the count, and flagged.append(site) goes under the if."]}
_tries, _locked, _score = {}, {}, {}


def _norm(v):
    if isinstance(v, bool):
        return str(v)
    if isinstance(v, (int, float, np.integer, np.floating)):
        return f"{float(v):g}"
    return str(v).strip()


def _h(v):
    return hashlib.sha256(_norm(v).encode()).hexdigest()[:12]


def check(name, value):
    """Is your result right? Wrong results get a nudge, never the answer."""
    try:
        good = _h(value) == _KEY[name]
    except Exception:
        good = False
    if good:
        print("✅ Correct.")
        return
    n = _tries.get(name, 0)
    _tries[name] = n + 1
    hints = _HINTS[name]
    print("🔁 Not yet.", hints[min(n, len(hints) - 1)])


def lock(name, choice):
    """Commit to a prediction BEFORE you see the result."""
    if choice is None:
        print("✍️ Type your prediction on the line above (replace None), then run this cell again.")
        return
    _locked[name] = choice
    print(f"🔒 Locked in: {choice!r}. Now do the work and see what actually happens.")


def reveal(name, actual):
    """After the real code has run: compare it with the prediction you locked in."""
    if name not in _locked:
        print("🔒 There is no locked-in prediction. Go back, make one, and lock it first. That is the whole point.")
        return
    choice = _locked[name]
    print(f"   Your prediction: {choice!r}     What happened: {actual!r}")
    _score[name] = choice == actual
    print("   You called it." if choice == actual else "   Different from your prediction. What did you expect to see, and why?")


def scorecard():
    """How did your predictions go?"""
    if not _score:
        print("No predictions yet.")
        return
    print(f"You called {sum(_score.values())} of {len(_score)} predictions.")


def load_clean_table(path_to_file):
    """A ready-made clean table, for when you are stuck or arrived late. No shame: this is what it is for.

    It does what Block A builds: reads the file, drops the two junk rows, builds Datetime, makes Sample Value numeric.
    """
    df = pd.read_csv(path_to_file, sep="|", header=[0], low_memory=False,
                     dtype={"Date": str, "Start Time": str})[1:-1]
    df["Datetime"] = pd.to_datetime(df["Date"] + df["Start Time"], format="%Y%m%d%H:%M")
    df["Sample Value"] = pd.to_numeric(df["Sample Value"], errors="coerce")
    print(f"📦 Loaded the clean table: {df.shape[0]:,} rows. You can continue from here.")
    return df

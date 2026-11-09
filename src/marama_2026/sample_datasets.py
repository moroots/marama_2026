"""Small real datasets for the MARAMA 2026 tutorial.

    from marama_2026 import sample_datasets as sd
    df = sd.load_aqs_pm25()

Each load_* function returns something ready to use (a DataFrame, an xarray
Dataset, ...). The files live in the repository's data/ folder. The first call
downloads a file from GitHub into ~/.cache/marama_2026; after that it is read
from disk.
"""

import urllib.request
from pathlib import Path

BASE_URL = "https://raw.githubusercontent.com/moroots/marama_2026/main/data/"
CACHE_DIR = Path.home() / ".cache" / "marama_2026"


def _fetch(name):
    """Return the local copy of data/<name>, downloading it the first time."""
    in_repo = Path(__file__).resolve().parents[2] / "data" / name     # only exists in a repo checkout (editable install)
    if in_repo.is_file():
        return in_repo
    local = CACHE_DIR / name
    if not local.exists():
        local.parent.mkdir(parents=True, exist_ok=True)
        part = local.with_name(local.name + ".part")
        try:
            urllib.request.urlretrieve(BASE_URL + name, part)
        except Exception as err:
            part.unlink(missing_ok=True)
            raise RuntimeError(f"Could not download {name} from {BASE_URL}. Check your internet connection.") from err
        part.replace(local)
    return local


# ---- Session 2: surface PM2.5 ------------------------------------------------

def load_aqs_pm25():
    """AQS hourly PM2.5 for 2025 at 8 Allegheny County, PA monitors (a DataFrame, one row per hour)."""
    import pandas as pd

    df = pd.read_csv(_fetch("session_2/AMP501_2420560-0.txt"), sep="|", skiprows=[1], dtype=str,
                     low_memory=False).iloc[:-1]
    df["Sample Value"] = pd.to_numeric(df["Sample Value"])
    df["Datetime"] = pd.to_datetime(df["Date"] + df["Start Time"], format="%Y%m%d%H:%M")
    return df


def load_epa_daily_pm25():
    """EPA's pre-generated daily PM2.5 file for 2025, eight mid-Atlantic states (a DataFrame)."""
    import pandas as pd

    return pd.read_parquet(_fetch("epa_daily_pm25_2025_midatlantic.parquet"))


# ---- Session 3: tools for atmospheric science -------------------------------

def load_geos_cf():
    """GEOS-CF model PM2.5, NO2 and O3 over the mid-Atlantic, August 2025 (an xarray Dataset)."""
    import xarray as xr

    return xr.open_dataset(_fetch("session_3/geos_cf_midatlantic_aug2025.nc"))


def load_states():
    """Mid-Atlantic state outlines (a GeoPandas GeoDataFrame)."""
    import geopandas as gpd

    return gpd.read_file(_fetch("session_3/states_midatlantic.geojson"))


def load_monitors_pm25():
    """Daily PM2.5 at 151 EPA monitors, 2025 (a DataFrame)."""
    import pandas as pd

    return pd.read_parquet(_fetch("session_3/pm25_daily_monitors_2025.parquet"))


def load_sounding_kiad():
    """Weather-balloon sounding from Sterling, VA (KIAD), 6 Aug 2025 12 UTC (a DataFrame)."""
    import pandas as pd

    return pd.read_csv(_fetch("session_3/sounding_KIAD_2025-08-06_12Z.csv"))


def load_arm_met():
    """ARM surface meteorology, SGP site, 1 Jan 2019 (an xarray Dataset, read with ACT)."""
    import act

    return act.io.read_arm_netcdf(str(_fetch("session_3/sgpmetE13.b1.20190101.000000.cdf")))


def load_asos():
    """Hourly airport weather at BWI, IAD and DCA, 5 to 6 Aug 2025 (a DataFrame)."""
    import pandas as pd

    return pd.read_parquet(_fetch("session_3/asos_bwi_iad_dca_2025-08-05_06.parquet"))


def load_tempo_no2():
    """TEMPO satellite tropospheric NO2 pixels over the mid-Atlantic, 20 Oct 2026 (a DataFrame)."""
    import pandas as pd

    return pd.read_parquet(_fetch("session_3/tempo_no2_2026-10-20_midatlantic.parquet"))


def load_tolnet():
    """TOLNet lidar ozone profiles, 28 to 31 Jul 2025 (a dict: date text -> DataFrame of profiles x altitude)."""
    import pandas as pd

    profiles = pd.read_parquet(_fetch("session_3/tolnet_smol2_hartmiller_20250728_31.parquet"))
    profiles.columns = profiles.columns.astype(float)       # the altitude labels were saved as text
    return {day: frame for day, frame in profiles.groupby(profiles.index.strftime("%Y-%m-%d"))}

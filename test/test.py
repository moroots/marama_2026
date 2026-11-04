# %% 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

# Here we define the path to the data file as a string (str)
# Notice the 'r' in from of the quotes, this tells the computer
# to ignore spetial characters and read it as a string
path_to_file = r"/mnt/workspace/projects/tutorials/marama_2026/data/AMP501_2420560-0.txt"

if not isinstance(path_to_file, Path):
    if isinstance(path_to_file, str): 
        path_to_file = Path(path_to_file)
    else: 
        raise TypeError("path must be of type string or Path")

if not path_to_file.is_file():
    raise FileNotFoundError(f"The file {path_to_file.resolve()} could not be found on this machine")

# First we try to naively import the file using 'pandas.read_csv()'
# It shouldn't work exactly as you want it
df = pd.read_csv(path_to_file)

# .read_csv() can import more delimeter types than ','
df = pd.read_csv(path_to_file, sep="|")

# A DtypeWarning means that the data have conflicting datatypes
# This is definetely caused by the two header lines
df = pd.read_csv(path_to_file, sep="|", skiprows=2, header=[1], low_memory=False)
"""
Load all simulation field CSV files
"""

from pathlib import Path

import pandas as pd

#location of my data, for now it's the fields data from autohgs outputs that I've imported here
#NOTE: In future, add workflow for automatically loading fields data here?
FIELDS_DIR = Path(__file__).resolve().parents[1] / "autohgs" / "fields"

#load data func.
def load_data(data_dir = FIELDS_DIR):
    # files from fields_dir
    files = sorted(Path(data_dir).glob("case_*.csv"))
    #file not found error if no csvs exist, shouldn't be an issue
    if not files:
        raise FileNotFoundError(f"No case CSV files found in {data_dir}")

    #init. frames list
    frames = []
    #for loop to load all files
    for file in files:
        #add to frame
        frame = pd.read_csv(file)

        #file.stem is the filename without the extension
        frame["case_id"] = file.stem
        #add frame to frames list
        frames.append(frame)

    #return my list
    return pd.concat(frames, ignore_index = True)

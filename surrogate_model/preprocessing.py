"""
prep. model inputs + salinity values; may ned to change later
"""

from .data import load_data

def preprocess_data():
    data = load_data()
    X = data[["x", "z"]]
    y = data["salinity"]
    return X, y
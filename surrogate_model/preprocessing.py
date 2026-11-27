"""Build one LSE-profile input and one salt-front target per simulation."""

import pandas as pd

from .data import load_data

SALT_FRONT_THRESHOLD = 17.5


def profile_to_features(profile):
    required = {"x", "land_surface_elevation"}
    if not required.issubset(profile.columns):
        raise ValueError(f"LSE profile must contain columns: {sorted(required)}")
    if profile[["x", "land_surface_elevation"]].isna().any().any():
        raise ValueError("LSE profile contains missing x or elevation values")

    elevations_per_x = profile.groupby("x")["land_surface_elevation"].nunique()
    if elevations_per_x.gt(1).any():
        raise ValueError("Each x must have exactly one land-surface elevation")

    elevations = profile.groupby("x")["land_surface_elevation"].first().sort_index()
    features = {f"lse_at_x_{x:g}": elevation for x, elevation in elevations.items()}
    return pd.DataFrame([features])


def _salt_front_x(simulation, threshold=SALT_FRONT_THRESHOLD):
    if simulation["salinity"].isna().any():
        raise ValueError("Simulation contains missing salinity values")

    salinity_by_x = simulation.groupby("x")["salinity"].max().sort_index()
    crossings = []
    points = list(salinity_by_x.items())
    for (left_x, left_salinity), (right_x, right_salinity) in zip(
        points, points[1:]
    ):
        if left_salinity >= threshold and right_salinity < threshold:
            crossing = left_x + (
                (threshold - left_salinity)
                * (right_x - left_x)
                / (right_salinity - left_salinity)
            )
            crossings.append(crossing)

    if not crossings:
        raise ValueError(
            f"No inland salinity crossing found for the {threshold:g} PSU threshold"
        )
    return max(crossings)


def preprocess_data(data_dir=None):
    data = load_data() if data_dir is None else load_data(data_dir)
    feature_rows = []
    front_positions = []
    expected_columns = None

    for case_id, simulation in data.groupby("case_id", sort=True):
        if "time_days" in simulation and simulation["time_days"].nunique() != 1:
            raise ValueError(
                f"{case_id} contains multiple times; select one simulation time first"
            )

        features = profile_to_features(simulation)
        columns = list(features.columns)
        if expected_columns is None:
            expected_columns = columns
        elif columns != expected_columns:
            raise ValueError(f"{case_id} uses a different x grid")

        feature_rows.append(features)
        front_positions.append(_salt_front_x(simulation))

    X = pd.concat(feature_rows, ignore_index=True)
    y = pd.Series(front_positions, name="salt_front_x")
    return X, y

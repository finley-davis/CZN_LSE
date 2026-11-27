"""Predict a salt-front position from a new LSE profile."""

from .preprocessing import profile_to_features


def predict_salt_front(model, lse_profile):
    features = profile_to_features(lse_profile)
    expected_columns = list(model.feature_names_in_)
    if list(features.columns) != expected_columns:
        raise ValueError("LSE profile must use the same x coordinates as the training data")
    return float(model.predict(features)[0])
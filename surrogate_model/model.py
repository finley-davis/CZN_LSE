"""Model for predicting salt-front position from an LSE profile."""

from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def make_model():
    return make_pipeline(StandardScaler(), Ridge(alpha=1.0))

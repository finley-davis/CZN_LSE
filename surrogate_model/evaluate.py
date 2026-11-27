"""
Calculate and report metrics
"""

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import LeaveOneOut, cross_val_predict


def evaluate_model(model, X, y):
    y_pred = cross_val_predict(model, X, y, cv=LeaveOneOut())
    mae = mean_absolute_error(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    return mae, mse, r2
"""
loading, splitting, fitting. Making a pipeline
"""

from .model import make_gpr
from .preprocessing import preprocess_data

X, y = preprocess_data()
model = make_gpr()
model.fit(X, y)

#run dis
import pandas as pd
from .predict import predict_salinity

#predicts salinity at these coords.
new_points = pd.DataFrame({"x": [0], "z": [-10]})
#outputs preds.
predictions = predict_salinity(model, new_points)
print(predictions)
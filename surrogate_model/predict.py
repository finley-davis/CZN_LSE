"""
Make predictions for new inputs, this is how i'm going to understand the mechanisms behind microtopgraphy salinity differences
"""

def predict_salinity(model, new_points):
    return model.predict(new_points[["x", "z"]])
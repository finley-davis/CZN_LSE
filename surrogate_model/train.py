"""
loading, splitting, fitting. Making a pipeline
"""

from .model import make_gpr
from .preprocessing import preprocess_data

X, y = preprocess_data()
model = make_gpr()
model.fit(X, y)


#NOTE: To run: python3 -m surrogate_model.train; This takes forever...
#I call it like this because I am using relative import, so I run it as a module from the repo root, rather than as a file

This model predicts one salt-front x position per simulation from the simulation's
land-surface-elevation (LSE) profile.

Run from the repository root:

```sh
python3 -m surrogate_model.train
```

Each case CSV contributes one training example. The 13 vertical mesh rows at each
x are collapsed to one LSE value; the salt-front target is the inland 17.5 PSU
crossing, found from the maximum salinity in each vertical column and linearly
interpolated between x coordinates. The script reports leave-one-case-out
metrics before fitting the model on all cases. To use the fitted estimator in
Python:

```python
import pandas as pd

from surrogate_model.predict import predict_salt_front
from surrogate_model.train import train_model

model = train_model()
profile = pd.read_csv("new_lse_profile.csv")
front_x = predict_salt_front(model, profile)
```

The profile must contain `x` and `land_surface_elevation` columns on the same
x grid as the training cases.

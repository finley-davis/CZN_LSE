"""Train and evaluate the salt-front model."""

from .evaluate import evaluate_model
from .model import make_model
from .preprocessing import preprocess_data


def train_model():
    X, y = preprocess_data()
    mae, mse, r2 = evaluate_model(make_model(), X, y)
    model = make_model().fit(X, y)

    print(f"Training cases: {len(X)}")
    print(f"Leave-one-case-out MAE: {mae:.3f} m")
    print(f"Leave-one-case-out MSE: {mse:.3f} m^2")
    print(f"Leave-one-case-out R^2: {r2:.3f}")
    return model


if __name__ == "__main__":
    train_model()
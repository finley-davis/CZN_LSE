"""
make GPR kernel and estimator
"""

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

from .config import Config

#create gpr model
def make_gpr():
    # load in params. from config
    config = Config()
    #init. model
    model = GaussianProcessRegressor(
        kernel = RBF(),
        alpha = config.alpha,
        n_restarts_optimizer = config.n_restarts_optimizer,
        random_state = config.random_state,
    )
    return model
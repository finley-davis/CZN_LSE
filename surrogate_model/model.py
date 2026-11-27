"""
make GPR kernel and estimator
"""

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

from sklearn.ensemble import RandomForestRegressor

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


#create RF model, GPR is very slow
#add this to config later, gonna have to reorgianize. just hardcoded for now
def make_rf():
    return RandomForestRegressor(
        #tells the model how many trees to use, more trees = better performance but slower
        n_estimators = 100,
        #reproducibility, same random seed = same results
        random_state = 322,
        #tells the model how many cores to use, -1 = use all available cores
        n_jobs = -1,
    )


#could add more models here, like XGBoost or LightGBM, but for now just GPR and RF. Potentially KNN too.
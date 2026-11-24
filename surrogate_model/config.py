"""
Configuration for the surrogate model. I'm gonna use Gaussian Process Regression (GPR).

The config file will contain the hyperparameters for the GPR model, as well as any other relevant settings

Other files will be used to load the data, train the model, and make predictions. The config file will be imported into those files to access the hyperparameters and settings

"""


class Config:
    #default parameter values
    def __init__(self):
        # Hyperparameters for the GPR model
        self.kernel = "RBF"  #radial Basis Function kernel
        self.alpha = 1e-10  # noise level
        self.n_restarts_optimizer = 10  #number of restarts for optimizer

        # Other settings
        self.random_state = 322  #random seed for reproducibility

    #return params. as dict.
    def get_config(self):
        return {
            "kernel": self.kernel,
            "alpha": self.alpha,
            "n_restarts_optimizer": self.n_restarts_optimizer,
            "random_state": self.random_state
        }

    #option to set params. myself
    def set_config(self, kernel = None, alpha = None, n_restarts_optimizer = None, random_state = None, verbose = None):
        if kernel is not None:
            self.kernel = kernel
        if alpha is not None:
            self.alpha = alpha
        if n_restarts_optimizer is not None:
            self.n_restarts_optimizer = n_restarts_optimizer
        if random_state is not None:
            self.random_state = random_state
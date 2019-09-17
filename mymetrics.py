import numpy as np
from sklearn.metrics import make_scorer, mean_squared_log_error

def rmsle(y_true, y_pred):
    return np.sqrt(mean_squared_log_error(y_true, y_pred))

root_mean_squared_log_error = make_scorer(rmsle, greater_is_better=False)
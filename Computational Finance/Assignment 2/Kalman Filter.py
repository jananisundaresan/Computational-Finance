
from __future__ import division, absolute_import, print_function

import numpy as np
import statsmodels.api as sm

class LocalLinearTrend(sm.tsa.statespace.MLEModel):
    def __init__(self, endog, **kwargs):
        # Model order
        k_states = k_posdef = 2

        # Initialize the statespace
        super(LocalLinearTrend, self).__init__(
            endog, k_states=k_states, k_posdef=k_posdef, **kwargs
        )

        # Initialize the matrices
        self['design'] = np.r_[1, 0]
        self['transition'] = np.array([[1, 1],
                                       [0, 1]])
        self['selection'] = np.eye(k_states)

        # Initialize the state space model as approximately diffuse
        self.initialize_approximate_diffuse()
        # Because of the diffuse initialization, burn first two
        # loglikelihoods
        self.loglikelihood_burn = 2
        
        # Cache some indices
        idx = np.diag_indices(k_posdef)
        self._state_cov_idx = ('state_cov', idx[0], idx[1])
        
        # Setup parameter names
        self._param_names = ['sigma2.measurement', 'sigma2.level', 'sigma2.trend']

    @property
    def start_params(self):
        # Simple start parameters: just set as 0.1
        return np.r_[0.1, 0.1, 0.1]

    def transform_params(self, unconstrained):
        # Parameters must all be positive for likelihood evaluation.
        # This transforms parameters from unconstrained parameters
        # returned by the optimizer to ones that can be used in the model.
        return unconstrained**2

    def untransform_params(self, constrained):
        # This transforms parameters from constrained parameters used
        # in the model to those used by the optimizer
        return constrained**0.5

    def update(self, params, **kwargs):
        # The base Model class performs some nice things like
        # transforming the params and saving them
        params = super(LocalLinearTrend, self).update(params, **kwargs)

        # Extract the parameters
        measurement_variance = params[0]
        level_variance = params[1]
        trend_variance = params[2]

        # Observation covariance
        self['obs_cov', 0, 0] = measurement_variance

        # State covariance
        self[self._state_cov_idx] = [level_variance, trend_variance]
        
        
        
import pandas as pd
from datetime import datetime
# Load Dataset
df = pd.read_csv("C:/users/Janani/Desktop/2019/Computational Finance/Assignment 2/GSPC.csv")
#df.columns = ['date', 'nf', 'ff']
df['day']=df['Date']


#df.index = pd.date_range(start=datetime(df.date[0].date(), 1, 1), end=datetime(df.iloc[-1, 0], 1, 1), freq='AS')
df.index=df['day']
# Log transform
df['lff'] = np.log(df['Adj Close'])

# Setup the model
mod = LocalLinearTrend(df['lff'])

# Fit it using MLE (recall that we are fitting the three variance parameters)
res = mod.fit()
print(res.summary())


import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10,4))

# Perform dynamic prediction and forecasting
ndynamic = 5
predict_res = res.get_prediction(alpha=0.05, dynamic=df['lff'].shape[0]-ndynamic)

predict = predict_res.predicted_mean
ci = predict_res.conf_int(alpha=0.05)

# Plot the results
ax.plot(df['lff'], 'k.', label='Actual Prediction');
ax.plot(df.index[:-ndynamic], predict[:-ndynamic], label='Auto Regressive Prediction');
ax.plot(df.index[:-ndynamic], ci.iloc[:-ndynamic], 'k--', alpha=0.5);

ax.plot(df.index[-ndynamic:], predict[-ndynamic:], 'r', label='Kalman Filter Prediction');
ax.plot(df.index[-ndynamic:], ci.iloc[-ndynamic:], 'k--', alpha=0.5);

# Cleanup the image
ax.set_ylim((6, 8));
props = {"rotation" : 90}
plt.setp(ax.get_xticklabels(), **props)
legend = ax.legend(loc='upper right');
legend.get_frame().set_facecolor('w')
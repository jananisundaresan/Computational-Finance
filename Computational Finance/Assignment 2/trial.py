
import numpy as np
import scipy.stats as si
import sympy as sy

import pandas as pd
import random

from pandas. plotting import scatter_matrix
from scipy.stats import skew
from scipy.stats import kurtosis

import time
import datetime as dt
from math import sqrt, pi


# import numpy, pyplot and scipy
import numpy as np
import matplotlib as mat
mat.style.use('ggplot')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy
from scipy.stats import norm
from scipy.optimize import brentq
from scipy.interpolate import interp1d

# import pandas
import pandas
# new in 0.17.1
from pandas_datareader import data as pd

import math
# underlying stock price
S = 7030.46
# series of underlying stock prices to demonstrate a payoff profile
#S_ = np.arange(40.0, 50.0, 0.01)

# strike price
K = 4800

# time to expiration (you'll see this as T-t in the equation)
t = 70.0

# risk free rate (there's nuance to this which we'll describe later)
r = 1.359

# volatility (latent variable which is the topic of this talk)
vol = 0.12

def N(z):
    """ Normal cumulative density function

    :param z: point at which cumulative density is calculated 
    :return: cumulative density under normal curve
    """
    return norm.cdf(z)


def black_scholes_call_value(S, K, r, t, vol):
    """ Black-Scholes call option

    :param S: underlying
    :param K: strike price
    :param r: rate
    :param t: time to expiration
    :param vol: volatility
    :return: BS call option value
    """
    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)
    d2 = d1 - (vol * np.sqrt(t))
    
    return N(d1) * S - N(d2) * K * np.exp(-r * t)

def black_scholes_put_value(S, K, r, t, vol):
    """ Black-Scholes put option

    :param S: underlying
    :param K: strike price
    :param r: rate
    :param t: time to expiration
    :param vol: volatility
    :return: BS put option value
    """
    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)
    d2 = d1 - (vol * np.sqrt(t))
    
    return N(-d2) * K * np.exp(-r * t) - N(-d1) * S



print ('Black-Scholes call value %0.2f' % black_scholes_call_value(S, K, r, t, vol))
print( 'Black-Scholes put value %0.2f' % black_scholes_put_value(S, K, r, t, vol))



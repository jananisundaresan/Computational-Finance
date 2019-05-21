from math import *
import math
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
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
from scipy.stats import norm
# import numpy, pyplot and scipy
import matplotlib as mat
mat.style.use('ggplot')
from mpl_toolkits.mplot3d import Axes3D
import scipy
from scipy.optimize import brentq
from scipy.interpolate import interp1d
from scipy import log,exp,sqrt,stats
from math import sqrt, exp, log, pi

def d(sigma, S, K, r, t):
    d1 = 1 / (sigma * sqrt(t)) * ( log(S/K) + (r + sigma**2/2) * t)
    d2 = d1 - sigma * sqrt(t)
    return d1, d2

def call_price(sigma, S, K, r, t, d1, d2):
    C = norm.cdf(d1) * S - norm.cdf(d2) * K * exp(-r * t)
    return C
d(0.13,6765.94,4800,1.2,0.18)
call_price(0.13,6765.94,4800,1.2,0.18,10.16,10.11)
S =6765
K = 4800.0
r = 1.2
t = 0.18
C0 = 1935

vol = 0.5
epsilon = 1.0          #  Define variable to check stopping conditions
abstol = 1e-4          #  Stop calculation when abs(epsilon) < this number

i = 0                  #  Variable to count number of iterations
max_iter = 1e3   

while epsilon > abstol:
    #  if-statement to avoid getting stuck in an infinite loop.
    if i > max_iter:
        print ('Program failed to find a root.  Exiting.')
        break

    i = i + 1
    orig = vol
    d1, d2 = d(vol, S, K, r, t)
    function_value = call_price(vol, S, K, r, t, d1, d2) - C0
    vega = S * norm.pdf(d1) * sqrt(t)
    vol = -function_value/vega + vol
    epsilon = abs(function_value)

print ('Implied volatility = ',  vol)
print ('Code required', i, 'iterations.')

#d(0.8,6728,4800,1.2,0.18)
#call_price(0.8,6728,4800,1.2,0.18,1.8,1.4)
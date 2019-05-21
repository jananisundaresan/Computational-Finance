# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 13:31:12 2019

@author: Janani
"""


import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from pandas. plotting import scatter_matrix
from scipy.stats import skew
from scipy.stats import kurtosis
import pandas as pd
from numpy import sqrt,mean,log,diff
import quandl



import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/Janani/Desktop/2019/Computational Finance/Assignment 2/Newdata.csv")
#df = pd.read_table('callputoptionprices/c2925.prn', delim_whitespace=True, header=None, names=['data', 'price', 'value'])
df.head()

# Compute the logarithmic returns using the Closing price 
df['Log_Ret'] = np.log(df['FTSE'] / df['FTSE'].shift(1))
df.head()
historical_vol_daily = std(df['Log_Ret'])  

df['Volatility'] = (df['Log_Ret'].rolling(66).std())  *100

print(df.tail())


min_periods = 66
   # calculate the volatility
vol = pd.stats.moments.rolling_std(df['Log_Ret'], min_periods) * \
           np.sqrt(min_periods)
   # plot it
vol.plot(figsize=(10, 8));

import math
def phi(x):
    return math.exp(-x * x / 2.0) / math.sqrt(2.0 * math.pi)

#-----------------------------------------------------------------------

# Return the value of the Gaussian probability function with mean mu
# and standard deviation sigma at the given x value.

def pdf(x, mu=0.0, sigma=1.0):
    return phi((x - mu) / sigma) / sigma

#-----------------------------------------------------------------------

# Return the value of the cumulative Gaussian distribution function
# with mean 0.0 and standard deviation 1.0 at the given z value.

def Phi(z):
    if z < -8.0: return 0.0
    if z >  8.0: return 1.0
    total = 0.0
    term = z
    i = 3
    while total != total + term:
        total += term
        term *= z * z / float(i)
        i += 2
    return 0.5 + total * phi(z)

#-----------------------------------------------------------------------

# Return standard Gaussian cdf with mean mu and stddev sigma.
# Use Taylor approximation.

def cdf(z, mu=0.0, sigma=1.0):
    return Phi((z - mu) / sigma)

#-----------------------------------------------------------------------

# Black-Scholes formula.

def callPrice(s, x, r, sigma, t):
    a = (math.log(s/x) + (r + sigma * sigma/2.0) * t) / \
        (sigma * math.sqrt(t))
    b = a - sigma * math.sqrt(t)
    return s * cdf(a) - x * math.exp(-r * t) * cdf(b)


s =  7034.0
x = 4800.0
r = 1.13
sigma = 0.12
t = 66
print(callPrice(s, x, r, sigma, t))
# df['a'] = (math.log(s/x) + (r + sigma * sigma/2.0) * t) / \
#         (sigma * math.sqrt(t))

df.head()


bs = []
for i in range(len(df)):
    bs.append(callPrice(df.iloc[i]['FTSE'], 4800.0, df.iloc[i]['Rate'], df.iloc[i]['Volatility'], t))
    
    
bs = pd.DataFrame(bs)
bs.tail()

bs.plot()


df.iloc[66:]['Volatility'].head()


pd.concat([df, bs], axis=1)

#volatility
import pandas as pd
from numpy import sqrt,mean,log,diff

# use the daily data of Google(NASDAQ: GOOG) from 01/2016 to 08/2016
close = df['FTSE']
r = diff(log(close))
r_mean = mean(r)
diff_square = [(r[i]-r_mean)**2 for i in range(0,len(r))]
std = sqrt(sum(diff_square)*(1.0/(len(r)-1)))
vol = std*sqrt(260)
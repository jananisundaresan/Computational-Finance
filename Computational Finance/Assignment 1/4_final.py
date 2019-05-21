# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 20:46:07 2019

@author: Janani
"""

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from pandas. plotting import scatter_matrix
from scipy.stats import skew
from scipy.stats import kurtosis
#from pylab import rcParams
#rcParams['figure.figsize'] = 2,2

data=pd.read_csv("C:/Users/Janani/Desktop/2019/Computational Finance/Assignment 1/prices.csv")
data.index=data['Date']
data=data.iloc[:,1:]
#data=data[['GVC','GLEN','NMC']] #27
#data=data[['GVC','SLA','NMC']] #28.38
#data=data[['RR','STAN','NMC']]  #42.73
data=data[['GVC','STAN','NMC']]  #43.88


#split data into 2 
data1=data.iloc[:506,:]
data2=data.iloc[506:,:]

daily_simple_returns = data1.pct_change()
daily_simple_returns.head()
daily_simple_returns.plot()
plt.xticks(rotation=90)
plt.title("Daily Returns")


#mean return daily
mean_return_daily=np.mean(daily_simple_returns)*100
#daily_return = (np.sum(daily_simple_returns)/len(daily_simple_returns))*100
#visaulize the change
#plt.hist(daily_simple_returns.dropna(),bins=10,density=False)
#plt.show()

corrs_12=daily_simple_returns.corr()
corrs_12
plt.matshow(corrs_12)
plt.xticks(range(len(daily_simple_returns.columns)),((daily_simple_returns.columns)),rotation=90)
plt.yticks(range(len(daily_simple_returns.columns)),daily_simple_returns.columns)
plt.colorbar()
plt.show()
annual_returns = mean_return_daily * 252
annual_returns

sigma_daily = np.std(daily_simple_returns)
print(sigma_daily)

# Calculate the daily variance
variance_daily = sigma_daily**2
print(variance_daily)

kurt = kurtosis(daily_simple_returns.dropna())
skew = skew(daily_simple_returns.dropna())

d=pd.concat([mean_return_daily,sigma_daily,variance_daily],axis=1)
d.columns=['Mean Return (Daily)%','Standard Deviation','Variance']
weights = np.random.random(3)
weights = weights / sum(weights)
weights

print(np.sum(weights))

WeightedReturns = (daily_simple_returns).mul(weights, axis=1)

# Calculate the portfolio returns
re = WeightedReturns.sum(axis=0)
print(str(round(re * 100, 2)) + '%')


#along colusmn
#port_returns_expected = np.sum(weights * daily_simple_returns)
#print(str(round(port_returns_expected * 100, 2)) + '%')

# Plot the cumulative portfolio returns over time
CumulativeReturns = ((1+re).cumprod()-1)
CumulativeReturns.plot()
plt.xticks(rotation=90)
plt.title("Cumulative Portfolio Return over time")
plt.show()

#1/N Naive portfolio

# How many stocks are in your portfolio?
numstocks = 3

# Create an array of equal weights across all assets
portfolio_weights_ew = np.repeat(1/numstocks, numstocks)

# Calculate the equally-weighted portfolio returns
StockReturns.iloc[:, 0:numstocks].mul(portfolio_weights_ew, axis=1).sum(axis=1)
cumulative_returns_plot(['Portfolio', 'Portfolio_EW'])
#
##standard deviation
#import math
#np.sum(daily_simple_returns.rolling(window=252).std()) * math.sqrt(252)

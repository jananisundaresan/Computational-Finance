# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:23:33 2019

@author: Janani
"""

import numpy as np

from pandas_datareader import data as wb

import matplotlib.pyplot as plt

from scipy import stats

import statsmodels.api as sm

import pandas as pd

from scipy.stats import norm
def d1(S,K,r,stdev,T):

    return (np.log(S/K)+(r+stdev**2/2)*T)/(stdev*np.sqrt(T))

def d2(S,K,r,stdev,T):

    return (np.log(S/K)+(r-stdev**2/2)*T)/(stdev*np.sqrt(T))

    

norm.cdf(0) #cumm dist of a standard normal dist at points below 0 which is 0.5

norm.cdf(0.25)

norm.cdf(0.75)



def BSM(S,K,r,stdev,T):

    return(S*norm.cdf(d1(S,K,r,stdev,T)))-(K*np.exp(-r*T)*norm.cdf(d2(S,K,r,stdev,T)))



ticker = 'GSPC'

#data = pd.DataFrame()

data=pd.read_csv("C:/Users/Janani/Desktop/2019/Computational Finance/Assignment 2/Newdata.csv")
#data.set_index('Date', inplace=True)
data=data[['FTSE']]
#data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2005-1-1',end='2017-3-21')['Adj Close']



S = 7034




log_returns = np.log(1+data.pct_change())



stdev = log_returns.std()*260**0.5



r = 1.1

K = 4800.0

T = 66



print(d1(S,K,r,stdev,T))

print(d2(S,K,r,stdev,T))

print(BSM(S,K,r,stdev,T))



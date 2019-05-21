# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 19:23:38 2019

@author: Janani
"""


import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from pandas. plotting import scatter_matrix
from scipy.stats import skew
from scipy.stats import kurtosis

data=pd.read_csv("C:/Users/Janani/Desktop/2019/Computational Finance/Assignment 1/prices.csv")
data.index=data['Date']
data=data.iloc[:,1:]
data=data[['GVC','STAN','NMC']]  #43.88

#Correlation Matrix for netire data for 3 stocks
#daily_simple_returns = data.pct_change().dropna()
#corrs_12=daily_simple_returns.corr()
#corrs_12
#plt.matshow(corrs_12)
#plt.xticks(range(len(daily_simple_returns.columns)),((daily_simple_returns.columns)),rotation=90)
#plt.yticks(range(len(daily_simple_returns.columns)),daily_simple_returns.columns)
#plt.colorbar()
#plt.xticks(fontsize=14)
#plt.yticks(fontsize=14)
#plt.xlabel("FTSE 100 Companies",fontsize=14)
#plt.ylabel("FTSE 100 Companies",fontsize=14)
#plt.title("Correlation matrix for 3 Stocks",fontsize=18, y=+1.35)
#plt.show()

#split data into 2 
#data_ev=data.iloc[:379,:]
#data_naive=data.iloc[379:,:]
#data_ev= data_ev.astype(int)

data_ev=data
data_naive=data
#EV Calculation



daily_simple_returns_ev = data_ev.pct_change().dropna()
mean_return_daily_ev=np.mean(daily_simple_returns_ev)*100
daily_simple_returns_ev.cov()
#plt.figure(figsize=(5,17))
(daily_simple_returns_ev).plot()
plt.xticks(rotation=90,fontsize=14)
plt.yticks(fontsize=14)
plt.title("Daily Returns - E-V Model Portfolio",fontsize=14)
plt.legend(fontsize=12)
plt.show()


sigma_daily_ev = np.std(daily_simple_returns_ev)
print(sigma_daily_ev)

# Calculate the daily variance
variance_daily_ev = sigma_daily_ev**2
print(variance_daily_ev)

kurt_ev = kurtosis(daily_simple_returns_ev.dropna())
skew_ev = skew(daily_simple_returns_ev.dropna())

d_ev=pd.concat([mean_return_daily_ev,sigma_daily_ev,variance_daily_ev],axis=1)
d_ev.columns=['Mean Return (Daily)%','Standard Deviation','Variance']
weights_ev = np.random.random(3)
weights_ev = weights_ev / sum(weights_ev)
weights_ev

#print(np.sum(weights_ev))

WeightedReturns_ev = (daily_simple_returns_ev).mul(weights_ev, axis=1)

# Calculate the portfolio returns
re = WeightedReturns_ev.sum(axis=1)
print(str(round(re * 100, 2)) + '%')

a=pd.DataFrame(re)
a.columns=["E-V"]
#along colusmn
port_returns_expected = np.sum(weights_ev * daily_simple_returns_ev)
print(str(round(port_returns_expected * 100, 2)) + '%')

#Plot the cumulative portfolio returns over time
CumulativeReturns = ((1+a).cumprod()-1)
CumulativeReturns.plot()
plt.xticks(rotation=90)
plt.title("Cumulative Portfolio Return E-V Portfolio")
plt.show()

#extra
import plotly.plotly as py
import plotly.graph_objs as go
import plotly 
plotly.tools.set_credentials_file(username='janusundarj21', api_key='••••••••••')
daily_simple_returns_nv = data_naive.pct_change().dropna()
# Create random data with numpy
import numpy as np
ddd=daily_simple_returns_nv
trace0 = go.Scatter(
    x = ddd.index,
    y = ddd['GVC'],
    mode = 'lines',
    name = 'lines'
)
trace1 = go.Scatter(
    x = ddd.index,
    y = ddd['STAN'],
    mode = 'lines+markers',
    name = 'lines+markers'
)
trace2 = go.Scatter(
    x = ddd.index,
    y = ddd['NMC'],
    mode = 'markers',
    name = 'markers'
)
data = [trace0, trace1, trace2]
py.iplot(data, filename='line-mode')

#1/N Portfolio

daily_simple_returns_nv = data_naive.pct_change().dropna()
(daily_simple_returns_nv).plot()
plt.xticks(rotation=90,fontsize=14)
plt.yticks(fontsize=14)
plt.title("Daily Returns - Naive 1/N  Model Portfolio",fontsize=14)
plt.legend(fontsize=12)
plt.show()
mean_return_daily_nv=np.mean(daily_simple_returns_nv)*100

#daily_simple_returns_nv = daily_simple_returns_nv.iloc[1:,:]
#daily_simple_returns_nv.head()
#daily_simple_returns_nv.plot()

numstocks = 3
weights4= np.random.uniform(0,1)
    
weights = np.array([weights4,weights4,weights4])
# Create an array of equal weights across all assets
portfolio_weights_ew = weights

# Calculate the equally-weighted portfolio returns
r=daily_simple_returns_nv.iloc[:, 0:numstocks].mul(portfolio_weights_ew, axis=1).sum(axis=1)
print(np.sum(r)*100)#b=pd.DataFrame(r)
r.name="1/N Portfolio"
r=pd.DataFrame(r)
r.columns=["1/N"]
CumulativeReturns_nv = ((1+r).cumprod()-1)
CumulativeReturns_nv.plot()
plt.title("Cumulative Portfolio Return 1/N Portfolio")
plt.xticks(rotation=90)
plt.ylabel('Return',fontsize=14)

re.columns=["E-V Portfolio"]
CumulativeReturns_ev = ((1+re).cumprod()-1)
CumulativeReturns_ev.plot()
plt.xticks(rotation=90)
plt.title("Cumulative Portfolio Return E-V Portfolio")
plt.show()
from matplotlib.dates import date2num , DateFormatter
import datetime as dt
f=plt.figure(figsize=(10,25))
ax = plt.subplot(121)
ax.plot(CumulativeReturns_ev, 'black')
plt.xticks(rotation=90)
ax.plot(CumulativeReturns_nv, 'r')
ax.xaxis_date()
#ax.xaxis.set_major_formatter(DateFormatter('%MM/%DD:%YYYY'))
plt.xticks(rotation=90)
plt.title("Eigenportfolio")
#co-variance matrix

#efficient Frontier
#E-V Portfolio
q1_cov=daily_simple_returns_ev.cov()
q1_return = mean_return_daily_ev

#1/N Portfolio
q2_cov=daily_simple_returns_nv.cov()
q2_return = mean_return_daily_nv



pf_returns, pf_volatility, pf_sharpe_ratio, pf_coins_weights=([] for i in range(4))
pf_var=[]
num_portfolios= 100

for portfolio in range(num_portfolios):
    
    weights= np.random.random(3)

    weights /= np.sum(weights)
    

 
    returns = np.dot(weights, q1_return)
    volatility = np.sqrt(np.dot(weights.T, np.dot(q1_cov, weights)))

    
    
    vari=volatility*volatility

    sharpe = returns / volatility

    pf_coins_weights.append(weights)

    pf_returns.append(returns)

    pf_volatility.append(volatility)
    
    pf_var.append(vari)

    pf_sharpe_ratio.append(sharpe)

pf2_returns, pf2_volatility, pf2_sharpe_ratio, pf2_coins_weights=([] for i in range(4))
pf2_var=[]
num2_portfolios= 100

for portfolio2 in range(num2_portfolios):
#    
#    weights= np.random.random(3)
#
#    weights /= np.sum(weights)
    
    weights2= np.random.uniform(0,1)
    
    weights2 = np.array([weights2,weights2,weights2])
 
    returns2 = np.dot(weights2, q2_return)
    volatility2 = np.sqrt(np.dot(weights2.T, np.dot(q2_cov, weights2)))

    
    
    vari2=volatility2*volatility2

    sharpe2 = returns2 / volatility2

    pf2_coins_weights.append(weights2)

    pf2_returns.append(returns2)

    pf2_volatility.append(volatility2)
    
    pf2_var.append(vari2)

    pf2_sharpe_ratio.append(sharpe2)



import seaborn as sns



plt.figure(figsize=(12,10))
#
plt.scatter(x=pf_var, y=pf_returns, c= pf_sharpe_ratio, cmap='viridis')
plt.scatter(x=pf2_var, y=pf2_returns, c= pf2_sharpe_ratio, cmap='magma')
sns.set(style='darkgrid')
#plt.text(0.0195,0.135, "Sharper Ratio:" + " " + str(round(max(pf_sharpe_ratio),4)),fontsize=18)
cb=plt.colorbar(cmap="plasma")
cb.set_label(label='Sharpe Ratio 1/N',fontsize=20)
cb.ax.tick_params(labelsize=16)
plt.title('Efficient Frontier for Naive 1/N Portfolio ',fontsize=20,y=+1.05)
plt.xticks(fontsize=16,rotation = 90)
plt.yticks(fontsize=16)
plt.xlabel('Voltality',fontsize=20)
plt.ylabel('Mean Return',fontsize=20)
plt.show()








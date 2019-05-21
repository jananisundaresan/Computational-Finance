# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 18:41:11 2019

@author: Janani
"""

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from pandas. plotting import scatter_matrix
#from pylab import rcParams
#rcParams['figure.figsize'] = 2,2

data=pd.read_csv("C:/Users/Janani/Desktop/2019/Computational Finance/Assignment 1/prices.csv")
data.index=data['Date']
data=data.iloc[:,1:]

#split data into 2 
data1=data.iloc[:379,:]
data11=data1.iloc[:,1:11]
data12=data1.iloc[:,11:21]
data13=data1.iloc[:,21:]
data2=data.iloc[379:,:]

daily_simple_returns = data1.pct_change()
daily_simple_returns.head()


corrs = daily_simple_returns.corr()
corrs
# annualise daily returns. 250 trading days in a year
#data11 calculation
daily_simple_returns_11 = data11.pct_change()
corrs_11 = daily_simple_returns_11.corr()
scatter_matrix(daily_simple_returns_11,diagonal='kde')
plt.matshow(corrs_11)
plt.xticks(range(len(daily_simple_returns_11.columns)),((daily_simple_returns_11.columns)),rotation=90)
plt.yticks(range(len(daily_simple_returns_11.columns)),daily_simple_returns_11.columns)
plt.colorbar()
plt.show()

#data12 calculation
#GVC-GLEN,GVC-BRBY,GVC-COCA
daily_simple_returns_12 = data12.pct_change()
corrs_12 = daily_simple_returns_12.corr()
scatter_matrix(daily_simple_returns_12,diagonal='kde')

plt.matshow(corrs_12)
plt.xticks(range(len(daily_simple_returns_12.columns)),((daily_simple_returns_12.columns)),rotation=90)
plt.yticks(range(len(daily_simple_returns_12.columns)),daily_simple_returns_12.columns)
plt.colorbar()
plt.show()

#data13 calculation - nmc-rr,nmc-stan
#best - nmc- sla
daily_simple_returns_13 = data1.pct_change()
corrs_13 = daily_simple_returns_13.corr()
scatter_matrix(daily_simple_returns_13,diagonal='kde')
from pylab import rcParams
rcParams['figure.figsize'] = 10,10
plt.matshow(corrs_13)
plt.xticks(range(len(daily_simple_returns_13.columns)),((daily_simple_returns_13.columns)),rotation=90)
plt.yticks(range(len(daily_simple_returns_13.columns)),daily_simple_returns_13.columns)
plt.colorbar()
plt.show()
annual_returns = daily_simple_returns.mean() * 256
annual_returns

#nmc-pr,nmc-stan,nmc-sla,nmc-sse
scatter_matrix(daily_simple_returns,diagonal='kde')
plt.scatter(data1['GVC'],data1['GLEN'],color="red")
plt.scatter(data1['GLEN'],data1['CPG'],color="green")
plt.scatter(data1['CPG'],data1['GVC'],color="blue")

plt.scatter(data1['NMC'],data1['SLA'],color="red")
plt.scatter(data1['GLEN'],data1['CPG'],color="green")
plt.scatter(data1['CPG'],data1['GVC'],color="blue")

#plot a correlation plot
plt.matshow(corrs)
plt.xticks(range(len(data1.columns)),range(len(data1.columns)))
plt.yticks(range(len(data1.columns)),data1.columns)
plt.colorbar()
plt.show()
#CPG,BLND/BLND,BATS
#data_final=data1[['NMC','SLA','GVC','GLEN','CPG','BLND','BATS']]
data_final=data1[['GVC','GLEN','NMC']]
daily_simple_returns_f = data_final.pct_change()
corrs_f = daily_simple_returns_f.corr()
from pylab import rcParams
rcParams['figure.figsize'] = 10,10
plt.matshow(corrs_f)
plt.xticks(range(len(daily_simple_returns_f.columns)),((daily_simple_returns_f.columns)),rotation=90)
plt.yticks(range(len(daily_simple_returns_f.columns)),daily_simple_returns_f.columns)
plt.colorbar()
plt.show()
scatter_matrix(daily_simple_returns_13,diagonal='kde')
daily_return = (np.sum(daily_simple_returns)/len(daily_simple_returns))*100

weights = np.random.random(3)
weights = weights / sum(weights)
weights

print(np.sum(weights))

port_returns_expected = np.sum(weights * annual_returns)
print(str(round(port_returns_expected * 100, 2)) + '%')

#[1] https://medium.com/python-data/calculating-expected-rates-of-returns-for-a-portfolio-of-stocks-with-python-e3afbd4eeba5
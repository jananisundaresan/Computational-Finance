# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 00:08:26 2019

@author: Janani
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:14:26 2019

@author: Janani
"""

import datetime
import numpy as np
from time import sleep

q1_return= [0.10,0.20,0.15]

q1_cov= [[0.005,-0.010,0.004],
         [-0.010,0.040,-0.002],
         [0.004,-0.002,0.023]]


q2_return= [0.10,0.20]

q2_cov= [[0.005,-0.010],
         [-0.010,0.040]]

q3_return= [0.20,0.15]

q3_cov= [[0.040,-0.002],
         [-0.002,0.023]]

q4_return= [0.10,0.15]

q4_cov= [[0.005,0.004],
         [0.004,0.023]]
weights= np.random.random(3)

weights /= np.sum(weights)
weightsnew=weights
print(weightsnew)
pf_returns, pf_volatility, pf_sharpe_ratio, pf_coins_weights=([] for i in range(4))
pf_var=[]
num_portfolios= 100

for portfolio in range(num_portfolios):

    weights= weightsnew

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
num_portfolios2= 100

for portfolio2 in range(num_portfolios2):

    weights2= weightsnew[0:2]
    #weights2 /= np.sum(weights2)

    returns2 = np.dot(weights2, q2_return)

    volatility2 = np.sqrt(np.dot(weights2.T, np.dot(q2_cov, weights2)))
    
    vari2=volatility2*volatility2

    sharpe2 = returns2 / volatility2

    pf2_coins_weights.append(weights2)

    pf2_returns.append(returns2)

    pf2_volatility.append(volatility2)

    pf2_sharpe_ratio.append(sharpe2)
    
    pf2_var.append(vari2)

pf3_returns, pf3_volatility, pf3_sharpe_ratio, pf3_coins_weights=([] for i in range(4))
pf3_var=[]
num_portfolios3= 100

for portfolio3 in range(num_portfolios3):

    weights3= weightsnew[1:]

    #weights3 /= np.sum(weights3)

    returns3 = np.dot(weights3, q3_return)

    volatility3 = np.sqrt(np.dot(weights3.T, np.dot(q3_cov, weights3)))
    
    vari3=volatility3*volatility3

    sharpe3 = returns3 / volatility3

    pf3_coins_weights.append(weights3)

    pf3_returns.append(returns3)

    pf3_volatility.append(volatility3)

    pf3_sharpe_ratio.append(sharpe3)
    
    pf3_var.append(vari3)
    
pf4_returns, pf4_volatility, pf4_sharpe_ratio, pf4_coins_weights=([] for i in range(4))
pf4_var=[]
num_portfolios4= 100

for portfolio4 in range(num_portfolios4):

    weights4= np.array(weightsnew[0],weightsnew[2])

    #weights4 /= np.sum(weights4)

    returns4 = np.dot(weights4, q4_return)

    volatility4 = np.sqrt(np.dot(weights4.T, np.dot(q4_cov, weights4)))
    
    vari4=volatility4*volatility4

    sharpe4 = returns4 / volatility4

    pf4_coins_weights.append(weights4)

    pf4_returns.append(returns4)

    pf4_volatility.append(volatility4)

    pf4_sharpe_ratio.append(sharpe4)
    
    pf4_var.append(vari4)

import matplotlib.pyplot as plt

import seaborn as sns



plt.figure(figsize=(15,7))
#
plt.scatter(x=pf_volatility, y=pf_returns, c= pf_sharpe_ratio, cmap='viridis')
#plt.scatter(x=pf2_volatility, y=pf2_returns, c= pf2_sharpe_ratio, cmap='plasma')
#plt.scatter(x=pf3_volatility, y=pf3_returns, c= pf3_sharpe_ratio, cmap='inferno')
#plt.scatter(x=pf4_volatility, y=pf4_returns, c= pf4_sharpe_ratio, cmap='magma')

##plt.scatter(x=pf2_var, y=pf2_returns, c= pf2_sharpe_ratio, cmap='plasma')
#plt.scatter(x=pf3_var, y=pf3_returns, c= pf3_sharpe_ratio, cmap='inferno')
#plt.scatter(x=pf4_var, y=pf4_returns, c= pf4_sharpe_ratio, cmap='magma')
plt.text(0.025,0.13, "Sharper Ratio:" + " " + str(round(max(pf_sharpe_ratio),4)),fontsize=14)
cb=plt.colorbar()
cb.set_label(label='Sharpe Ratio',fontsize=18)
cb.ax.tick_params(labelsize=14)
sns.set(style='darkgrid')

plt.title('Efficient Frontier for 3 Stock portfolio',fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Voltality',fontsize=18)
plt.ylabel('Mean Return',fontsize=18)
plt.text(0.12,0.020,'Sharper Ratio')
plt.show()


print ( "Sharper Ratio" + str(max(pf_sharpe_ratio)))








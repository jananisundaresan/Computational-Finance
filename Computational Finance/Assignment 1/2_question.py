# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:14:26 2019

@author: Janani
"""

import datetime
import numpy as np
from time import sleep

q1_return= [0.10,0.20,0.15]
#
q1_cov= [[0.005,-0.010,0.004],
         [-0.010,0.040,-0.002],
         [0.004,-0.002,0.023]]

#
#q1_return= [0.10,0.20]
#
#q1_cov= [[0.005,-0.010],
#         [-0.010,0.040]]

#q1_return= [0.20,0.15]
#
#q1_cov= [[0.040,-0.002],
#         [-0.002,0.023]]

#q1_return= [0.10,0.15]
#
#q1_cov= [[0.005,0.004],
#         [0.004,0.023]]

pf_returns, pf_volatility, pf_sharpe_ratio, pf_var,pf_coins_weights=([] for i in range(5))

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

    pf_sharpe_ratio.append(sharpe)
    
    pf_var.append(vari)



import matplotlib.pyplot as plt

#import seaborn as sns



plt.figure(figsize=(15,7))

plt.scatter(x=pf_var, y=pf_returns, c= pf_sharpe_ratio, cmap='viridis')

plt.colorbar(label='Sharpe Ratio')

#sns.set(style='darkgrid')

plt.title('Efficient Frontier')

plt.xlabel('Volatility')

plt.ylabel('Return')

plt.show()


print ( "bets value" + str(max(pf_sharpe_ratio)))







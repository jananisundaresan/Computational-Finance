
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

dd=pd.read_csv("C:/Users/Janani/Desktop/imp_vol_final_put.csv")
#binoc6800=df[['BinoC6800']]
#calltrue6800=df[['CallTrue6800']]
#bsc6800=df[['CallEst6800']]
#binop6800=df[['BinoP6800']]
#puttrue6800=df[['PutTrue6800']]
#bsp6800=df[['PutEst6800']]
#daays=df[['days to expire']]
fig = plt.figure()
ax = plt.subplot(111)
#dd=pd.concat([binoc6800,calltrue6800,bsc6800,daays],axis=1)
#dd.columns=["Binomial","True","Black Scholes","Days"]
ax.plot(dd['Vol'],dd['4800'])
ax.plot(dd['Vol'],dd['5600'])
ax.plot(dd['Vol'],dd['6300'])
ax.plot(dd['Vol'],dd['6800'])
ax.plot(dd['Vol'],dd['7200'])
ax.plot(dd['Vol'],dd['7600'])
ax.plot(dd['Vol'],dd['8000'])
ax.plot(dd['Vol'],dd['8400'])
ax.plot(dd['Vol'],dd['8800'])
ax.plot(dd['Vol'],dd['9200'])
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), shadow=True, ncol=1)

#plt.scatter(dd['Vol'],dd['4800'])
#plt.scatter(dd['Vol'],dd['5600'])
#plt.scatter(dd['Vol'],dd['6300'])
#plt.scatter(dd['Vol'],dd['6800'])
#plt.scatter(dd['Vol'],dd['7200'])
#plt.scatter(dd['Vol'],dd['7600'])
#plt.scatter(dd['Vol'],dd['8000'])
#plt.scatter(dd['Vol'],dd['8400'])
#plt.scatter(dd['Vol'],dd['8800'])
#plt.scatter(dd['Vol'],dd['9200'])

#plt.gca().invert_xaxis()
plt.grid()
plt.xticks(fontsize=12,rotation = 90)
plt.title("Put Option - Implied Volatility vs Volatility",fontsize=14)
plt.yticks(fontsize=12)
plt.xlabel('Volatility',fontsize=14)
plt.ylabel('Implied Volatility',fontsize=14)

#dd1=pd.concat([binop6800,puttrue6800,bsp6800,daays],axis=1)
#dd1.columns=["Binomial","True","Black Scholes","Days"]
#plt.plot(dd1['Days'],dd1['Binomial'])
#plt.plot(dd1['Days'],dd1['True'])
#plt.plot(dd1['Days'],dd1['Black Scholes'])
#plt.gca().invert_xaxis()
#plt.legend()
#plt.grid()
#plt.legend()
#plt.xticks(fontsize=12,rotation = 90)
#plt.title("Put Option - Binomial vs Black Scholes vs True for K = 6800",fontsize=14)
#plt.yticks(fontsize=12)
#plt.xlabel('Days Remaining',fontsize=14)
#plt.ylabel('Price',fontsize=14)

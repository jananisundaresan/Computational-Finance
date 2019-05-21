
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

df=pd.read_csv("C:/Users/Janani/Desktop/2019/Computational Finance/Assignment 2/binomialoption.csv")

binoc6800=df[['BinoC6800']]
calltrue6800=df[['CallTrue6800']]
bsc6800=df[['CallEst6800']]
binop6800=df[['BinoP6800']]
puttrue6800=df[['PutTrue6800']]
bsp6800=df[['PutEst6800']]
daays=df[['days to expire']]

dd=pd.concat([binoc6800,calltrue6800,bsc6800,daays],axis=1)
dd.columns=["Binomial","True","Black Scholes","Days"]
plt.plot(dd['Days'],dd['Binomial'])
plt.plot(dd['Days'],dd['True'])
plt.plot(dd['Days'],dd['Black Scholes'])
plt.legend()
plt.gca().invert_xaxis()
plt.grid()
plt.legend()
plt.xticks(fontsize=12,rotation = 90)
plt.title("Call Option - Binomial vs Black Scholes vs True for K = 6800",fontsize=14)
plt.yticks(fontsize=12)
plt.xlabel('Days Remaining',fontsize=14)
plt.ylabel('Price',fontsize=14)

dd1=pd.concat([binop6800,puttrue6800,bsp6800,daays],axis=1)
dd1.columns=["Binomial","True","Black Scholes","Days"]
plt.plot(dd1['Days'],dd1['Binomial'])
plt.plot(dd1['Days'],dd1['True'])
plt.plot(dd1['Days'],dd1['Black Scholes'])
plt.gca().invert_xaxis()
plt.legend()
plt.grid()
plt.legend()
plt.xticks(fontsize=12,rotation = 90)
plt.title("Put Option - Binomial vs Black Scholes vs True for K = 6800",fontsize=14)
plt.yticks(fontsize=12)
plt.xlabel('Days Remaining',fontsize=14)
plt.ylabel('Price',fontsize=14)

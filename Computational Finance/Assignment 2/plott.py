# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:11:37 2019

@author: Janani
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df=pd.read_csv("C:/Users/Janani/Desktop/2019/Computational Finance/Assignment 2/4800data.csv")
df=pd.read_csv("C:/Users/Janani/Desktop/2019/Computational Finance/Assignment 2/final.csv")
ftse=df[['FTSE ']]
call=df[['PutTrue6800']]
est=df[['PutEst6800']]
da=df[['Days to Expire']]
dd=pd.concat([call,est,da],axis=1)

#df['Log_Ret'] = np.log(df['FTSE 100 - PRICE INDEX'] / df['FTSE 100 - PRICE INDEX'].shift(1))
#g=df['Log_Ret'].rolling(window=66,center=False).std()
#j=g/np.sqrt(len(df)/4)


dd.columns=["True","Estimate","Days to Expire"]
plt.plot(dd['True'])
plt.plot(dd['Estimate'])
plt.legend()
plt.gca().set_xlim(xmin=50,xmax= 270)
plt.legend()
plt.xticks(fontsize=12,rotation = 90)
plt.title("European Put - True vs Estimate for K = 6800",fontsize=14)
plt.yticks(fontsize=12)
plt.xlabel('Window',fontsize=14)
plt.ylabel('Price',fontsize=14)
plt.grid()

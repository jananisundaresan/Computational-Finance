# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:58:35 2019

@author: Janani
"""

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

path="C:/Users/Janani/Desktop/2019/Computational Finance/Assignment 1/"

#selected 30 companies
ftse=pd.read_csv(path+"FTSE_final.csv")
blnd=pd.read_csv(path+"BLND.L.csv")
abf=pd.read_csv(path+"ABF.L.csv")
bats=pd.read_csv(path+"BATS.L.csv")
dlg=pd.read_csv(path+"DLG.L.csv")
crda=pd.read_csv(path+"CRDA.L.csv")
lse=pd.read_csv(path+"LSE.L.csv")
ferg=pd.read_csv(path+"FERG.L.csv")
cpg=pd.read_csv(path+"CPG.L.csv")
sbry=pd.read_csv(path+"SBRY.L.csv")
glen=pd.read_csv(path+"GLEN.L.csv")
gvc=pd.read_csv(path+"GVC.L.csv")
coca=pd.read_csv(path+"CCH.L.csv")
bkg=pd.read_csv(path+"BKG.L.csv")
bnzl=pd.read_csv(path+"BNZL.L .csv")
brby=pd.read_csv(path+"BRBY.L.csv")
ezj=pd.read_csv(path+"EZJ.L.csv")
expn=pd.read_csv(path+"EXPN.L.csv")
hlma=pd.read_csv(path+"HLMA.L.csv")
lloyd=pd.read_csv(path+"LLOY.L.csv")
mks=pd.read_csv(path+"MKS.L.csv")
mrw=pd.read_csv(path+"MRW.L.csv")
rr=pd.read_csv(path+"RR.L.csv")
sge=pd.read_csv(path+"SGE.L.csv")
stan=pd.read_csv(path+"STAN.L.csv")
tesco=pd.read_csv(path+"TSCO.L.csv")
sla=pd.read_csv(path+"SLA.L.csv")
smds=pd.read_csv(path+"SMDS.L.csv")
sse=pd.read_csv(path+"SSE.L.csv")
rmv=pd.read_csv(path+"RMV.L.csv")
nmc=pd.read_csv(path+"NMC.L.csv")



print("FTSE:"+str(ftse.shape)) #768
print("BLND:"+str(blnd.shape)) # 758
print("ABF:"+str(abf.shape)) # 758
print("BATS:"+str(bats.shape)) #758
print("LSE:"+str(lse.shape)) #758
print("DLG:"+str(dlg.shape)) #758
print("CRDA:"+str(crda.shape)) #758
print("FERG:"+str(ferg.shape)) #758
print("CPG:"+str(cpg.shape)) #758
print("SBRY:"+str(sbry.shape)) #758
print("GLEN:"+str(glen.shape)) #758
print("GVC:"+str(gvc.shape)) #755
print("COCA:"+str(coca.shape)) #758
print("NMC:"+str(nmc.shape)) #758
print("RMV:"+str(rmv.shape)) #758
print("SSE:"+str(sse.shape)) #758
print("SMDS:"+str(smds.shape)) #758
print("SLA:"+str(sla.shape)) #758
print("TESCO:"+str(tesco.shape)) #758
print("STAN:"+str(stan.shape)) #758
print("RR:"+str(rr.shape)) #758
print("SGE:"+str(sge.shape)) #758
print("MRW:"+str(mrw.shape)) #758
print("MKS:"+str(mks.shape)) #758
print("LLOYD:"+str(lloyd.shape)) #758
print("HLMA:"+str(hlma.shape)) #758
print("EXPN:"+str(expn.shape)) #758
print("EZJ:"+str(ezj.shape)) #758
print("BRBY:"+str(brby.shape)) #758
print("BNZL:"+str(bnzl.shape)) #758
print("BKG:"+str(bkg.shape)) #758
data=pd.concat([microsoft['Adj Close'],google['Adj Close'],amazon['Adj Close']],axis=1)
data.index=microsoft['Date']
#data=data.drop(data['Date'])
data.columns=['MSFT','GOOGL','AMZN']

#split data into 2 
data1=data.iloc[:384,:]
data2=data.iloc[384:,:]

daily_simple_returns = data1.pct_change()
daily_simple_returns.head()


corrs = daily_simple_returns.corr()
corrs
# annualise daily returns. 250 trading days in a year

annual_returns = daily_simple_returns.mean() * 256
annual_returns

from pandas. plotting import scatter_matrix
scatter_matrix(daily_simple_returns,diagonal='kde')
plt.scatter(data1['MSFT'],data1['GOOGL'],color="red")
plt.scatter(data1['MSFT'],data1['AMZN'],color="green")
plt.scatter(data1['GOOGL'],data1['AMZN'],color="blue")

#plot a correlation plot
plt.matshow(corrs)
plt.xticks(range(len(data1.columns)),range(len(data1.columns)))
plt.yticks(range(len(data1.columns)),data1.columns)
plt.colorbar()
plt.show()

daily_return = (np.sum(daily_simple_returns)/len(daily_simple_returns))*100

weights = np.random.random(3)
weights = weights / sum(weights)
weights

print(np.sum(weights))

port_returns_expected = np.sum(weights * annual_returns)
print(str(round(port_returns_expected * 100, 2)) + '%')

#[1] https://medium.com/python-data/calculating-expected-rates-of-returns-for-a-portfolio-of-stocks-with-python-e3afbd4eeba5
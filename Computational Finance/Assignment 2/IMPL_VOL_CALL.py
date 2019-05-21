

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def implied_vol_call_min(S,X,T,r,c):
    from scipy import log,exp,sqrt,stats
    implied_vol=1.0
    min_value=1000
    for i in range(10000):
        sigma=0.0001*(i+1)
        d1=(log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))
        d2 = d1-sigma*sqrt(T)
        c2=S*stats.norm.cdf(d1)-X*exp(-r*T)*stats.norm.cdf(d2)
        abs_diff=abs(c2-c)
        if abs_diff<min_value:
            min_value=abs_diff
            implied_vol=sigma
            k=i
    return implied_vol



from scipy import log,exp,sqrt,stats 



def implied_vol_put_min(S,X,T,r,p):
    implied_vol=1.0
    min_value=100.0
    for i in range(1,10000): 
        sigma=0.0001*(i+1)
        d1=(log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T)) 
        d2 = d1-sigma*sqrt(T)
        put=X*exp(-r*T)*stats.norm.cdf(-d2)-S*stats.norm.cdf(-d1) 
        abs_diff=abs(put-p)
        if abs_diff<min_value: 
            min_value=abs_diff 
            implied_vol=sigma 
            k=i
        put_out=put


    #print 'k, implied_vol, put, abs_diff' 

    return implied_vol
#implied_vol_put_min(6877.5,6800,0.03,0.013,116.3)
#implied_vol_call_min(6980.24,6800,0.08,0.016,330)
#df.to_dense().to_csv('C:/Users/Janani/Desktop/imp_vol_final.csv', sep=',', encoding='utf-8',index=False)
df=pd.read_csv("C:/Users/Janani/Desktop/2019/Computational Finance/Assignment 2/final_plot_imp.csv")
S=df['FTSE']
X=7600
T=df['in fraction']
r=df['Rate fra']
c=df['7600']
days=df['Daysto']
vol=df['Vol']
df['imp7600']=np.nan
imp=df['imp7600']

for i in range(len(df)):
   #Sa=S[i]implied_vol_call_min(6980.24,6800,0.08,0.016,330)
   imp[i]=implied_vol_put_min(S[i],X,T[i],r[i],c[i])
   
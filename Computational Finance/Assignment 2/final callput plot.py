

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df1=pd.read_csv("C:/Users/Janani/Desktop/imp_vol_finalcall.csv")

impvol1=df1[['4800']]
impvol2=df1[['5600']]
impvol3=df1[['6300']]
impvol4=df1[['6800']]
days=df1[['Daysto']]

vol=df1[['Vol']]
dd=pd.concat([impvol1,impvol2,impvol3,impvol4,vol,days],axis=1)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

X = [4800,5600]
Y = days
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = [impvol1,impvol2]
surf = ax.plot_surface(X, Y, Z, rstride=4, cstride=4,cmap=cm.plasma,
                       linewidth=0, antialiased=False)
ax.set_xlim(4800, 5600)
xticks = ax.get_xticks()
xticklabels = ax.get_xticklabels()
ax.set_xticks(xticks[::2])
ax.set_xticklabels(xticks[::2])
ax.set_xlabel('Strike Price')
ax.set_ylabel('Days to Expire')
ax.set_zlabel('Implied Volatility')
ax.title





fig = plt.figure()
ax = fig.gca(projection='3d')
X1 = [6800,7600]
Y1 = days
X1, Y1 = np.meshgrid(X1, Y1)
Z1 = impvol2
surf = ax.plot_surface(X1, Y1, Z1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_xlim(6800, 7600)
xticks = ax.get_xticks()
xticklabels = ax.get_xticklabels()
ax.set_xticks(xticks[::2])
ax.set_xticklabels(xticks[::2])
# rotate the axes and update
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.0001)

fig = plt.figure()
ax = fig.gca(projection='3d')
X1 = [6800,7600]
Y1 = days
X1, Y1 = np.meshgrid(X1, Y1)
Z1 = impvol3
surf = ax.plot_surface(X1, Y1, Z1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_xlim(6800, 7600)
xticks = ax.get_xticks()
xticklabels = ax.get_xticklabels()
ax.set_xticks(xticks[::2])
ax.set_xticklabels(xticks[::2])
# rotate the axes and update
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)
# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.set_xticks(ticks, minor=False)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
#df['Log_Ret'] = np.log(df['FTSE 100 - PRICE INDEX'] / df['FTSE 100 - PRICE INDEX'].shift(1))
#g=df['Log_Ret'].rolling(window=66,center=False).std()
#j=g/np.sqrt(len(df)/4)


#dd.columns=["Implied Volatility","Volatility"]


plt.plot(dd['Daysto'],dd["C6800ImpVol"],)
plt.scatter(dd["P6800ImpVol"],dd['Daysto'])
plt.scatter(dd["P7600ImpVol"],dd['Daysto'])
plt.scatter(dd["C7600ImpVol"],dd['Daysto'])



plt.scatter(dd["C6800ImpVol"],dd["Vol"])
plt.scatter(dd["P6800ImpVol"],dd["Vol"])
plt.scatter(dd["P7600ImpVol"],dd["Vol"])
plt.scatter(dd["C7600ImpVol"],dd["Vol"])
plt.plot()
plt.legend()
plt.grid()


plt.gca().set_xlim(xmin=50,xmax= 270)
plt.legend()
plt.xticks(fontsize=12,rotation = 90)
plt.title("European Put - True vs Estimate for K = 6800",fontsize=14)
plt.yticks(fontsize=12)
plt.xlabel('Days Remaining',fontsize=14)
plt.ylabel('Price',fontsize=14)

imp=pd.read_csv("C:/Users/Janani/Desktop/2019/Computational Finance/Assignment 2/volsmile.csv")
import seaborn as sns
ax = sns.regplot(x="Strike Price", y="Put", data=imp,
                 scatter_kws={"s": 80},
                 order=2, ci=None, truncate=True)
ax = sns.scatterplot(x="Strike Price", y="Put",data=imp)
ax = sns.scatterplot(x="Strike Price", y="Call",data=imp)
import seaborn as sns
fig = plt.figure()
ax = plt.subplot(111)
ax.plot("Strike Price","Put", label="Put",data=imp, marker='o', color='mediumvioletred')
ax.plot("Strike Price","Call",label="Call", data=imp, marker='o', color='blue')
ax.set_xlabel('Strike Price',fontsize=14)
#plt.gca().set_xlim(xmin=4800,xmax= 9200)
ax.set_xticks(np.arange(4800, 9600, step=400))
ax.set_ylabel('Implied Volatility',fontsize=14)
plt.title("Volatility Smile",fontsize=14)
plt.xticks(fontsize=14,rotation=90)
plt.yticks(fontsize=14)
ax.legend()
plt.show()
ax.grid()

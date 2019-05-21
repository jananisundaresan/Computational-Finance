
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df1=pd.read_csv("C:/Users/Janani/Desktop/imp_vol_final_put.csv")

#impvol1=df1[['imp4800']]
#impvol2=df1[['imp5600']]
#impvol3=df1[['imp6300']]
#impvol4=df1[['imp6800']]
#days=df1[['Daysto']]

#vol=df1[['Vol']]
#dd=pd.concat([impvol1,impvol2,impvol3,impvol4,vol,days],axis=1)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')
d=pd.DataFrame({"li":[5600,6800,8000,9200]})

def cc(arg):
    return mcolors.to_rgba(arg, alpha=0.6)

ys = np.arange(0, 30, 1)
verts = []
zs = d['li']
for z in zs:
    z=str(z)
    xs = np.array(df1[z]).reshape(30,)
    
    #ys[0], ys[-1] = 0, 0
    verts.append(list(zip(xs, ys)))
    #print(verts)

poly = PolyCollection(verts, facecolors=[cc('r'), cc('g'), cc('b'),
                                         cc('y')])
poly.set_alpha(0.7)
ax.add_collection3d(poly, zs=zs, zdir='z')

ax.zaxis.set_rotate_label(False) 
ax.xaxis.set_rotate_label(False)
ax.yaxis.set_rotate_label(False) # disable automatic rotation
ax.set_zlabel('Strike Price', rotation=90,fontsize=10)
ax.set_xlabel('Implied Volatility', rotation=105,fontsize=10)
ax.set_ylabel('Days to Expire',rotation=180,fontsize=10,y=+1.5)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.title("Put - Implied Volatility vs Days to Expire vs Strike Price",fontsize=14,y=+1.05,rotation=180)
ax.set_xlim3d(0, 1)
ax.set_zticks([5600,6800,8000,9200])
props = {"rotation" : 180}
plt.setp(ax.get_xticklabels(), **props)
plt.setp(ax.get_yticklabels(), **props)
plt.setp(ax.get_zticklabels(), **props)
ax.set_ylim3d(0,30)

ax.set_zlim3d(5000,10000)


for angle in range(0, 360):
    ax.view_init(20, angle)
    plt.draw()
    plt.pause(.001)
plt.show()

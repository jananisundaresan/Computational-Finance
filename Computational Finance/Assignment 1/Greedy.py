# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 18:00:55 2019

@author: Janani
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score as acc
#from mlxtend.feature_selection import SequentialFeatureSelector as sfs
from sklearn import preprocessing
#from sklearn.neighbors import KNeighborsClassifier
# Read data
df = pd.read_csv('C:/Users/Janani/Desktop/2019/sparse.csv')
df['X.FTSE']=df['X.FTSE']*10000
df['FTSE']=df['X.FTSE']
df=df.drop(['X.FTSE'],axis=1)

X=df.values[:,:-1].astype(int)
y=df.values[:,-1:].astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33)
#from sklearn.svm import SVR
#svr = SVR()
#svr.fit(X_train, y_train)
#print(svr.score(X_train, y_train))
#print(svr.score(X_test, y_test))
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
lr = LinearRegression()
#k=KNeighborsClassifier(n_neighbors=4)
#k1=KNeighborsRegressor(n_neighbors=4)
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
sfs = SFS(lr, 
          k_features=5, 
          forward=True, 
          floating=False, 
          scoring='neg_mean_squared_error',
          cv=10)

sfs = sfs.fit(X_train, y_train)
fig = plot_sfs(sfs.get_metric_dict(), kind='std_err')
import seaborn as sns
sns.set(style='darkgrid')
plt.title('Greedy Forward Selection',fontsize=16,y=+1.05)
#plt.title('Efficient Frontier for Naive 1/N Portfolio ')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.ylabel('Standard Error',fontsize=20)
plt.xlabel('Number of Stocks',fontsize=20)

plt.show()
#k1.fit(X_train, y_train)
y_train_pred = k1.predict(X_train)
#print('Training accuracy on selected features: %.3f' % acc(y_train, y_train_pred))

print('Selected features:', sfs.k_feature_idx_)
from sklearn.metrics import mean_squared_error
mean_squared_error(y_train_pred, y_train)

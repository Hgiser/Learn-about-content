# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:07:32 2019

@author: Administrator
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np
import geoplot as gplt
import geopandas as gpd
from pandas import DataFrame, Series

import sys
sys.path.append(r'E:\geostatsmodels-master\notebooks')




class data_body(object):
    def __init__(self,x,y,z,porosity,impedance):
        self.x = x
        self.y = y
        self.z = z
        self.porosity = porosity
        self.impedance = impedance


f=open(r'E:\geostatsmodels-master\sample_data.gslib.txt',"r",encoding='utf-16')
fdata = f.readlines()
mydata = []
        
for data in fdata:
    data1 = data.strip('\n')	# 去掉开头和结尾的换行符
    data2 = data1.split(' ')	# 把tab作为间隔符
    
    
    mydata.append(data2)	# 把这一行的结果作为元素加入列表dataset

mydata = np.array(mydata)

print(mydata)
data = np.zeros([563,4])
for i in range(563):
    for j in range (4):
        data[i,j] = mydata[i][j]
print(data)
x = data[:,0]
y = data[:,1]
#z = data[:,2]
porosity = data[:,3]
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x,y,porosity)
plt.show()
  
plt.figure(figsize=(10, 10), dpi=80)
plt.subplot(1, 1, 1)
N = 20
values = (0.008,0.004,0.01,0.004,0.013,0.018,0.037,0.035,0.084,0.108,0.117,0.142,0.13,0.135,0.07,0.05,0.03,0.004,0.005,0.005)
index = np.arange(N)
width = 0.35
p2 = plt.bar(index, values, width, label="porosity", color="#87CEFA")
plt.ylabel('frequency (m)')
plt.xlabel('porosity (%)') ;
plt.Xticks(index, ('0.18','0.19','0.20','0.2','0.21','0.22','0.23','0.24','0.25','0.26','0.27','0.28','0.29','0.30','0.31','0.32','0.33','0.34','0.35','0.36'))
plt.Yticks(index, ('0', '0.02', '0.04', '0.06', '0.08', '0.10','0.12','0.14','0.16'))
plt.show()  


tolerance = 250
lags = np.arange( tolerance, 10000, tolerance*2 )
sill = np.var( P[:,2] )
geoplot.semivariogram( P, lags, tolerance )
svm = model.semivariance( model.spherical, ( 4000, sill ) )
geoplot.semivariogram( P, lags, tolerance, model=svm )    
covfct = model.covariance( model.spherical, ( 4000, sill ) )
kriging.simple( P, covfct, pt, N=6 )
kriging.ordinary( P, covfct, pt, N=6 )
est, kstd = kriging.krige( P, covfct, [[2000,4700],[2100,4700],[2000,4800],[2100,4800]], 'simple', N=6 )

est



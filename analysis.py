# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 20:17:35 2019

@author: En_Ryuu
"""

import rand3d

n=1000

xsum=0
x_l=[]
y_l=[]
z_l=[]

for _ in range(10):
    (x,y,z,s)=rand3d.random_generate(n)
    xsum += s
    x_l.append(x)
    y_l.append(y)
    z_l.append(z)

fig = plt.figure(figsize=(10,10))
ax = fig.gca(projection='3d')    
ax.scatter(x_l, y_l, z_l, c='b', marker='o', s=80)
ax.scatter(0,0,0, c='k', marker='d', s =80)
ax.text(0,0,0, '%s' %("(0,0)"), fontsize=30)


average = xsum/100    
print("Average distance travelled = ",average)    
    



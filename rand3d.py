#import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from mpl_toolkits.mplot3d import Axes3D

x_list=[0]
y_list=[0]
z_list=[0]


def randlist():
    direction = np.random.randint(0, 100, size=3)
    r = sum(direction)%3
    return r

def random_generate(n):
    x = 0 
    y = 0
    z = 0
    far = 0
    for i in range(n):
        (r1) = randlist()
        if r1 == 0:
            x += random.choice([-1,1])
        elif r1 == 1:
            y += random.choice([-1,1])
        else:    
            z += random.choice([-1,1])
                
        if math.sqrt(abs(x)**2 +abs(y)**2 +abs(z)**2) > far:
            far = math.sqrt(abs(x)**2 +abs(y)**2 +abs(z)**2)
            xfar = x
            yfar = y
            zfar = z
            
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)
        
    return xfar,yfar,zfar,far


def rand_plot(x,y,z,n,fx,fy,fz,f):
    fig = plt.figure(figsize=(10,10))
    ax = Axes3D(fig)
    marx=[fx,0]
    mary=[fy,0]
    marz=[fz,0]
    ax.plot(x, y, z, label='Random walk', marker = '>')
    ax.plot(marx, mary, marz, c='b', marker='o',label = ('Total Distance Travelled = %s units' %(f)))
    ax.text(x[0]+0.1,y[0]+0.1,z[0],  '%s' % (str("Start")), size=20, color='k',bbox=dict(facecolor='r', alpha=0.5)) 
    ax.text(x[n]+0.1,y[n]+0.1,z[n],  '%s' % (str("End")), size=20, color='k',bbox=dict(facecolor='g', alpha=0.5)) 
    ax.text(fx+0.1,fy+0.1,fz,  '%s' % (str("Farthest Distance Travelled")), size=20, color='k',bbox=dict(facecolor='b', alpha=0.5)) 
    ax.scatter(x[-1], y[-1], z[-1], c='b', marker='o')
    ax.legend()
    plt.show()

def fmain ():
    n = 1000
    (xfar,yfar,zfar,far)=random_generate(n)
    rand_plot(x_list,y_list,z_list,n,xfar,yfar,zfar,far)

fmain()
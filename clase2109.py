# montecarlo

import numpy as np 
import matplotlib.pyplot as plt
import random 
import math
import time 

a,b,n = 0,1,200

py = []
px = []

for i in range (n):
    py.append(random.uniform(-1,1))
    px.append(random.uniform(-1,1))

plt.plot(px,py,'o',markersize=1)

####################################################################

npx = np.random.uniform(-1,1,n)
npy = np.random.uniform(-1,1,n)

plt.figure()
plt.plot(npx,npy,'o',markersize=1)

sumac=0
cpx,cpy=((b+a)/2,(b+a)/2)
print (cpx,cpy)

circ = npx**2 + npy**2 <= 1
cuad = np.invert(circ)
pi = circ.sum()*4/n

for i in range (n):
    plt.plot(npx[circ],npy[circ],'o',markersize=1)
    plt.plot(npx[cuad],npy[cuad],'o',markersize=1)
    time.sleep(.5)
print (pi)

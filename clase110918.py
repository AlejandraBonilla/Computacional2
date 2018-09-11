#librería numpy 
#hacer un histograma en dos dimensiones 

import numpy as np 
from numpy import matrix
import math
import matplotlib.pyplot as plt 
import random

vx = []
vy = []
num =10000
for i in range(num): 
    vrx=random.gauss(0,2)
    vry=random.gauss(0,2)
    vx.append(vrx)
    vy.append(vry)
    
print(vx)
#plt.hist(vx,bins=int(math.sqrt(num)))
#plt.hist(vy,bins=int(math.sqrt(num)))
plt.plot(vx,vy,'p', markersize=1)
plt.figure()
plt.hist2d(vx,vy, bins=50)
###############################################################
n = 514
a = np.zeros(263169).reshape(513,513)

centro=(n-2)/2
cent = int(centro)

a[cent][cent] = vx
rci=2

for i in range (n):
  for j in range (n):
    if(math.sqrt((i-cent)*(i-cent)+(j-cent)*(j-cent))<=70):
      a[i][j]=vx

plt.imshow(a)


def samplemat(dims):
    """Make a matrix with all zeros and increasing elements on the diagonal"""
    aa = np.zeros(dims)
    for i in range(min(dims)):
        aa[i, i] = i
    return aa


# Display matrix
plt.matshow(samplemat((15, 15)))

plt.show()

# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import numpy as np
import math
import matplotlib.pyplot as plt 

fa=fpx(a)
fa

def lin0(a,b,fa,fb):
    m=(fb-fa)/(b-a)
    return (m*b-fb)/m

def funx(x):
    return [(math.exp(-i) -i) for i in x]

def fpx(x):
    return (math.exp(-x)-x)

     
#x1= np.arange(-5,5,0.1)
#plt.plot(x1,funx(x1))
    
def xm(a,b):
    return (b-a)/2


a,b,np=-1,2,100
delta=(b-a)/(np-1)

vx=[a+i*delta for i in range(np)]

plt.plot(vx,funx(vx))
max(funx(vx))
pm=xm(a,b)

for j in range(20):
    if (fpx(a)*fpx(pm)<0):
        a=pm
    else: 
        b=pm
    pm=xm(a,b)
    print("{:.4f}".format(a),"{:.4f}".format(b),"{:.4f}".format(pm),"{:.4f}".format(fpx(pm)))


print(pm,fpx(pm))



# código para el método de Euler

import matplotlib.pyplot as plt 
import numpy as np 
import math 

def F(x,y): 
    return (-3.0/4.0*x**4+4.0/3.0*x**3-x**2+8.5*x)

def f(x,y): 
    return (-3.0*x**3+4.0*x**2-2.0*x+8.5)

x0 = 0.0
xf = 4.0
y0 = 1.0
h = [0.5,0.4,0.3,0.2,0.1]

for j in h:
    x0 = 0.0
    xf = 4.0
    y0 = 1.0
    npx=(int((xf-x0)/j)+1)
    xi=[]
    yi=[]

    for i in range(npx): 
        x0=i*j
        print (x0)
        y0=y0+f(x0,y0)*j
        xi.append(x0)
        yi.append(y0)
    
    plt.plot(xi,yi)
    plt.xlabel('x')
    plt.ylabel('f(x,y)')
    
plt.show()

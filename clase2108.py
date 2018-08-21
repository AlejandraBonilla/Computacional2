#importo las librerias 
import numpy as np
import math
import matplotlib.pyplot as plt 

#defino mi funcion para cada punto 
def funx(x):
    return [(math.exp(-i) -i) for i in x]

#defino la funcion evaluada en un solo punto
def fpx(x):
    return (math.exp(-x)-x)

#defino el punto medio en cada intervalo
def xm(a,b):
    return (b+a)/2

#doy miis condiciones iniciales ;#nuestro valor verdadero es 0.5671 y otras variables
a,b,np=-1,2,100
delta=(b-a)/(np-1)
vv=0.5671
i=1
vciclos=[]
verror=[]

vx=[a+i*delta for i in range(np)]

#creo un grupo de graficas
plt.figure(1)
#grafico la funcion 
plt.subplot(1,2,1)
plt.plot(vx,funx(vx))
max(funx(vx))

#redefno el punto medio
pm=xm(a,b)

#definimos el error porcentual 
def error(vv,pm):
    e = ((vv-pm)/vv)*100
    return e 

#erp= error de 100; error deseado= 0.001
erp=100
err=0.01

while(erp>err):
    erp=abs(error(vv,pm))
    verror.append(erp)
    vciclos.append(i)
    if (fpx(a)*fpx(pm)<0):
        b=pm
    else: 
        a=pm
    pm=xm(a,b)
    print('a =',"{:.4f}".format(a),'b =', "{:.4f}".format(b),'punto medio =', "{:.4f}".format(pm),
          'funcion evaluada en el punto medio = ', "{:.4f}".format(fpx(pm)), 'error=', abs(error(vv,pm)))    
    i=i+1
plt.subplot(1,2,2)
plt.semilogy()
plt.plot(vciclos,verror)

#método de la regla falsa
def pfalsa(a,b,fa,fb):
    m=(fb-fa)/(b-a)
    return (m*b-fb)/m

vferror,vfciclos=[],[]
erp=100 
i=1
while(erp>err):
    erp=abs(error(vv,pfalsa(a,b,fa,fb)))
    print(pfalsa(a,b,fa,fb),erp)
    verror.append(erp)
    vciclos.append(i)
    if (fa*fun(pfalsa(a,b,fa,fb))<0):
        b=pfalsa(a,b,fa,fb)
    else: 
        a=pfalsa(a,b,fa,fb)
    pm=xm(a,b)
    i=i+1
    #print('a =',"{:.4f}".format(a),'b =', "{:.4f}".format(b),'punto medio =', "{:.4f}".format(pm),
          #'funcion evaluada en el punto medio = ', "{:.4f}".format(fpx(pm)), 'error=', abs(error(vv,pm))) 
plt. plot(vfciclos,vferror)

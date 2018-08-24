
#  clase 24/08/2018
#  mínimos cuadrados, objetivo :  modificar la dispersión. 
#  aproximando a una recta y = mx+b+E

import matplotlib.pyplot as plt 
import random as ra #importo librería aleatoria

def linea(m,b,vi,vf): 
    np = 100  #número de puntos
    delta = (vf -vi)/(np-1) # incremente para calcular algo en el dominio
    vx = [vi+i*delta for i in range (np)] # puntos que va tener el domino
    vy = [m*i+b+ra.gauss(0,5) for i in vx] # puntos en el codominio
    return vx,vy

m,b,vi,vf = 2,5,-10,10 #doy mis valores 

valx,valy=linea (m,b,vi,vf)

ra.gauss(0,5) #(media, desviación estándar)

vra=[ra.gauss(0,1) for i in range(10)] #valores aleatorios

plt.plot(valx,valy,"o")
#plt.plot(vra)


import numpy as np 
import matplotlib.pyplot as plt 

def f(t):
    return A*np.cos(w*t+b)

def g(t):
  return B*np.sin(w2*t+c)

# definimos el rango de dos variables y el intervalo en el que cambiann
t1 = np.arange(0.0, 5.0, 0.01)

# crea el grupo de graficas. 
plt.figure(1)

############################################################
plt.subplot(221)
A=6
w=1
b=1
B=6
w2=1
c=1
plt.plot(t1, f(t1),'b', label='A=6, w=1, b=1')
plt.plot(t1, g(t1),'k', label='B=6, w"=1, c=1')
plt.ylabel('f(t),g(t)')
plt.title('Cuatro gráficas con dos funciones;', fontsize='small')

legend = plt.legend(loc='upper center', shadow=True, fontsize='x-small')

##############################################################
plt.subplot(222)
A=6
w=9
b=3
B=7
w2=8
c=4
plt.plot(t1, f(t1),'b', label='A=6, w=9, b=3')
plt.plot(t1, g(t1),'k', label='B=7, w"=8, c=4')

legend = plt.legend(loc='upper center', shadow=True, fontsize='x-small')

plt.title('Azul: f(t)=Acos(wt+b) Negra: g(t)=Bsen(w"t+c);', fontsize='small')

#############################################
plt.subplot(223)
A=4
w=2
b=7
B=6
w2=9
c=5
plt.plot(t1, f(t1),'b', label='A=4, w=2, b=7')
plt.plot(t1, g(t1),'k', label='B=6, w"=9, c=5')
plt.xlabel('t')
plt.ylabel('f(t),g(t)')

legend = plt.legend(loc='upper center', shadow=True, fontsize='x-small')
##################################
plt.subplot(224)
A=8
w=3
b=7
B=6
w2=8
c=9
plt.plot(t1, f(t1),'b', label='A=8, w=3, b=7')
plt.plot(t1, g(t1),'k', label='B=6, w"=8, c=9')
plt.xlabel('t')

legend = plt.legend(loc='upper center', shadow=True, fontsize='x-small')

# guarda la grafica
plt.savefig('Dosfunciones.png')
# muestra la grafica 
plt.show()

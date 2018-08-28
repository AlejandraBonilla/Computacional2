import math 
import matplotlib.pyplot as plt 

def f(x):
    y=(math.exp(-x)-x)
    return y

def fp(x):
    y=(-1*math.exp(-x)-1)
    return y

p0=0 # en dónde empieza
tol=0.001 # presición
xi=10 #número de iteraciones
i=1

vciclos=[]
verror=[]
vv=0.5671

def error(vv,p):
    e = ((vv-p)/vv)*100
    return e 

print('i', 'xi', 'error')

while i<=xi:
  p=p0-f(p0)/fp(p0)
  print(i,p,abs(error(vv,p))) # imprime la iteración, i,  y la función evaluado en xi
  vciclos.append(i)
  verror.append(error(vv,p))
  if abs(p-p0)<tol:
   print("La solucion es ",p," despues de ",i," iteraciones",error(vv,p))
  break
  i=i+1
  p0=p

plt.plot(vciclos,verror)
plt.title('Grácia de iteraciones vs error en el método Newton-Rsphson')
plt.xlabel('ciclos')
plt.ylabel('error')
plt.savefig('tarea5.png')
plt.show()

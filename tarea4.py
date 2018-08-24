import math
import matplotlib.pyplot as plt

def f(x):
  return (math.exp(-i) -i for i in x)

def g(x):
  g = (math.exp(-x))
  return g

p0=0 #valor inicial para la función g(x)
tol=0.001 #presición 
xi=20 #número de iteraciones
i=0 #inicia el contador en 0

vciclos=[]
verror=[]
vv=0.5671

def error(vv,p):
    e = ((vv-p)/vv)*100
    return e 

print('i', 'xi')
while i<=xi:
    p=g(p0) #función evaluada en cada iteración
    print(i,p,abs(error(vv,p))) # imprime la iteración, i,  y la función evaluado en xi
    vciclos.append(i)
    verror.append(error(vv,p))
    if abs(p-p0)<tol:
        print("El punto fijo es ",p," despues de ",i," iteraciones", "con un error de",error(vv,p))
        break

    i=i+1
    p0=p

plt.plot(vciclos,verror)
plt.title('Grácia de iteraciones vs error en el método del punto fijo')
plt.xlabel('ciclos')
plt.ylabel('error')
plt.savefig('tarea4.png')
plt.show()

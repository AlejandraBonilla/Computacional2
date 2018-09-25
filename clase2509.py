import time 

def cuadrado(x):
    return x*x

# cuando tengo un funcioón sencilla puedo definirla por medio de la fución lambda x:x*x

vx=[]
for i in range(10): 
    vx.append(i)
    
print (vx)

#esta función lo que hace es aplicar un for a cuadrado de manera más compacta 
cmapeo=map(cuadrado,vx)#(nombre del vector, localidad a la que quiero accesar)
    #map aplica la función a la definición y se asegura qu es ecumpla la regla 3
    
                    #otra forma de escribilo es 
for i in cmapeo: #for i in range(len(cmapeo)): 
    print (i)       #print cmapeo[i]

#utilizadno una función lambda 
cmapeo2=map(lambda x:x*x,vx)

#otra manera es vx y vy=[ciadrado(i) for i in vx] lod dos con la misma longitud. 

#filter: es un filtro y da los valores que cumplen la condición "una manera reducida del ciclo for". 

#reduce[lamnda x,y:x+y,vx] es igual a: 
ht=[]
vi=time.time()

for j in range(1000): 
    vi=time.time()
    for i in range (10000000):
        i=i+i        
    vf=time.time()
    ht.append(vf-vi)
    print("termino",vf-vi)

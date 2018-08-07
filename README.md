# Computacional2

# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import math 

def fac(a,b): 
    lista1=[]
    x=a*b
    exp=a**b
    for i in range(10):
        lista1.append(i*a)
    return x, exp, lista1


def punto(a,b):
    suma=0
    for i in range(len(a)):
        suma=suma+a[i]*b[i]
    return suma 


a,b,c,hola=10,7,6,"°"

prod, expo, lista1=fac(a,b)
va=[6,7,8,9,10]
vb=[10,5,-1,7,10]

print (punto(va,vb))


print (fac(a,b))
print (fac(b,c))


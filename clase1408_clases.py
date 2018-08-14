# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

class persona: 
    def _init_(self):
      print  ("Simepre se ejecuta")
        # cada método tienen un nombre; este método se llama dos_m
    def dos_m(self):
      print  ("Tengo dos manos")
      
#######################################################################

class gato:
    
    def __init__(self,energia,hambre):
     self.energia=energia
     self.hambre=hambre
     print ("se cree un gato")
     
    def jugar(self):
        if self.energia <=0 or self.hambre <=1:
            print ("no")
        else: 
            self.energia -=1
            self.hambre -=1
            print ("Jugar")
            
    def extra(self):
        self.energia +=1
        self.hambre +=3
        print ("extra")

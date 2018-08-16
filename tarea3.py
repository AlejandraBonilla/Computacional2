
#######################################################################
import random

class detector:
    
    def __init__(self,energia,tiempo,mx,my,masa):
     self.energia=energia
     self.tiempo=tiempo
     self.mx=mx
     self.my=my
     self.masa=masa
     print ("detector activado")
     
    def posicion(self):
        if self.energia <=0 or self.tiempo <=1:
            print ("no")
        else: 
            self.energia -=1
            self.hambre -=1
            print ("Jugar")
            
    def extra(self):
      

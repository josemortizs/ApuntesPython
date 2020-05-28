# Ejemplo de Herencia en Python

import math

#########################################################
class Punto():
    """Representación de un punto en el plano"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def mostrar(self):
        return str(self.x) + ":" + str(self.y)
    
    def distancia(self, punto):
        """ Devuelve la distancia entre dos puntos """
        dx = self.x - punto.x
        dy = self.y - punto.y
        return math.sqrt((dx*dx + dy*dy))
#########################################################


class Punto3d(Punto):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x,y)
        self.z = z
    
    @property
    def z(self):
        print("Doy z")
        return self.__z
    
    @z.setter
    def z(self, z):
        print("Cambio z")
        self.__z = z
    
    def mostrar(self):
        return super().mostrar() + ":" + str(self.__z)
    

punto3d = Punto3d(1, 2, 3)
print(punto3d.mostrar())
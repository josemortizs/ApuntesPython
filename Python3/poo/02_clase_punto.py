import math

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


if __name__ == '__main__' : 
    
    punto1 = Punto()
    punto2 = Punto(4,5)
    print(punto1.distancia(punto2))
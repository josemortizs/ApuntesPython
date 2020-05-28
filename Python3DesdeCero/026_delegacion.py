# Ejemplo de DELEGACIÓN:

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

#########################################################
class Circulo():
    
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    
    def mostrar(self):
        return "Centro: {0} - Radio: {1}".format(self.centro.mostrar(), self.radio)



# Creamos un objeto de tipo círculo y otro de tipo punto:

punto = Punto(5, 5)
circulo = Circulo(punto, 7)
print(circulo.mostrar())
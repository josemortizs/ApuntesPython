# Ejemplo de encapsulación:

class Circulo():
    def __init__(self, radio):
        self.radio = radio
    
    @property
    def radio(self):
        print("Estoy dando el radio")
        return self.__radio

    @radio.setter
    def radio(self, radio):
        if radio >= 0:
            self.__radio = radio
        else:
            print("Radio debe ser positivo")
            self.__radio=0


circulo = Circulo(5)
print(circulo.radio)
circulo.radio = -5
print(circulo.radio)

circulo2 = Circulo(-3)
print(circulo2.radio)
class Circulo():
    # Constructor
    def __init__(self: object, radio: int):
        self.radio = radio

    @property
    def radio(self: int) -> int:
        print("Estoy dando el radio")
        return self._radio
    
    @radio.setter
    def radio(self: int, radio: int):
        if radio >= 0:
            self._radio = radio
        else:
            self._radio = 0
            raise ValueError("El radio debe ser positivo")

    @radio.deleter
    def radio(self: int):
        del self._radio
        
    # Reescribimos el método __str__ 
    def __str__(self : object):
        clase = type(self).__name__
        mensaje = "Clase: {0}, su radio es {1}"
        return mensaje.format(clase, self.radio)
    
    # Reescribimos el método equal para poder usarlo con nuestra clase
    def __eq__(self, otro):
        return self.radio == otro.radio
    


c1 = Circulo(5)
c2 = Circulo(2)

print(c1==c2) # Puedo usarlo, siendo objetos, porque hemos sobrescrito el método equal (__eq__)
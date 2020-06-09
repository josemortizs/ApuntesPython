class Circulo():
    # Constructor
    def __init__(self, radio):
        self.radio = radio

    @property
    def radio(self):
        print("Estoy dando el radio")
        return self._radio
    
    @radio.setter
    def radio(self, radio):
        if radio >= 0:
            self._radio = radio
        else:
            self._radio = 0
            raise ValueError("El radio debe ser positivo")

    @radio.deleter
    def radio(self):
        del self._radio



c = Circulo(5)
print(c.radio)


    
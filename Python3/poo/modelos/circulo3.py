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



c = Circulo(5)
print(c.radio)

c1 : Circulo = Circulo(6)
print(c1.radio)
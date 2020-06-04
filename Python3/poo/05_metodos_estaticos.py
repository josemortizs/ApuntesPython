# Ejemplo de métodos estáticos:

class Calculadora():
    def __init__(self, nombre):
        self.nombre = nombre
    def modelo(self):
        return self.nombre
    
    @staticmethod
    def sumar(x,y):
        return x+y



c1 = Calculadora("basica")

print(Calculadora.sumar(3,2))
print(getattr(c1, "nombre"))
print(setattr(c1, "nombre", "compleja"))
print(getattr(c1, "nombre"))

# Tambien existe: hasattr(objeto, atributo) y delattr(objeto, atributo)

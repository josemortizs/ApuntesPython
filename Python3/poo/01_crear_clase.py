# Ejemplo de clase

class EjemploClase() : 
    atributo_de_clase = 1
    def metodo(self) : 
        self.atributo_de_objeto = 2

objetoEjemplo = EjemploClase()
objetoEjemplo.metodo()

print(objetoEjemplo.atributo_de_clase)
print(objetoEjemplo.atributo_de_objeto)
print(EjemploClase.atributo_de_clase)
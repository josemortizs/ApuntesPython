# Ejemplo de: Atributos de clase

class Alumno() :
    contador = 0 # Atribujo de clase
    def __init__(self, nombre=""):
        self.nombre = nombre # Atributo de objeto
        self._atributoOculto = "1234abcd" # NO SE OCULTA, se trata de una convención
        self.__esteSiEstaOCulto = "abcd1234" # Intentar mostrar el valor de este atributo sí que ocultaría el parámetro (*)
        Alumno.contador += 1


pepe = Alumno("Pepe Ortiz")
alberto = Alumno("Alberto Ortiz")
paz = Alumno("Paz")

print(paz.nombre)
print(pepe.nombre)
print(alberto.nombre)
print(pepe.contador)
print(alberto.contador)
print(Alumno.contador)
print(pepe.__atributoOculto)

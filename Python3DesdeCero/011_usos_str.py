# Métodos de formato para STR:

variableSTR = "hola, ¿Cómo estás?"

print(variableSTR.capitalize()) # salida: Hola, ¿cómo estás?
print(variableSTR) # salida: hola, ¿Cómo estás?
# ¡OJO!, no modifica el valor de la variable, le aplica formato.

variableSTR = variableSTR.capitalize()
print(variableSTR) # Ahora sí ha modificado el valor de variableSTR

print(variableSTR.upper()) # salida: HOLA, ¿CÓMO ESTÁS?
print(variableSTR.lower()) # salida: hola, ¿cómo estás?

cadena = "holA mundO"
print(cadena.swapcase()) # salida: HOLa MUNDo
print(cadena.title()) # salida: Hola Mundo

cadena = "bienvenido a mi aplicación"
print(cadena.count("a")) # salida: 3
print(cadena.count("a", 16)) # Búsqueda desde la posición 16
print(cadena.count("a", 10, 16)) # Búsqueda desde la posición 10 hasta la 16

print(cadena.find("mi")) # Devuelve la posición de "mi" en la cadena o -1 si no lo encontrase
print(cadena.startswith("b")) # ¿Comienza "cadena" por TRUE?
print(cadena.endswith("ción")) # ¿Termina con "ción"?

cadena = cadena.replace("a", "u") 
print(cadena) # salida: bienvenido u mi uplicución

hora = "12:23:12"
ejemploArray = hora.split(":")
print(ejemploArray) # salida: ['12', '23', '12']

ejemplo = "Linea1\nLinea2\nLinea3"
ejemploArray2 = ejemplo.splitlines()
print(ejemploArray2) # salida: ['Linea1', 'Linea2', 'Linea3']


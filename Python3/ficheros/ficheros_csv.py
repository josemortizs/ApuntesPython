# Ejemplo de trabajo con ficheros CSV:

import csv

fichero = open("ejemplo1.csv", "r")

contenido = csv.reader(fichero)

print(list(contenido))
print(list(contenido))

fichero.seek(0)

datos = list(contenido) # Almacenamos en la variable "datos" una lista con el contenido del fichero CSV

# Podemos usar una lista como si se tratase de un array bidimensional:
print(datos[0][1]) # salida: Apples
print(datos[0][2]) # salida: 73
print(datos[0][0]) # salida: 4/5/2015 13:34


# Y recorrerla:

fichero.seek(0)

for row in contenido:
    print("Fila: {0} - Columna: {1}".format(contenido.line_num, str(row)))
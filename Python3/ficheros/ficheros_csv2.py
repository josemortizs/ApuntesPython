# Ejemplo2 de trabajo con ficheros CSV:

import csv

fichero = open("ejemplo2.csv", "r")
contenido = csv.reader(fichero, quotechar='"')

for row in contenido :
    for colum in row : 
        print(contenido.line_num, colum)

fichero.close()

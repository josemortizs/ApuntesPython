# Ejemplo2 de trabajo con ficheros CSV:

import csv

fichero = open("ejemplo4.csv", "w")

contenido = csv.writer(fichero)

contenido.writerow(['4/5/2015 3:41', 'Cherries', '85'])

fichero.close()
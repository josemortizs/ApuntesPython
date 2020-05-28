# Importación de módulos (librerías)

import math # Importaría, completa, la librería MATH

print(math.sqrt(9)) # salia: 3.0

from math import sqrt # Importaría la clase SQRT, y ésta podría usarse sin el nombre del módulo:
print(sqrt(9)) # salida: 3.0

from random import randint
print(randint(1,100)) # Imprime un número aleatorio, del 1 al 100...

import time
time.sleep(1) # "Duerme" la ejecución durante 1 segundo

import datetime
print(datetime.datetime.now())

import os
print(os.system("clear"))
os.system("ls -lo")

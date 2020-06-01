# Ejemplo de trabajo con FICHEROS en Python
# Modos de acceso: 
# r     -> Solo lectura
# rb    -> Solo lectura en modo binario
# r+    -> Lectura y escritura
# rb+   -> Lectura y escritura binaria
# w     -> Solo escritura, sobreescribe si existe. Crea el archivo si no existe.
# wb    -> Igual, en binario
# w+    -> Escritura y lectura. Sobreescribe si existe. Crea el archivo si no existe.
# wb+   -> Igual, en binario.
# a     -> Añadido (agrega contenido). Crea el archivo si no existe.
# a+    -> Añadido y lectura. Crea el archivo si no existe
# ab+   -> Igual, en binario...

fichero = open("ejemplo1.txt", "r")

if fichero.closed != True :
    print("El fichero está abierto")

print("El modo de acceso al fichero ha sido {0}".format(fichero.mode))
print("El nombre del fichero es:  {0}".format(fichero.name))

fichero.closed

# Leer todo el contenido del fichero: 

with open("ejemplo1.txt", "r") as archivo : 
    contenido = archivo.read() # El fichero se cierra tras cargar el contenido en la variable: contenido

print(contenido)

# Otras opciones:

fichero = open("ejemplo1.txt", "r")
print(fichero.read())
print(fichero.tell()) # Posición del puntero dentro del fichero

fichero.seek(0) # Sitúa el puntero en la posición 0
fichero.closed

# Leer línea a línea:

fichero = open("ejemplo1.txt", "r")

print(fichero.readline()) # imprime la primera línea
print(fichero.readline()) # imprime la segunda línea
print(fichero.readline()) # No hay más líneas, no imprime nada

fichero.seek(0)

print(fichero.readlines()) # Nos devuelve una lista con cada línea en una posición

fichero.closed

# Escribir en un fichero: 

fichero = open("ejemplo2.txt", "w")
fichero.write("Prueba de escritura \n")
fichero.writelines(["Otra línea \n", "Otra línea más...\n"])
fichero.closed

# Formas de recorrer un fichero:

with open("ejemplo2.txt", "r") as fichero : 
    for linea in fichero : 
        print(linea)

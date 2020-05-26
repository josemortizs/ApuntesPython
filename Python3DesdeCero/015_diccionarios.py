# Usos de Diccionarios:

diccionario = {'uno' : 1, 'dos' : 2, 'tres' : 3}
print(type(diccionario)) # salida: <class 'dict'>

print(diccionario["dos"]) # salida: 2

jugador = {}
jugador["nombre"] = "Pepe Ortiz"
jugador["dorsal"] = 11
print(jugador) # salida: {'nombre': 'Pepe Ortiz', 'dorsal': 11}

# Operadores básicos:
print(len(jugador)) # salida: 2

# Otros operadores:
# del jugador["nombre"]
# "nombre" in jugador

# IMPORTANTE: Los diccionarios son mutables
# Y se copian por referencia, no por valor, ejemplo:

dicc1 = {}
dicc2 = dicc1 # Ahora, ambas variables harían referencia al mismo diccionario

# Si queremos copiar por valor:
dicc2 = dicc1.copy()



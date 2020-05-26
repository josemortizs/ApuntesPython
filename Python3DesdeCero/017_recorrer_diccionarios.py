# Como recorrer Diccionarios:

diccionario = {'uno' : 1, 'dos' : 2, 'tres' : 3}

for clave in diccionario.keys():
    print(clave) 
# salida: 
# uno
# dos
# tres

for valor in diccionario.values(): 
    print(valor)
# salida: 
# 1
# 2
# 3

for clave, valor in diccionario.items():
    print(clave, " -> ", valor)
# salida: 
# uno -> 1
# dos -> 2
# tres -> 3
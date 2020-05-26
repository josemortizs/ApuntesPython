# LISTAS:

lista1 = [] # Lista vacía

# Se pueden agregar elementos de distinto tipo
lista2 = [1, "abc", True] # Hay gente que solo quiere ver arder el mundo...

for elemento in lista2:
    print(elemento)

listaLetras = ['a', 'e', 'i', 'o', 'u']
listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numero, letra in zip(listaNumeros, listaLetras):
    print(numero, letra)

print(2 in listaNumeros) # salida: True

# Concatenar listas: 
listaNumeros = listaNumeros + [10, 11, 12]
print(listaNumeros) # salida: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Multiplicación de listas:
listaLetras *= 2
print(listaLetras) #salida: ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u']

# slice en listas:

subLista = listaLetras[2:4]
print(subLista) # salida: ['i', 'o']
subLista2 = listaLetras[0:5:2] 
print(subLista2) # salida: ['a', 'i', 'u']

# Algunas funciones para listas:
print(len(listaLetras)) # salida: 10 
print(max(listaNumeros)) # salida: 12

# Otras funciones para listas: sorted(lista), sum(lista), min(lista)...

# IMPORTANTE:
# Si bien, cuando hablábamos de string (str) decíamos que se trataba
# de elementos inmutables, las listas sí que son mutables y su contenido
# puede ser modificado. Los métodos que se usan, en dicha lista, modifican
# esta, no devuelven otro objeto con el resultado.

# Agregar nuevos elementos:

print(lista1) # salida: []
lista1.append("Pepe Ortiz")
print(lista1) # salida: ['Pepe Ortiz']

# CUIDADO!!, Al copiar listas, o elementos de una lista, se copian por referencia,
# para copiarlas por valor: 

lista1 = lista2[:]


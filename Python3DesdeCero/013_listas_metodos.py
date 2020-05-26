# Métodos de inserción:

lista = [1, 2, 3]
lista.append(4)
print(lista) # salida: [1, 2, 3, 4]

lista2 = [5, 6]
lista.extend(lista2)
print(lista) # salida: [1, 2, 3, 4, 5, 6]

lista.insert(0, 100)
print(lista) # salida: [100, 1, 2, 3, 4, 5, 6]

# Métodos de eliminación:

temporal = lista.pop()
print(temporal) # salida: 6
print(lista) # salida: [100, 1, 2, 3, 4, 5]
# pop() ha eliminado el último elemento de la lista y lo ha devuelto
# pop(parámetro) acepta un parámetro numérico, el índice a eliminar


lista.remove(3) 
print(lista) # salida: [100, 1, 2, 4, 5]
# remove(parámetro) elimina todos los elementos de la lista que coincidan con el parámetro enviado

# Métodos de ordenación:

lista.reverse()
print(lista) # salida: [5, 4, 2, 1, 100]
# Otros métodos: lista.sort(), lista.sort(reverse=True)...

# Métodos de búsqueda:
print(lista.count(5)) # ¿Cuántos 5 hay en la lista?
print(lista.index(5)) # ¿En qué posición aparece?
print(lista.index(5, 2)) # ¿En qué posición aparece a partir de la posición 2?

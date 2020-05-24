# Ejemplos de While, Break y Continue

cont = 0
while cont < 5: 
    print("La variable cont ahora vale: %d" % cont)
    cont += 1

cont2 = 0
while cont2 < 5: 
    print("La variable cont2 ahora vale: %d" % cont2)
    if cont2 == 2:
        break # Termina el bucle
    cont2 += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue # Salta a la siguiente iteración
  print(i)
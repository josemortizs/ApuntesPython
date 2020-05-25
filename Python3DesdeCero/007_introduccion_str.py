# Introducció a las cadenas de caracteres

# Concatenación:
cadena1 = "Hola, "
cadena2 = "¿Cómo estás?"
cadena3 = cadena1 + cadena2
print(cadena3) # salida: Hola, ¿Cómo estás?

# Multiplicación: 
cadena4 = cadena1 * 4
print(cadena4) # salida: Hola, Hola, Hola, Hola, 

# Indexación:
print(cadena1[0]) # salida: H

# Longitud:
print(len(cadena1)) # salida: 6

# Recorrer STR:
cadena = "Informática"
for caracter in cadena:
    print(caracter)

# Operadores de pertenencia: 
print("a" in cadena) # salida: True
print("b" in cadena) # salida: False
print("Info" not in cadena) # salida: False

# Usos de SLICE:
print(cadena[2:5]) # salida: for
print(cadena[2:7:2]) # salida: frá
print(cadena[5:]) # salida: mática
print(cadena[:5]) # salida: Infor
print(cadena[::-1]) # salida: acitámrofnI








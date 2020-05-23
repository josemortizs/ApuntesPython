# Tipos de datos numéricos en Python:

numeroEntero = 7
print(type(numeroEntero)) # salida: <class 'int'>

numeroReal = 7.5
print(type(numeroReal)) # salida: <class 'float'>

# Funciones integradas en el lenguaje:

print(abs(-7)) # salida: 7
print(divmod(7,2)) # salida: (3, 1) 
print(hex(7)) # salida: 0x7
print(pow(2,3)) # salida: 8
print(round(7.567,1)) # salida: 7.6
print(round(7.567,2)) # salida: 7.57

# Operadores
print(3+4) # salida: 7
print(8-1) # salida: 7
print(2*3) # salida: 6
print(7/2) # salida: 3.5
print(7//2) # salida: 3
print(7%2) # salida: 1
print(2**3) # salida: 8

# Casting
# De: https://www.w3schools.com/python/python_casting.asp
x = int(1)   # salida: 1
print(x)
y = int(2.8) # salida: 2
print(y)
z = int("3") # salida: 3
print(z)

x = float(1)     # salida: 1.0
print(x)
y = float(2.8)   # salida: 2.8
print(y)
z = float("3")   # salida: 3.0
print(z)
w = float("4.2") # salida: 4.2
print(w)

x = str("s1") # salida: 's1'
print(x)
y = str(2)    # salida: '2'
print(y)
z = str(3.0)  # salida: '3.0'
print(z)

# Librería math:
import math
print(math.sqrt(9)) # salida: 3.0
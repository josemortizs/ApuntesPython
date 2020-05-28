# Funciones en Python:

#Ejemplo:

def CalcularValorMaximo( num1, num2 ) :
    if num1 > num2:
        return num1
    else:
        return num2

#
maximo = CalcularValorMaximo(1, 2)
print(maximo)

# IMPORTANTE: En python el paso de parámetros siempre se hace por referencia

def factorial(n):
    """Calcula el factorial de un número"""
    resultado = 1
    for i in range(1, n+1):
        resultado*=i
    return resultado


num = int(input("Introduce el número a calcular su factorial: "))

print(factorial(num))
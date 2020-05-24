# La función input recoge un str, importante

print("Hola, ")
nombre = input("¿Cómo te llamas? ")
print("Hola " + nombre)

edad = int(input("¿Cuántos años tienes? "))
if edad > 18:
    print("Eres mayor de edad!")
else:
    print("Qué joven eres!")

# Formateo de salida:
# %s (str), %d (int), %f (float), $.2f (float, dos decimales)
print("Su nombre es %s y tiene %d años" % (nombre, edad))

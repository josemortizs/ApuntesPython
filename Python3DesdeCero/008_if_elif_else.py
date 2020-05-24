# Ejemplo de IF - ELIF - ELSE

edad = int(input("Introduce tu edad: "))

if edad >= 0 and edad < 100 : 
    print("Edad válida")
elif edad < 0:
    print("NO PUEDES TENER UNA EDAD NEGATIVA!")
else:
    print("¿De verdad eres tan mayor?")
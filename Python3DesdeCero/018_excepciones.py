# CONTROL DE EXCEPCIONES:

while True:
    try:
        x = int(input("Introduce un número: "))
        break
    except ValueError:
        print("Debes introducir un número")


num = input("Dime un número: ")
try:
    print(10/int(num))
except ValueError:
    print("No se puede convertir a entero")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
else:
    print("Se ha producido otro tipo de error")
finally:
    print("Este excepción siempre se ejecuta si ha habido una excepción")


while True:
    try:
        x = (10/int(input("Introduzca un número: ")))
        break
    except ValueError:
        print("Debes intrducir un número")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except: # también sería válida la palabra reservada: else
        print("Otro error")
    finally: 
        print("Se ha producido un error")

print(x)
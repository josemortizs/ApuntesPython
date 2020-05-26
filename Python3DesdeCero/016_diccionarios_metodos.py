# Algunos métodos sobre diccionarios:

jugador = {}
jugador["nombre"] = "Pepe Ortiz"
jugador["dorsal"] = 11
print(jugador) # salida: {'nombre': 'Pepe Ortiz', 'dorsal': 11}

jugador.clear()
print(jugador) # salida: {}

jugador = {}
jugador["nombre"] = "Pepe Ortiz"
jugador["dorsal"] = 11
print(jugador) # salida: {'nombre': 'Pepe Ortiz', 'dorsal': 11}

datosJugada = {"recepcion" : 1, "ataque" : 2}
jugador.update(datosJugada)
print(jugador) # salida: {'nombre': 'Pepe Ortiz', 'dorsal': 11, 'recepcion': 1, 'ataque': 2}

# Otros: copy(), jugador.get("nombre"), jugador.pop("nombre")
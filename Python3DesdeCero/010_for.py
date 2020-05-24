# Ejemplos de FOR

equipos = ["CV Berja", "Univoley", "Adra"]

for equipo in equipos:
    print(equipo)

for equipo in equipos:
    if equipo == "Univoley":
        break
    print(equipo)

for equipo in equipos:
    if equipo == "Univoley":
        continue
    print(equipo)

for i in range(6):
    print("i vale: %d" % i)

for i in range(2, 6):
    print("i vale: %d" % i)

for i in range(2, 6, 2):
    print("i vale: %d" % i)


# Uso Else in For:
for equipo in equipos:
    print(equipo)
else:
    print("For finalizado!")
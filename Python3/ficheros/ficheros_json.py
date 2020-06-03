import json

datos_json = '{"nombre": "carlos", "edad": 23}'

datos = json.loads(datos_json)

print("datos es una variable de tipo: {0}".format(type(datos))) # salida: datos es una variable de tipo: <class 'dict'>

with open("ejemplo1.json") as fichero:
    datos = json.load(fichero)

print(datos) # salida: {'bookstore': {'book': [{'title': {'_lang': 'en', '__text': 'Everyday Italian'}...

fichero = open("ejemplo2.json", "w") # Abrimos el fichero en modo escritura
json.dump(datos_json, fichero)
fichero.close()
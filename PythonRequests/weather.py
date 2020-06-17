import requests
import os

# Previamente, mediante la terminal, declaré una variable con el nombre open_weather_key
# y le asigné el valor de mi clave de open weather, mediante la instrucción: 
# export open_weather_map="aquí_va_la_api_key"
api_key = os.getenv("open_weather_key")
print(api_key)

parametros = {
    "q" : "Berja",
    "mode" : "json",
    "units" : "metric",
    "APPID" : api_key
}

# Realizamos una petición de tipo GET:

request = requests.get("http://api.openweathermap.org/data/2.5/weather", params=parametros)

# Borramos la consola antes de mostrar los datos:
os.system("clear")

print("Petición realizada a: \n {0}".format(request.url))
print("Código de respuesta: {0}".format(request.status_code)) # Si request.status_code == 200 -> OK
print("JSON devuelto: \n {0}".format(request.json()))

datos = request.json() # datos es una variable de tipo Diccionario que contiene la información del json
print("La temperatura es de: {0}".format(datos["main"]["temp"]))
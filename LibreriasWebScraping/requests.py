import requests
import sys

print('Googleando...') # Texto mostrado mientras descargamos la página de Google...

if len(sys.argv) > 1:
    search = ' '.join(sys.argv[1:])
    res = requests.get('http://google.com/search?q=' + search)
    print(res.text)
else:
    print('Debe introducir algún parámetro')

import requests

r = requests.get('https://api.github.com/users/josemortizs/repos')
print(r.url)
print(r.text)
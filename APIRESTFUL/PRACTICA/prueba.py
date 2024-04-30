

import requests
import json
url = 'https://rickandmortyapi.com/api/character/?page=1'

response = requests.get(url)
print(response.content)
print('------------------------------------------')
r_json = response.json()
print(r_json)
if r_json == response.content:
    pritn('SIIIIIIIIIIIIIIIIIIIIIIIIIII')
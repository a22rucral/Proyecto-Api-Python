import requests
import json


# Offset indica de cuanto en cuanto hay en una pagina listada
def get_pokemons( offset=0):
    name_pokemon = input('Dime el nombre del pokemon a buscar')
    url = f'https://pokeapi.co/api/v2/pokemon/{name_pokemon}'
    # Siempre y cuando lo que nos esten pasando sea diferente de 0 en caso contrario mandar diccionario de 0
    args = {'offset': offset} if offset else {}
    response = requests.get(url, params=args)

    if response.status_code == 200:
        payload = response.json()
        # Intentara obtener esta llave y si no existe devuelve lista vacia
        result = payload.get('results', [])

        if result:
            for pokemon in result:
                name = pokemon['name']
                print(name)

    next = input('continuar listando [S/N]').upper()
    if next == 's'.upper():
        get_pokemons(offset=offset + 20)


if __name__ == '__main__':
    get_pokemons()

# end point es una url

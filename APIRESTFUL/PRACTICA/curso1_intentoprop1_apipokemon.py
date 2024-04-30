import requests
import json


# Offset indica de cuanto en cuanto hay en una pagina listada
def get_pokemons(offset=0):
    name_pokemon = input('Dime el nombre del pokemon a buscar')
    url = f'https://pokeapi.co/api/v2/pokemon-form/{name_pokemon}'
    # Siempre y cuando lo que nos esten pasando sea diferente de 0 en caso contrario mandar diccionario de 0
    args = {'offset': offset} if offset else {}
    r = requests.get(url, params=args)

    if r.status_code == 200:
        r_json = r.json()
        print("\n Codigo de pokemon: ", r_json["id"], "\nNombre : ", r_json["name"],
              "\nVersion : ", r_json["version_group"]["name"],
              "\nPokemon tipo: ", r_json["types"][0]["type"]["name"], "\n")


if __name__ == '__main__':
    get_pokemons()

# end point es una url

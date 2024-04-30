# Dada la Api de rick y Morty haremos una serie de consultas que nos proporcionen información sobre la serie
# Estas son las siguientes opciones que se muestran en el menu y que podrás encontrar información
import sys
import webbrowser

# Opción 1 - Obtener el nombre del personaje dado el código.
# Opción 2 - recoger todas las especies del programa.
# Opción 3 - Listar los personajes que salen en un episodio
# Opción 4 - Listar todas las residencias
# Opción 5 - Listar los personajes que residen en la misma residencia
# Opción 6 - Mostrar información del personaje por el nombre
#
# Author: Alejandro Ruiz Crespo
#
# Fecha 24 / 04 / 2024

import requests
from time import sleep as s
from menu import Menu
import sys
import os
import webbrowser

list_of_species = []


# 1: NO 2:FUNCIONA 3: FUNCIONA 4: FUNCIONA  5: FUNCIONA  6: FUNCIONA
# Preguntarle a rafa que mas errores puedo controlar


def main():
    print('Chequeando conexion a internet: ')
    s(0.5)
    check_internet()
    s(0.5)
    args = ('Busca nombre de un personaje por su código', 'Lista todas las especies',
            'Listar los personajes que salen en un episodio', 'Listas todos los sitios de residencia',
            'Lista todos los personajes que residen en el mismo sitio',
            'Información de un personaje por su nombre')

    while True:
        print('\n')
        m = Menu('RICK Y MORTY', args)
        options = m.print_menu()

        match options:
            case 0:
                break
            case 1:
                search_character_by_code()
            case 2:
                search_species_of_character()
            case 3:
                list_episode_characters()
            case 4:
                residences_of_characters()
            case 5:
                character_residences()
            case 6:
                character_info()
        s(4)


def check_internet():
    try:
        response = requests.get('https://www.google.com')
        if response.status_code == 200:
            return print('Conexion a internet realizada con exito')
    except requests.ConnectionError:
        print('No se ha podido conectar a internet', file=sys.stderr)
        exit(1)


def catch_error(status_code):
    match status_code:
        case 400:
            raise ValueError('La solicitud no pudo ser entendida por el servidos debido a una sintaxis incorrecta')
        case 401:
            raise ValueError('La solicitud no pudo ser entendida por el servidor debido a una sintaxis incorrecta')
        case 403:
            raise ValueError('El servidor entendio la solicitud pero se niega a cumplirla')
        case 404:
            raise ValueError('El recurso solicitado no pudo encontrarse en el servidor')


# Uso 1.- Recorre caracteres hasta que coincide el código y devuelve el nombre junto al código del personaje
# Uso 2.- Recoge una lista de códigos y los busca guardando los nombre en una lista y devuelve la lista con los nombres
def search_character_by_code(list_of_code=None, pages=1, vuelta=False, code=None):
    if list_of_code is None:
        if vuelta is False:
            code = int(input('Dime el código del personaje: '))

        url = f'https://rickandmortyapi.com/api/character/{code}/?pages={pages}'
        vuelta = True
        response = requests.get(url)

        if response.status_code == 200:
            response_json = response.json()
            max_pages = 42
            try:
                print("\n Código de personaje: ", response_json["id"], "\nNombre Personaje: ", response_json["name"], )
                vuelta = False
            except:
                vuelta = True
        else:
            catch_error(response.status_code)
    else:
        list_of_names = []
        for code in list_of_code:
            url = f'https://rickandmortyapi.com/api/character/{code}'
            response = requests.get(url)
            if response.status_code == 200:
                response_json = response.json()
                list_of_names.append(response_json['name'])
            else:
                catch_error(response.status_code)
        return list_of_names
    if vuelta is True and pages < max_pages:
        pages += 1
        vuelta = True
        search_character_by_code(list_of_code, pages, vuelta, code)


# ¡Recorre los caracteres guardando las especies en lista y luego la hace conjunto y devuelve, pasa página True, espera!
def search_species_of_character(pages=1, vuelta=False):
    url = f'https://rickandmortyapi.com/api/character?page={pages}'
    global list_of_species
    if vuelta is False:
        list_of_species = []
        print('Recogiendo datos...')

    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        max_pages = response_json["info"]["pages"]
        result = response_json.get('results', [])

        if result:
            for character in result:
                species = character['species']
                list_of_species.append(species)
    else:
        catch_error(response.status_code)

    if pages < max_pages:
        pages += 1
        vuelta = True
        search_species_of_character(pages, vuelta)

    else:
        list_of_species = set(list_of_species)
        for i, specie in enumerate(list_of_species):
            print(f'{i + 1}.-{specie}')


# recorre los episodios hasta que coincida y recoge cod de caracteres de ese episodio y devuelve lista de nombres, pas p
def list_episode_characters(pages=1, vuelta=False, format_episode=''):
    if vuelta is False:
        season = int(input('Dime la temporada del episodio: '))
        chapter = int(input('Dime el episodio de la  temporada: '))
        format_episode = f'S{season:02d}E{chapter:02d}'
    list_of_code = []
    vuelta = True
    url = f'https://rickandmortyapi.com/api/episode/?page={pages}'

    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        max_pages = response_json['info']['pages']
        result = response_json.get('results', [])

        if result:
            for episode in result:
                if episode['episode'] == format_episode:
                    for character in episode['characters']:
                        character = int(character[42:])
                        list_of_code.append(character)
                        vuelta = False
        character_in_episode = search_character_by_code(list_of_code)
    else:
        catch_error(response.status_code)
    if vuelta is True and pages < max_pages:
        pages += 1
        list_episode_characters(pages, vuelta, format_episode=format_episode)
    else:
        for i, character in enumerate(character_in_episode):
            print(f'{i + 1}.-{character}')


# Recorre las localizaciones y devuelve 3 datos suyos, pasando páginas = True
def residences_of_characters(pages=1):
    url = f'https://rickandmortyapi.com/api/location?page={pages}'
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        result = response_json.get('results', [])

        if result:
            print(f'Id'.ljust(5), 'Nombre Residencia'.ljust(35), 'Tipo Residencia'.ljust(22))
            for location in result:
                print(f'{location["id"]}'.ljust(5), f'{location["name"]}'.ljust(35),
                      f'{location["type"]}'.ljust(22))

        next = input('\nContinuar listando [S/N]')
        if next.upper() == 'S':
            pages += 1
            residences_of_characters(pages)
    else:
        catch_error(response.status_code)


# Código recorre todas las páginas guardando cod personajes que vivan ahí y devuelve nombre, Pasando Páginas True
def character_residences(pages=1, vuelta=False, residence=None):
    if vuelta is False:
        residence = input('Dime la residencia que quieras saber: ')
    list_of_code = []
    vuelta = True
    url = f'https://rickandmortyapi.com/api/location/?page={pages}'

    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        result = response_json.get('results', [])
        max_pages = response_json['info']['pages']

        if result:
            for location in result:
                if location['name'] == residence:
                    for character in location['residents']:
                        character = int(character[42:])
                        list_of_code.append(character)
                    vuelta = False
    else:
        catch_error(response.status_code)

    location_residents = search_character_by_code(list_of_code)
    if vuelta is True and pages < max_pages:
        pages += 1
        character_residences(pages, vuelta, residence)
    else:
        for i, character in enumerate(location_residents):
            print(f'{i + 1}.- {character}')


# Código recorre los personajes y cuando coincida el nombre devuelve los datos de este, pasando páginas = True
def character_info(pages=1, name=None, vuelta=False):
    if vuelta is False:
        name = input('Dime el nombre del personaje: ')
    url = f'https://rickandmortyapi.com/api/character/?page={pages}'
    response = requests.get(url)
    vuelta = True

    if response.status_code == 200:
        response_json = response.json()  # todo implementar foto del personaje
        max_pages = response_json['info']['pages']
        result = response_json.get('results', [])

        if result:
            for character in result:
                if character['name'] == name:
                    print("\nCódigo de personaje: ", character["id"],
                          "\nNombre Personaje: ", character["name"],
                          "\nStatus: ", character["status"],
                          "\nNombre Genero: ", character["gender"],
                          "\nEspecie: ", character["species"],
                          )
                    image_url = character["image"]
                    vuelta = False
    else:
        catch_error(response.status_code)
    if vuelta is True and pages < max_pages:
        pages += 1
        character_info(pages, name, vuelta)
    else:
        question = input('Quieres ver una imagen del personaje (S/N) : ')
        if question.upper() == 'S':
            webbrowser.open(image_url)


if __name__ == '__main__':
    main()

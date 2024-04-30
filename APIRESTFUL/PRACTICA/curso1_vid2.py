import requests

if __name__ == '__main__':
    url = 'https://www.google.com'
    # crea un objeto de tipo response
    response = requests.get(url)
    # Tódo servidor nos devuelve como cliente un status que es un valor numerico, 200 indica que se ha realizado bien.
    # COndición de que si se realiza bien nos imprima el html = response.content
    if response.status_code == 200:
        content = response.content
        with open('google.html', 'bw') as file_google:
            file_google.write(content)
    
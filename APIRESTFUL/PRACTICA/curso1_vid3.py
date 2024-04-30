import requests

if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    # Creamos una variable con los argumentos que le vamos a pasar al get
    args = {'nombre': 'eduardo', 'curso': 'python', 'nivel': 'intermedio'}
    # Metemos el atributo de parametros y le indicamos la variable con los parametros
    response = requests.get(url, params=args)

    if response.status_code == 200:
        content = response.content
        print(response.url)
        print(content)

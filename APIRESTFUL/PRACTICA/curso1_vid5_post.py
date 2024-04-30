import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    payload = {'nombre': 'eduardo', 'curso': 'python', 'nivel': 'intermedio'}
    # Enviar encabezados
    headers = {'Conten-type' : 'application/json', 'access-toke': '12345'}
    # Diferencia entre el metodo post y el metodo get es que con el post creamo algun recurso en el servidor
    # y con el get lo obteniamos
    response = requests.post(url, data=json.dumps(payload), headers = headers)

    # json post se encarga de serializarlos
    # data los tienes que serializar tu
    print(response.url)

    if response.status_code == 200:
        # print(response.content)
    # leer encabezados
        headers_response = response.headers # dic
        server = headers_response['Server']
        print(server)
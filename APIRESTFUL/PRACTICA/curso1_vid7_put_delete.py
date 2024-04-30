import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/delete'
    payload = {'nombre': 'eduardo', 'curso': 'python', 'nivel': 'intermedio'}
    headers = {'Conten-type' : 'application/json', 'access-toke': '12345'}
    response = requests.delete(url, data=json.dumps(payload), headers=headers)

    '''
    GET obtener algun recurso 
    POST para crearlo 
    PUT para actualizarlo 
    DELETE para eliminarlo
    '''

    print(response.url)

    if response.status_code == 200:
        # print(response.content)
        headers_response = response.headers # dic
        server = headers_response['Server']
        print(server)
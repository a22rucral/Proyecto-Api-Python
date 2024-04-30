import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    # Creamos una variable con los argumentos que le vamos a pasar al get
    args = {'nombre': 'eduardo', 'curso': 'python', 'nivel': 'intermedio'}
    # Metemos el atributo de parametros y le indicamos la variable con los parametros
    response = requests.get(url, params=args)

    if response.status_code == 200:
        '''
                response_json = response.json()
            origin = response_json['origin']
           print(response_json['origin'])
            print(origin)
        '''
        # carga el objeto como diccionario
        response_json = json.loads(response.text)
        # guarda el valor de origin en la variable origin
        origin = response_json['origin']
        print(origin)

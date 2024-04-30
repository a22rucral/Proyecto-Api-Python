import requests
import json

if __name__ == '__main__':
    url = 'https://upload.wikimedia.org/wikipedia/commons/e/ee/Salida_humildad_y_paciencia_C%C3%B3rdoba_2016.jpg'
    # Colocando stream como verdadero dejamos la conexion abierta para posteriormente descargar el contenido
    response = requests.get(url, stream=True)
    with open('imagen.jpg', 'wb') as file:
        # iter content lo qeu hace es tomar tódo el contenido del servido y la va a descargar poco a poco
        for  chunk in response.iter_content(): # Descarga contenido poco a poco Imagen o archivos pesados
            file.write(chunk)
    response.close() # Cerramos la conexion

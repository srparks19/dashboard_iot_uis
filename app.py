from flask import Flask, render_template, Response
import csv
import io
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['iot']
collection = db['messages']
# Realiza la consulta a la base de datos
pipeline = [
    {"$group": {"_id": "$topic", "values": {"$push": {"$objectToArray": "$values"}}}}
]
result = list(collection.aggregate(pipeline))
topics_values = [{topic['_id']: [value['k'] for value in topic['values'][0]]} for topic in result]

@app.route('/')
def index():
    return render_template('index.html', topics_values=topics_values)

@app.route('/sensor/<estacion>/<dispositivo>')
def sensor(estacion,dispositivo):

    # Realizar la consulta a la base de datos para obtener los documentos del tema (topic) específico
    documentos = collection.find({'topic': estacion})

    # Crear una lista para almacenar los pares de timeStamp y values
    lista_time = []
    lista_value = []
    lista_resultados = []
    data_mapa = []

    # Iterar sobre los documentos y extraer los pares de timeStamp y values
    for documento in documentos:
        timestamp = documento['timeStamp']
        values = documento['values'][dispositivo]
        temperatura = documento['values']['temperatura']
        deviceUUID = documento['deviceUUID']
        latitud = documento['values']['latitude']
        longitud = documento['values']['longitude']
        lista_time.append(timestamp)
        lista_value.append(values)
        lista_resultados.append({'timeStamp': timestamp, 'values': values, 'deviceUUID':deviceUUID, 'latitude':latitud, 'longitude':longitud, 'temperatura':temperatura})
        data_mapa.append({'lon': longitud, 'lat': latitud, 'value':values})
    
    maximoNivel = max(lista_value)

    # Datos de para la gráfica
    data = {
        'timeStamp': lista_time,
        'values': lista_value
    }
    return render_template('sensor.html', topics_values=topics_values, data=data, estacion=estacion, 
                           dispositivo=dispositivo, lista_resultados=lista_resultados, maximoNivel=maximoNivel, data_mapa=data_mapa)

# Ruta para la descarga de datos en formato CSV
@app.route('/descargar_csv/<estacion>/<dispositivo>')
def descargar_csv(estacion, dispositivo):
    # Realizar la consulta a la base de datos para obtener los documentos del tema (topic) específico
    documentos = collection.find({'topic': estacion})
    # Iterar sobre los documentos y extraer los pares de timeStamp y values
    lista_resultados = []
    for documento in documentos:
        timestamp = documento['timeStamp']
        values = documento['values'][dispositivo]
        temperatura = documento['values']['temperatura']
        deviceUUID = documento['deviceUUID']
        latitud = documento['values']['latitude']
        longitud = documento['values']['longitude']
        lista_resultados.append({'timeStamp': timestamp, 'values': values, 'deviceUUID': deviceUUID, 'latitude': latitud, 'longitude': longitud, 'temperatura': temperatura})

    # Crear un objeto de tipo io.StringIO para escribir el CSV en memoria
    csv_buffer = io.StringIO()
    csv_writer = csv.DictWriter(csv_buffer, fieldnames=lista_resultados[0].keys())

    # Escribir los datos en el objeto de tipo io.StringIO
    csv_writer.writeheader()
    csv_writer.writerows(lista_resultados)

    # Crear la respuesta con el contenido CSV
    response = Response(csv_buffer.getvalue(), content_type='text/csv')
    response.headers.set('Content-Disposition', 'attachment', filename='datos.csv')

    return response

if __name__ == '__main__':
    app.run(debug=True)
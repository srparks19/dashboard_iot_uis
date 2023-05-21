from flask import Flask, render_template
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
    latitud = 7.131811
    longitud = -73.120741

    # Iterar sobre los documentos y extraer los pares de timeStamp y values
    for documento in documentos:
        timestamp = documento['timeStamp']
        values = documento['values'][dispositivo]
        deviceUUID = documento['deviceUUID']
        lista_time.append(timestamp)
        lista_value.append(values)
        lista_resultados.append({'timeStamp': timestamp, 'values': values, 'deviceUUID':deviceUUID})
        data_mapa.append({'lon': longitud, 'lat': latitud, 'value':values})
        longitud+=0.000110
        latitud+=0.000110
    
    maximoNivel = max(lista_value)

    # Datos de para la gráfica
    data = {
        'timeStamp': lista_time,
        'values': lista_value
    }
    return render_template('sensor.html', topics_values=topics_values, data=data, estacion=estacion, 
                           dispositivo=dispositivo, lista_resultados=lista_resultados, maximoNivel=maximoNivel, data_mapa=data_mapa)

if __name__ == '__main__':
    app.run(debug=True)
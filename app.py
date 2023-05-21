from flask import Flask, render_template, jsonify
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

@app.route('/sensor')
def sensor():
    # Datos de ejemplo para la gráfica
    data = {
        'timeStamp': ['2023-05-01', '2023-05-02', '2023-05-03', '2023-05-04', '2023-05-05'],
        'values': [10, 20, 15, 25, 30]
    }
    return render_template('sensor.html', topics_values=topics_values, data=data)

if __name__ == '__main__':
    app.run(debug=True)
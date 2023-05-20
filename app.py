from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['iot']
collection = db['messages']

@app.route('/')
def index():
    # Realiza la consulta a la base de datos
    pipeline = [
        {"$group": {"_id": "$topic", "values": {"$push": {"$objectToArray": "$values"}}}}
    ]
    result = list(collection.aggregate(pipeline))
    topics_values = [{topic['_id']: [value['k'] for value in topic['values'][0]]} for topic in result]
    return render_template('index.html', topics_values=topics_values)

@app.route('/sensor')
def buttons():
    return render_template('sensor.html')

if __name__ == '__main__':
    app.run(debug=True)
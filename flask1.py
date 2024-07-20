from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from datetime import datetime

app = Flask(__name__)

# Koneksi ke MongoDB menggunakan URI yang diberikan
uri = "mongodb+srv://zarreksagaming12:YSdt*AEkJNZ99$$@cluster0.ijigx2v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client['sensor_database']
sensor_collection = db['sensor1_data']

@app.route('/sensor1', methods=['POST'])
def sensor1():
    # Mengambil data dari request
    data = request.json
    temperature = data.get('temperature')
    kelembapan = data.get('kelembapan')

    if temperature is None or kelembapan is None:
        return jsonify({'error': 'Bad Request', 'message': 'Temperature and Kelembapan are required!'}), 400

    # Membuat data dengan timestamp
    sensor_data = {
        'temperature': temperature,
        'kelembapan': kelembapan
    }

    # Menyimpan data ke MongoDB
    result = sensor_collection.insert_one(sensor_data)

    return jsonify({'message': 'Data inserted successfully!', 'id': str(result.inserted_id)}), 201

if __name__ == '_main_':
    app.run(debug=True)
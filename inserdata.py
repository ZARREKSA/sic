from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://zarreksagaming12:YSdt*AEkJNZ99$$@cluster0.ijigx2v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)

db = client['MyDatabase']
my_collections = db['MyCollection']

person_1 = {'first': 'bat', 'last': 'ara'}
person_2 = {'first': 'ayam', 'last': 'dada'}

results = my_collections.insert_many([person_1, person_2])
print(results.inserted_ids)
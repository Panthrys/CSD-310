from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.dsypl.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print(" -- Pytech COllection List --")
print(db.list_collection_names())
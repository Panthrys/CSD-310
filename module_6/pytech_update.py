from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.dsypl.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})

for doc in docs:
    print(doc)

filter = { 'student_id': 1007}

newvalues = { "$set": { 'first_name': "Geralt of Rivia" } }

db.students.update_one(filter, newvalues)




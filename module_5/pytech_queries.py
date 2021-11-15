#Candice Walls
#November 14, 2021
#CSD 310 - Module 5

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.dsypl.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

docs = db.students.find({})

for doc in docs:
    print(doc)

print(" -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")

doc = db.students.find_one({"student_id": "1007"})
print(doc["student_id"])


doc2 = db.students.find_one({"student_id": "1008"})
print(doc2["student_id"])


doc3 = db.students.find_one({"student_id": "1009"})
print(doc3["student_id"])
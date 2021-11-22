from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.dsypl.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})

for doc in docs:
    print(doc)

Vesemir = {
 	"student_id": 1010, 
 	"first_name":"Vesemir"
}
 
vesemir_student_id = db.students.insert_one(Vesemir).inserted_id
 
print("Inserted student record Geralt into the students collection with document_id" , vesemir_student_id)

remv = {'student_id': 1010}
db.students.delete_one(remv)

#search = db.students.find_one({'student_in': 1010})
#print(search)

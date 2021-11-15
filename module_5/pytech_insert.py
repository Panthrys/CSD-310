#Candice Walls
#November 14, 2021
#CSD 310 - Module 5

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.dsypl.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

print(" -- INSERT STATEMENTS --")

Geralt = {
 	"student_id": 1007, 
 	"first_name":"Geralt"
}
 
geralt_student_id = db.students.insert_one(Geralt).inserted_id
 
print("Inserted student record Geralt into the students collection with document_id" , geralt_student_id)

Lambert = {
 	"student_id": 1008, 
	 "first_name":"Lambert"
}
 
lambert_student_id = db.students.insert_one(Lambert).inserted_id
 
print("Inserted student record Lambert into the students collection with document_id" , lambert_student_id)

Eskel = {
 	"student_id": 1009,
 	 "first_name":"Eskel"
}
 
eskel_student_id = db.students.insert_one(Eskel).inserted_id
 
print("Inserted student record Eskel into the students collection with document_id" , eskel_student_id)


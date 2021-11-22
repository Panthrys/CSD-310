#Candice Walls
#November 14, 2021
#CSD 310 - Module 5

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.dsypl.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech


print(" -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")

x = db.students.find_one()

print(x)
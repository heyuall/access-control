# Python code to illustrate
# inserting data in MongoDB
from pymongo import MongoClient
import datetime

try:
	conn = MongoClient()
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")

# database
db = conn.proget_db

# Created or Switched to collection names: my_gfg_collection
collection = db.historiques
date= datetime.datetime.now()

emp_rec1 = {
		"username":"Houssem",
		"date":str(date)
}

# Insert Data
rec_id1 = collection.insert_one(emp_rec1)


print("Data inserted with record ids",rec_id1)

# Printing the data inserted
cursor = collection.find()
for record in cursor:
	print(record)

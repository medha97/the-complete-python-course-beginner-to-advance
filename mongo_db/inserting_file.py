import pymongo
from pymongo import MongoClient
myclient = MongoClient()
db = myclient.mydb
Users = db.users
users = [{"username": "third","password": "12345"},{"username":"red", "password": "blue"}]
inserted = Users.insert_many(users)
inserted.inserted_ids
Users.find().count()
User.find({"fav_number": 445}).count()

import pymongo
from pymongo import MongoClient
myclient = MongoClient()
db = myclient.mydb
users = db.users
user2 = {"username":"john", "password": "q123123w", "fav_number": 445, "hobbies": ["python", "games", "pizza"]}
user_id = users.insert_one(user2).inserted_id
print(user_id)

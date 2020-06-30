import pymongo
from pymongo import MongoClient
import datetime

myclient = MongoClient()
db = myclient.mydb
Users = db.users

curent_date = datetime.datetime.now()
old_date = datetime.datetime(2009, 8, 12)

old = Users.insert_one({"username": "ffie", "date":curent_date})
print(Users.find({"date": {"$gte": old_date}}).count())
print(Users.find({"date": {"$exists": True}}).count())

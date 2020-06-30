import pymongo
from pymongo import MongoClient
import datetime

myclient = MongoClient()
db = myclient.mydb
Users = db.users

db.users.create_index([("username", pymongo.ASCENDING)])

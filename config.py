import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['r&d']
collection = db['Journal']
collection2 = db['Book']
import re

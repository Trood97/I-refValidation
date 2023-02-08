import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['ICODEX-DB01']
collection = db['Journal1']
collection2 = db['Book1']


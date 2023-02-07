import pymongo
import re
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['ICODEX-DB01']
collection = db['Journal1']
collection2 = db['Book1']
for i in collection.find():
        for j in i['authors']:
            lname = (j.get('lastname'))
            # print(lname)
            l = ['Dr.', 'Prof.']
            for a in l:
                if re.findall(r'\b' + str(a), lname):
                    reason = 'validation failed for preffix "Dr,Prof",'
                    print(reason)
                else:pass



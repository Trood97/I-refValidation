import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['ICODEX-DB01']
collection = db['Journal1']
collection2 = db['Book1']
#
# dict1 = {'authors': [{'lastname': 'GumminJr.', 'firstname': 'DD'}, {'lastname': 'Beuhler', 'firstname': 'MC'}, {'lastname': 'Spyker', 'firstname': 'DA'}, {'lastname': 'Bronstein', 'firstname': 'AC'}, {'lastname': 'Rivers', 'firstname': 'LJ'}, {'lastname': 'van', 'firstname': 'NPT'},{'lastname': 'Rivers', 'firstname': 'LJ'}, {'lastname': 'weber', 'firstname': 'J'}]}
#
#
#
#
# def authorduplicacy():
#
#     for i in dict1.get('authors'):
#         count = 0
#         check1 = str(i.get('lastname')+i.get('firstname'))
#         for j in dict1.get('authors'):
#             check2 = str(j.get('lastname')+ j.get('firstname'))
#             if check1 == check2:
#                 count +=1
#                 print('self checking')
#             else:
#                 pass
#         if count >1:
#             print('validation has failed for author',check1)
#             reason = 'duplicate author found hear'
#             return 1,reason
#
#
# print(authorduplicacy())
#
#
#

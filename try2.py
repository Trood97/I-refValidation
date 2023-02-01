from config import collection
import re




class validation():
    def duplicate(self, collectionname: str):
        if collectionname == 'collection':
            failed_ids_auth = []
            for Name in collection.find({}, {"_id": 1, "authors":
                {"lastname": 1, 'firstname': 1}}):
                a = Name.get('authors')
                # print(a)
                for i in range(0, len(a)):
                    for j in range(i + 1, len(a)):
                        if a[i] == a[j]:
                            print(a[j])
                            failed_ids_auth.append(Name.get('_id'))
            return failed_ids_auth

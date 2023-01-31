from config import collection
import re

failed_ids_title = []
failed_ids_auth = []

class validation():
    def checking(self, collectionnew: str):
        if collectionnew == 'collection':
            for a in collection.find({}, {"_id": 1, 'journalTitle': 1, 'articleTitle': 1,
                                          'authors': {"lastname": 1, "firstname": 1}}):
                lst = ['journalTitle', 'articleTitle', 'firstPage','authors']
                lst2 = ['lastname','firstname']
                ab = a.get('authors')
                for auth in ab:
                    # print(auth)
                    lst2 = ['lastname','firstname']
                    for xy in lst2:
                        auth_string = str(auth.get(xy))
                        if auth_string.startswith(" ") or auth_string.endswith(" "):
                            failed_ids_auth.append(a.get('_id'))

                for item in lst:
                    # print(type(a))
                    stringnew = str(a.get(item))
                    if stringnew.startswith(" ") or stringnew.endswith(" "):
                        failed_ids_auth.append(a.get('_id'))

            return failed_ids_auth









        #
        # if collectionnew == 'collection':
        #     for b in collection.find({},{"_id": 1,'authors': {"lastname": 1, "firstname": 1}}):
        #         ab = b.get('authors')
        #         for auth in ab:
        #             # print(auth)
        #             lst2 = ['lastname','firstname']
        #             for xy in lst2:
        #                 auth_string = str(auth.get(xy))
        #                 if auth_string.startswith(" ") or auth_string.endswith(" "):
        #                     failed_ids_auth.append(b.get('_id'))
        #     return failed_ids_auth

import datetime
from config import collection
import re


class validation():

    def validateyear(self, collectionname: str):
        pass
        today = datetime.date.today()
        year = today.year
        failed_ids = []
        current_year = year
        if collectionname == 'collection':
            for i in collection.find():
                # print(i)
                if int(i.get('year')) <= current_year:
                    print('validation passed')
                else:
                    print('validation failed for page number')
                    failed_ids.append(i.get('_id'))
            return failed_ids

    def validatepagenumberseq(self, collectionname):
        failed_ids_num = []
        if collectionname == 'collection':
            for fp in collection.find():
                try:
                    fp1 = int(fp.get('firstPage'))
                    lp1 = int(fp.get('lastPage'))
                except ValueError as e:
                    print('page number is blank here, ', 'Exception message :', e)
                    pass
                if fp1 <= lp1:
                    print('validation pass')
                else:
                    print('validation failed for page number')
                    failed_ids_num.append(fp.get('_id'))
        return failed_ids_num

    def punctuation(self, collectionname: str):
        if collectionname == 'collection':
            for trail in collection.find():
                ab = str(trail)
                clean = re.sub('\W+\s*', ' ', ab)
                print(clean)

    def suffix(self, collectionname: str):
        suffix_failed_id = []
        if collectionname == 'collection':
            for familyName in collection.find({}, {"_id": 1, "authors": {"lastname": 1}}):
                lname = str(familyName)
                print(lname)
                l = ['Jr', 'Sr', 'ber']
                for i in l:
                    if re.findall(str(i) + r'\b', lname):
                        suffix_failed_id.append(familyName.get('_id'))
                    else:
                        pass
            return suffix_failed_id
    def preffix(self, collectionname: str):
        preffix_failed_id = []
        if collectionname == 'collection':
            for givenName in collection.find({}, {"_id": 1, "authors": {"firstname": 1}}):
                fname = str(givenName)
                # print(fname)
                l = ['Dr.','Prof.']
                for i in l:
                    if re.findall( r'\b'+str(i), fname):
                        preffix_failed_id.append(givenName.get('_id'))
                    else:
                        pass
            return preffix_failed_id

    def trailing_colon_for_all(self, collectionnew: str):
        failed_idspu = []
        if collectionnew == 'collection':
            for j in collection.find():
                lst = ['journalTitle', 'articleTitle', 'bookSeriesTitle', 'bookTitle', 'chapterTitle',
                       'dataTitle', 'otherTitle', 'statuteTitle', 'familyName', 'publisherName', 'publisherLoc']
                for item in lst:
                    stringnew = str(j.get(item))
                    if stringnew.endswith(':'):
                        failed_idspu.append(j.get('_id'))
            return failed_idspu

    def white_space(self, collectionnew: str):
        failed_ids_auth = []
        if collectionnew == 'collection':
            for a in collection.find({}, {"_id": 1, 'journalTitle': 1, 'articleTitle': 1,
                                          'authors': {"lastname": 1, "firstname": 1}}):
                lst = ['journalTitle', 'articleTitle', 'firstPage', 'authors']
                ab = a.get('authors')
                for auth in ab:
                    lst2 = ['lastname', 'firstname']
                    for item1 in lst2:
                        auth_string = str(auth.get(item1))
                        if auth_string.startswith(" ") or auth_string.endswith(" "):
                            failed_ids_auth.append(a.get('_id'))
                            # print(item1,failed_ids_auth)
                #

                for item in lst:
                    stringnew = str(a.get(item))
                    if stringnew.startswith(" ") or stringnew.endswith(" "):
                        failed_ids_auth.append(a.get('_id'))
                        # print(item,failed_ids_auth)

            return (failed_ids_auth)

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


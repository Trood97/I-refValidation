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

    def white_space_leading_or_trailing(self, collectionnew: str):
        white_space_id = []
        if collectionnew == 'collection':
            for j in collection.find():

                lst = ['journalTitle','articleTitle','firstPage','lastname','firstname']
                for item in lst:
                    stringnew = str(j.get(item))
                    if stringnew.startswith(" ") or stringnew.endswith(" "):
                        white_space_id.append(j.get('_id'))
            return white_space_id


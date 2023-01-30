from config import collection
import re

failed_ids = []
failed_idspu = []
failed_idspus = []
failed_idspusf = []
class validation():
    def punctuation_for_all(self, collectionnew: str):
        if collectionnew == 'collection':
            for j in collection.find():
                lst = ['journalTitle','articleTitle','bookSeriesTitle','bookTitle','chapterTitle',
                       'dataTitle','otherTitle','statuteTitle','familyName','publisherName','publisherLoc']
                for item in lst:
                    stringnew = str(j.get(item))
                    if stringnew.endswith(':'):
                        failed_idspu.append(j.get('_id'))
            return failed_idspu







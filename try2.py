from config import collection
import re




class validation():
    def Validation_for_trailing_end_period(self,collectionname: str):  # Backlog 426
        if collectionname == 'collection':
            failed_id = []
            for j in collection.find():
                list = ['articleTitle', 'bookSeriesTitle', 'bookTitle', 'chapterTitle',
                        'keyword', 'publisherName', 'publisherLoc']

                for item in list:
                    stringnew = str(j.get(item))
                    # try:
                    if stringnew.endswith('.'):
                        failed_id.append(j.get('_id'))
                    # except:
            #         if stringnew.endswith('et.'):
            #             failed_id.append(j.get('_id'))
            return failed_id
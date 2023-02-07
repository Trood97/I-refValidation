import re

from config import collection2


def validatebookpunct():  # Exceptions from book----426
    exceptions = {
        "PublisherName": [
            "Acad.", "B.V.", "B. V.", "Co.", "co.", "Corp.", "corp.", "d.o.o.", "et Cie.", "e.V.", "e. V.",
            "Inc.", "Inst.", "K.G.", "KGaA.", "Lab.", "LLC.", "Ltd.", "Ltda.", "N.V.", "o.o.", "O.S.", "Plc.",
            "Pub.", "Publ.", "Pvt.", "S.A.", "S.A.R.L.", "S.A.S.", "Sci.", "S.L.", "Soc.", "S.p.A.", "s.r.l.",
            "S.r.l.", "S.R.L.", "s r. o.", "s. r. o.", "Univ.", "Verl."
        ],
        "PublisherLoc": ["U.K.", "U.S.", "U.S.A."],
        "Keyword": ["L.", "nov.", "s.l.", "sp.", "spp.", "ssp.", "sspp.", "subsp.", "subspp."]}

    for i in (collection2.find({}, dict(_id=1, bookSeriesTitle=1, bookTitle=1, chapterTitle=1, publisherName=1,
                                        pubLocation=1, keyword=1))):

        for no, condition in enumerate(exceptions.get('PublisherName')):  # publishername
            if str(i.get('publisherName')).endswith(str(condition)):
                continue
                # print(no,'validation passed pubname',i.get('_id'))
            else:
                print(no, 'validation failed pubname', )
        #

        for condition2 in exceptions.get('PublisherLoc'):  # publisherloc
            if str(i.get('pubLocation')).endswith(str(condition2)):
                print('validation passed publoc', i.get('_id'))
            else:
                print('validation failed publoc')

        for num, condition3 in enumerate(exceptions.get('Keyword')):  # keyword
            if str(i.get('keyword')).endswith(str(condition3)):
                print(num, 'validation passed keyword')
            else:
                print(num, 'validation failed keyword', i.get('_id'))

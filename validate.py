import datetime
from config import collection,collection2
import re


class validation():

        # year
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

        # page number
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

        # period, comma, quotation, exclamation, semicolon  brackets, braces, parenthesis, dash, hyphen, ellipsis, colon, --
        def punctuation(self, collectionname: str):         #sw

            if collectionname == 'collection':
                for trail in collection.find():
                    ab = str(trail)
                    clean = re.sub('\W+\s*', ' ', ab)
                    print(clean)

        # suffix including Jr.,Sr.
        def suffix(self, collectionname: str):              #sw
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

        # prefix for Dr.,Prof.
        def preffix(self, collectionname: str):             #sw
            preffix_failed_id = []
            if collectionname == 'collection':
                for givenName in collection.find({}, {"_id": 1, "authors": {"firstname": 1}}):
                    fname = str(givenName)
                    # print(fname)
                    l = ['Dr.', 'Prof.']
                    for i in l:
                        if re.findall(r'\b' + str(i), fname):
                            preffix_failed_id.append(givenName.get('_id'))
                        else:
                            pass
                return preffix_failed_id

        # Remove trailing colon for all element.
        def trailing_colon_for_all(self, collectionnew: str):       #ak
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

        # Check whitespace is present or not.
        def white_space(self, collectionnew: str):          #ak
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

                    for item in lst:
                        stringnew = str(a.get(item))
                        if stringnew.startswith(" ") or stringnew.endswith(" "):
                            failed_ids_auth.append(a.get('_id'))
                            # print(item,failed_ids_auth)

                return (failed_ids_auth)

        # check array objects are duplicate or not.
        def duplicate(self, collectionname: str):           #sw
            if collectionname == 'collection':
                failed_ids_auth = []
                for Name in collection.find({}, {"_id": 1, "authors":
                    {"lastname": 1, 'firstname': 1}}):
                    a = Name.get('authors')
                    for i in range(0, len(a)):
                        for j in range(i + 1, len(a)):
                            if a[i] == a[j]:
                                print(a[j])
                                failed_ids_auth.append(Name.get('_id'))
                return failed_ids_auth

            # check elocator in first page

        def validate_pageno_with_e(self, collectionname):          #sb
            if collectionname == 'collection':
                list_eloc = []
                for p in collection.find():
                    a = str(p.get('firstPage'))
                    b = str(p.get('lastPage'))

                    z = "[a-z]"

                    if re.findall(str(z) + r"\B", a) or re.findall(str(z) + r"\B", b):  # check for first & last page..
                        list_eloc.append(p.get('_id'))

                return list_eloc

        # family name should not be null
        def familyName_mandatory(self, collectionname: str):        #sb
            if collectionname == 'collection':
                failed_id = []
                for j in collection.find({}, {"_id": 1, 'authors': {"lastname": 1, "firstname": 1}}):
                    s = j.get('authors')
                    for ab in s:
                        lst2 = ['lastname']
                        for item1 in lst2:
                            auth_string = str(ab.get(item1))
                            if auth_string == '':
                                failed_id.append(j.get('_id'))
                return failed_id

        # Validation for "givenNames" ends with 'prefix'
        def givennameprefix(self, collectionnew: str):  # ak
            failed_idspusdd = []
            if collectionnew == 'collection':
                for a in collection.find({}, {"_id": 1, 'authors': {"firstname": 1}}):
                    lst = {'firstname'}
                    ab = a.get('authors')
                    for auth in ab:
                        lsts = ['firstname']
                        for item in lsts:
                            stringnew = str(auth.get(item))
                            prefix = ['van', 'von', 'v.', 'der', 'de', 'del']
                            for i in prefix:
                                if stringnew.endswith(i):
                                    failed_idspusdd.append(a.get('_id'))

                    for item2 in lst:
                        stringnew = str(a.get(item2))
                        if stringnew.endswith("van"):
                            failed_idspusdd.append(a.get('_id'))
                return failed_idspusdd

        # Validation for trailing period in familyname
        def familytrailing(self, collectionnew: str):  # ak
            failed_idspusdd = []
            if collectionnew == 'collection':
                for a in collection.find({}, {"_id": 1, 'authors': {"firstname": 1}}):
                    lst = {'firstname'}
                    ab = a.get('authors')
                    for auth in ab:
                        for item in lst:
                            stringnew = str(auth.get(item))
                            prefix = ['.']
                            for i in prefix:
                                if stringnew.endswith(i):
                                    failed_idspusdd.append(a.get('_id'))

                    for item2 in lst:
                        stringnew = str(a.get(item2))
                        if stringnew.endswith("."):
                            failed_idspusdd.append(a.get('_id'))
                return failed_idspusdd

        # Validation for trailing period in all
        def Validation_for_trailing_end_period(self, collectionname: str):  # Backlog 426
            if collectionname == 'collection':
                failed_id = []
                for j in collection.find({}):  # if it is a journal
                    list = ['articleTitle']
                    for item in list:
                        stringnew = str(j.get(item))
                        if stringnew.endswith('.'):
                            failed_id.append(j.get('_id'))

                for k in collection2.find():  # if it is book
                    list1 = ['bookSeriesTitle', 'bookTitle', 'chapterTitle', 'keyword', 'publisherName', 'publisherLoc']
                    for item in list1:
                        string1 = str(k.get(item))
                        if string1.endswith('.'):
                            failed_id.append(k.get('_id'))
                return failed_id





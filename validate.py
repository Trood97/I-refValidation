import datetime
import re


class validation():

    # Validation for Publication year
    def validateyear(self, i: dict):  #388
        pass
        today = datetime.date.today()
        year = today.year
        current_year = year
        a = int(i.get('year'))
        if a <= current_year:
            pass
        else:
            reason = f'Reason: year greater than the current year, Error:{a}'
            return 1, reason

    # Validation for page numbers
    def validatepagenumberseq(self, i: dict):  # -387
        fp1 = int(i.get('firstPage'))
        lp1 = int(i.get('lastPage'))
        if fp1 <= lp1:
            pass
        else:
            reason = 'Reason:validation failed for page number'
            return 1, reason

    # Validation for familyName contains suffix
    def suffix(self, i: dict):  # sw -430
        for familyName in i['authors']:
            lname = str(familyName.get('lastname'))
            # print(lname)
            l = ['Jr', 'Sr', 'ber']
            for i in l:
                if lname.endswith(i):
                    reason = f'validation failed for suffix jr,sr, Error:{lname}'
                    return 1, reason
                else:
                    pass

    # Validation for "givenNames" contains honorifics info like Dr,Prof
    def preffix(self, i: dict):  # -429
        for givenName in i['authors']:
            fname = str(givenName.get('firstname'))
            # print(fname)
            l = ['Dr.', 'Prof.']
            for a in l:
                if re.findall(r'\b' + str(a), fname):
                    reason = f'validation failed for preffix "Dr,Prof", Error:{fname}'
                    return 1, reason
                else:
                    pass

    # Validation for trailing punctuation colon
    def trailing_colon_for_all(self, i: dict):  # -431
        for item in i:
            stringnew = str(i.get(item))
            if stringnew.endswith(':'):
                reason = f'failed for colon, Error:{stringnew}'
                return 1, reason
            else:
                pass

    # Validation for whitespaces
    def white_space(self, i: dict):  # ak-656
        for item in i:
            stringnew = str(i.get(item))
            if stringnew.startswith(" ") or stringnew.endswith(" "):
                reason = f'validation failed for white space, Error:{stringnew}'
                return 1, reason

        for auth in i['authors']:
            # print(auth)
            lst2 = ['lastname', 'firstname']
            for item1 in lst2:
                auth_string = str(auth.get(item1))
                if auth_string.startswith(" ") or auth_string.endswith(" "):
                    reason = f'white sapce validation failed for fname and lname, Error:{auth_string}'
                    return 1, reason
                else:
                    pass

    # Validation for "familyName" and "givenNames" in author and editor
    def duplicate(self, i: dict):  #-427
        for x in i.get('authors'):
            count = 0
            check1 = str(x.get('lastname') + x.get('firstname'))
            for j in i.get('authors'):
                check2 = str(j.get('lastname') + j.get('firstname'))
                if check1 == check2:
                    count += 1
                    # print('self checking')
                else:
                    pass
            if count > 1:
                # print('validation has failed for author', check1)
                reason = f'duplicate author found hear, Error:{check1}'
                return 1, reason

        #Validation for page numbers with "e"
    def validate_pageno_with_e(self, i: dict):  #  skip --415
        a = str(i.get('firstPage'))
        b = str(i.get('lastPage'))
        z = "[a-z]"
        if re.findall(str(z) + r"\B", a) or re.findall(str(z) + r"\B", b):  # check for first & last page..
            reason = f'validation failed for page number with e, Error:{a or b}'
            return 1, reason
        else:
            pass

    # Validation for Author name in references, familyname is mandatory
    def familyName_mandatory(self, i: dict):  # -390
        for familyName in i['authors']:
            lname = str(familyName.get('lastname'))
            if lname == '':
                reason = f'lastname empty, Error:{lname}'
                return 1, reason
            else:
                pass

    # Validation for "givenNames" ends with 'prefix'
    def givennameprefix(self, i: dict):  # --428
        for familyName in i['authors']:
            lname = str(familyName.get('lastname'))
            prefix = ['van', 'von', 'v.', 'der', 'de', 'del']
            for i in prefix:
                if lname.endswith(i):
                    reason = f'validation failed for givenname, Error:{lname}'
                    return 1, reason
                else:
                    pass

    # Validation for trailing period in familyname
    def familytrailing(self, i: dict):  #  -741
        for familyName in i['authors']:
            fname = str(familyName.get('firstname'))
            # print(fname)
            prefix = ['.']
            for i in prefix:
                if fname.endswith(i):
                    reason = f'validation failed for familyname trailing, Error:{fname}'
                    return 1, reason
                else:
                    pass

    # Validation for trailing period in all
    def Validation_for_trailing_end_period(self, i: dict):  # -426

        # # if it is a journal
        # list = ['articleTitle']
        # for item in list:
        #
        #     stringnew = str(i.get(item))
        #     if stringnew.endswith('.'):
        #         reason = 'validation failed for articleTitle'
        #         return 1, reason
        #     else:pass
        # for k in collection2.find():  # if it is book
        list1 = ['articleTitle', 'bookSeriesTitle', 'bookTitle', 'chapterTitle', 'keyword', 'publisherName',
                 'publisherLoc']
        for item in list1:
            string1 = str(i.get(item))
            if string1.endswith('.'):
                reason = (f'validation failed for Titles, Error:{string1}')
                return 1, reason
            else:
                pass

from validate import validation
from validate2 import validatebookpunct
from config import *

a = validation()
validationerror = []

def runfullvalidationforjournal(i: dict):
    def1 = (a.validateyear(i))

    if def1 is not None and 1 in def1:
        (validationerror.append(str(def1[1])))
    else:
        pass
    # ---------
    def2 = (a.validatepagenumberseq(i))
    if def2 is not None and 1 in def2:  # ok
        (validationerror.append(str(def2[1])))
    else:
        pass
    # ---------
    def4 = (a.suffix(i))
    if def4 is not None and 1 in def4:
        (validationerror.append(str(def4[1])))
    else:
        pass
    # ---------

    def5 = (a.preffix(i))
    if def5 is not None and 1 in def5:
        (validationerror.append(str(def5[1])))
    else:pass
    # ----------
    def6 = (a.trailing_colon_for_all(i))
    if def6 is not None and 1 in def6:
        (validationerror.append(str(def6[1])))
    else:
        pass
    # -----------
    def7 = (a.white_space(i))
    if def7 is not None and 1 in def7:
        (validationerror.append(str(def7[1])))
    else:
        pass
    # -----------

    def8 = (a.duplicate(i))
    if def8 is not None and 1 in def8:
        (validationerror.append(str(def8[1])))
    else:
        pass
    # -----------

    # def9 = (a.validate_pageno_with_e(i))
    # if def9 is not None and 1 in def9:
    #     print(validationerror.append(def9[1]))
    # else:
    #     pass

    # ------------
    def10 = (a.familyName_mandatory(i))
    if def10 is not None and 1 in def10:
        (validationerror.append(def10[1]))
    else:
        pass
    # ------------
    def11 = (a.givennameprefix(i))
    if def11 is not None and 1 in def11:
        (validationerror.append(def11[1]))
    else:
        pass
    # -------------
    def12 = (a.familytrailing(i))
    if def12 is not None and 1 in def12:
        (validationerror.append(def12[1]))
    else:
        pass
    # -------------
    def13 = (a.Validation_for_trailing_end_period(i))
    if def13 is not None and 1 in def13:
        (validationerror.append(def13[1]))
    else:
        pass

    # -------------

class validate():
    def __init__(self):  # constructor
        print('code for full validation!!!')

    def journalvalidate(self):
        for i in collection.find():
            runfullvalidationforjournal(dict(i))
            if len(validationerror) >0:
                filter = {'_id': i.get('_id')}
                newvalues = {'$set': {'ValidationError': validationerror}}
                collection.update_one(filter, newvalues)
                print(filter.get('_id'),validationerror)
            else:
                pass # print('full validation passed for id:',i.get('_id'))
            del validationerror[:]

    def bookvalidate(self):
        for i in collection2.find():
            pass

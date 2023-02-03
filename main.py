from validate import validation
from validate2 import validatebookpunct
from config import collection,collection2

# from try2 import validation

for i in collection.find():
    print(i)

a = validation()

print(a.validateyear('collection'))

# print(a.validatepagenumberseq('collection'))

# print(a.punctuation('collection'))

# print(a.suffix('collection'))

# print(a.preffix('collection'))

# print(a.trailing_colon_for_all('collection'))

# print(a.white_space('collection'))

# print(a.duplicate('collection'))

# print(a.validate_pageno_with_e('collection'))

# print(a.familyName_mandatory('collection'))

# print(a.givennameprefix('collection'))

# print(a.familytrailing('collection'))

# print(a.Validation_for_trailing_end_period('collection'))

# validatebookpunct()









#
# # doi search---*
# def func():
#     search = collection.find({'url': input('enter doi')})
#     for i in search:
#         return i
# print(func())
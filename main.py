from validate import validation
# from try2 import validation
from config import collection

a = validation()

# print(a.validateyear('collection'))


# print(a.validatepagenumberseq('collection'))

# print(a.punctuation('collection'))

# print(a.suffix('collection'))

print(a.punctuation_for_all('collection'))


#
# # doi search---*
# def func():
#     search = collection.find({'url': input('enter url')})
#     for i in search:
#         return i
#
#
# print(func())
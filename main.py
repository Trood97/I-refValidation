from validate import validation
# from try2 import validation
from config import collection

a = validation()

# print(a.validateyear('collection'))

# print(a.validatepagenumberseq('collection'))

# print(a.punctuation('collection'))

# print(a.suffix('collection'))

# print(a.preffix('collection'))

# print(a.trailing_colon_for_all('collection'))

# print(a.white_space('collection'))

print(a.duplicate('collection'))








#
# # doi search---*
# def func():
#     search = collection.find({'url': input('enter doi')})
#     for i in search:
#         return i
# print(func())
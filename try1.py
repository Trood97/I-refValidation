import string
from string import *

s = ".$ABC-799-99,_.$^^&*(#;"
#
print(s.strip(punctuation))
print(s.rstrip(punctuation))  # rstrip any trailing punctuation
print(s.lstrip(punctuation))  # lstrip remove leading punctuations

import string

test_str = 'Gfg, is -best: for ! Geeks ;'

test_str = test_str.translate(str.maketrans('', '', string.punctuation))

s = s.translate(str.maketrans('', '', string.punctuation))
print(s)
print(test_str + '\n' + '------------------')
# -----------

import re

tweet = 'I am tired! I :like-$ fruit...and milk'
clean = re.sub('\W+\s*', ' ', tweet)
print(clean + '\n' + '-----------------')

fpage = 123
lpage = 130
if fpage < lpage:
    print('validation passed')

abc = '1'
xyz = '12'
print(len(abc))
print(len(xyz))

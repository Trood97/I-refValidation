import re

str = ('Python is a ','programming',' language')
#search using regex
x = re.search('language$', str)

if(x!=None):
	print('The line ends with \'language\'.')
else:
	print('The line does not end with \'language\'.')
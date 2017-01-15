#!/usr/bin/python3

import re # regex

phoneNumRegex = re.compile(r'(\d\d\d)?-?(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is 385-721-8734')
print('Phone number found: %s' % mo.group()) # mo.group() and mo.group(0) return entire object, not specific groups
print('The area code is: %s' % mo.group(1))
print('The area-specific number is: %s' % mo.group(2))

# Alternatively, use mo.groups() method <-- note plural form of 'groups'

mo.groups() # will return tuple of (group1, group2)
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

print('Findall to follow')
find = phoneNumRegex.findall('Cell: 604-555-9999 Work: 212-456-7892')
print(find)
print(find[0])
if not find[0][0]:
	print('doesn\'t exist')
else: 
	print(find[0][0])
	
print('NEXT: using findall to list all numbers found in string')

find2 = phoneNumRegex.findall('My phone number is 778-348-9887. My house number is 788-384-7645. My work number is 192-754-2389. 778-8656')
numFound = len(find2)

print('We found %s numbers in your string!' % numFound)
print('The numbers listed are as follows:')
for i in range(numFound):
	if not find2[i][0]:
		print(find2[i][1])		
	else:	
		print('-'.join(find2[i]))
		
		

#!/usr/bin/python3

# Import regex and logging
import re, logging

# Configure logging
logging.basicConfig(filename='logs/example.log', level=logging.DEBUG)

# Compile regex expression
ex = re.compile(r'\d+\s\w+')
logging.debug('Expression compiled')

# Find all in string that match expression, will return list
find = ex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

# Get number of matches found
numFound = len(find)

# Print number of strings found, then list them
print('We found %s strings that match your expression!' % numFound)
print('The strings are as follows:')

for i in find:
	print(i)
		
logging.debug('Done')

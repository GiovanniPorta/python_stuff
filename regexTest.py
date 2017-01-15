#!/usr/bin/python3

import re

#ex = re.compile(r'^([tT][oO][pP]|[mM][iI][dD]|[lL][oO][wW])-([lL]|[mM]|[rR])$')
ex = re.compile(r'^(top|mid|low)-(l|m|r)$', re.IGNORECASE)

userInput = input()

val = ex.search(userInput)

if not val:
	print('No match')
else:
	print(val)

#!/usr/bin/python3

# Handling exceptions and printing error

import sys

try: # try this code
	print(1 + 'hi')

except TypeError as detail: # if code fails as TypeError
	print('TypeError:', detail) # prints error followed by specifics

except: # if code fails as any other error
	print('Unexpected error:', sys.exc_info()[1]) # prints error info to screen
	
print('This code will execute after the error has been handled')
input()
	
	

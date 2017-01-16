#!/usr/bin/python3

# Substitution using regular expressions

import re

namesRegex = re.compile(r'[Aa]gent (\w)\w*')
print('Enter a sentence with names that are prefixed with \'Agent\'')

iText = input()

censoredText = namesRegex.sub(r'Agent \1****', iText)
print(censoredText)

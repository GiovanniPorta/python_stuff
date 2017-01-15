#!/usr/bin/python3

# Bullet point adder
# Adds markdown bullet points to start of each line of text in clipboard

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
	# loop through all indexes in the 'lines' list
	lines[i] = '* ' + lines[i] # add star to each string in list

# Join lines back together into one string
text = '\n'.join(lines)

pyperclip.copy(text)
print('Bullet points have been added to the lines in your clipboard')


#!/usr/bin/python3

# Password manager
# This program will store passwords for each account name
# Running account name as argument will put its password into clipboard
# Insecure! There is no file encryption involved

import sys, pyperclip

passwords = {'email': 'emailpasswordhere',
			 'blog': 'blogpasswordhere',
			 'luggage': '12345'}

if len(sys.argv) < 2:
	print('Usage: python3 pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1]  # first cmd line argument is account name

if account in passwords:
	pyperclip.copy(passwords[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)



#!/usr/bin/python3

import os

print(os.getcwd())
#print(os.listdir('.'))
print('Is test a file:', os.path.isfile('test')) # returns False, does not exist at all
print('Is logs a folder:', os.path.isdir('logs')) # returns True, does exist as folder

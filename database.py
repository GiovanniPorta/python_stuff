#!/usr/bin/python3

# SQLite

import sqlite3, sys

#def db_open():   # TODO: create class and functions for interacting with database
#	conn = sqlite3.connect('enterprise.db')
#	curs = conn.cursor()
#
def db_commit():
	conn.commit()

def db_close():
	curs.close()
	conn.close()
	
def db_get():
	for row in curs.execute('SELECT critter, count FROM zoo ORDER BY critter'):
		print(row)
	#print(curs.fetchall())

def db_add(cr, co=None, da=None):
	if not co:
		co = 1
	if not da:
		da = 0.0
	print('Adding:', cr, str(co), str(da))
	curs.execute('INSERT INTO zoo VALUES(?, ?, ?)', (cr, co, da))

def db_delete(cr):
	print('Deleting:', cr)
	curs.execute('DELETE FROM zoo WHERE critter=(?)', (cr,))


# Table: zoo
# critter (varchar20) # count (int) # damages (float) #

conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()

while True:
	cmd = input("Input: ")	
	
	if cmd == 'get':
		db_get()
	elif cmd == 'add':
		inputCritter = input('Enter critter name: ')
		inputCount = input('Enter count: ')
		inputDamages = input('Enter damages cost: ')
		db_add(inputCritter, inputCount, inputDamages)
		db_commit()
	elif cmd == 'commit':
		db_commit()
	elif cmd == 'delete':
		inputDelete = input('Enter critter name: ')
		db_delete(inputDelete)
	elif cmd == 'quit' or cmd == 'exit':
		db_close()
		sys.exit()
	else:
		print('Unknown command')



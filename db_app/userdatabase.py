#!/usr/bin/python3

# User database application with hashed/salted passwords (using passlib)
# Allows you to create, delete, and list users in database
# After creating a user, you can verify their password by checking it against the hash

# Ensure you run the init.py beforehand to initialize the database
# There is limited error handling, program will likely crash when running into one

# Import libraries
from passlib.apps import custom_app_context as pwd
import sqlite3, sys

# Table name: users
# id | name | pass

# Commit changes to database
def db_commit():
	conn.commit()

# Close database connection
def db_close():
	curs.close()
	conn.close()

# Add new user to database
def user_add(name, pw):
	pw_hash = pwd.hash(pw)
	curs.execute('INSERT INTO users (name, pass) VALUES(?, ?)', (name, pw_hash))
	print('Added user:', name)

# Delete user from database
def user_delete(name):
	curs.execute('DELETE FROM users WHERE name=(?)', (name,))
	print('Deleted user:', name)
	
# List users in database along with their corresponding unique ID
def user_list():
	print('List of users:')
	for row in curs.execute('SELECT id, name FROM users ORDER BY id'):
		print(row)

# Verify given password against password hash for user in database
def pass_verify(name, pw):
	curs.execute('SELECT pass FROM users WHERE name=(?)', (name,))
	try:
		pw_hash = curs.fetchone()[0]
		print('Fetched hash:', pw_hash)
		if pwd.verify(pw, pw_hash) == True:
			print('The password matches the hash')
		else:
			print('The password does not match the hash')
	except TypeError:
		print('User does not exist')

# Function definitions end here, code starts

# Connects to database
conn = sqlite3.connect('users.db')
curs = conn.cursor()

# Prints usable commands
print('Available commands: list, add, delete, verify, commit, quit')

# Constant loop
while True:
	cmd = input("Input: ") # prompt for command and match against following if statements
	
	if cmd == 'list': # list users
		user_list()
	elif cmd == 'add': # add new user
		inputName = input('Enter user name: ')
		inputPass = input('Enter pass: ')
		user_add(inputName, inputPass)
		db_commit()
	elif cmd == 'del' or cmd == 'delete': # delete user
		inputName = input('Enter user name: ')
		user_delete(inputName)
		db_commit()
	elif cmd == 'verify': # verify user password against hash in database
		inputName = input('Enter user name: ')
		inputPass = input('Enter pass: ')
		pass_verify(inputName, inputPass)
	elif cmd == 'commit': # commit changes (not really used since add/del automatically commit by themselves)
		db_commit()
	elif cmd == 'quit' or cmd == 'exit': # quit program: closes db connections and calls exit function
		db_close()
		sys.exit()
	else: # command not known
		print('Unknown command')



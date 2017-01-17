#!/usr/bin/python3
# Initialize database

import sqlite3

print('Enter database name for init:')
db = input()
conn = sqlite3.connect(db)
curs = conn.cursor()
print('Connected')
curs.execute('CREATE TABLE users(id INTEGER PRIMARY KEY, name VARCHAR(255) NOT NULL, pass VARCHAR(255) NOT NULL)')
print('Table created')
conn.commit()
print('Changes committed')
curs.close()
conn.close()
print('Connection closed. Initialization has been completed - goodbye')

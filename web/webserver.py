#!/usr/bin/python3

# Simple web server using bottle.py

from bottle import route, run, static_file

@route('/')
def home():
	#return "It isn't fancy, but it's my home page"
	return static_file('index.html', root='./static/')
	
@route('/echo/<thing>')
def echo(thing):
	return "Say hello to my little friend: %s!" % thing
	
run(host='localhost', port=80)

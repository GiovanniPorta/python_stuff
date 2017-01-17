#!/usr/bin/python3

# Web server using Flask

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	return app.send_static_file('index.html')

#@app.route('/echo/<thing>/<place>')
#def echo(thing, place):
#	return render_template('flask2.html', thing=thing, place=place) # pass thing variable to template, with string thing

@app.route('/echo/') # using GET parameters
def echo():
	thing = request.args.get('thing')
	place = request.args.get('place')
	return render_template('flask2.html', thing=thing, place=place) # template=variable
	
@app.route('/echo2/') #
def echo2():
	kwargs = {}
	kwargs['thing'] = request.args.get('thing')
	kwargs['place'] = request.args.get('place')
	return render_template('flask2.html', **kwargs)

@app.route('/table/')
def table():
	myTable = {'Name':'Giovanni','GUID':'929496c7f3a7e42299180d024ec5b55b'}
	myTable2 = {'Name':'Comrade','GUID':'8687e9dc36698ee386fb40fd1d7e4329'}
	return render_template('flask-table.html', myTable=myTable, myTable2=myTable2)

@app.route('/database/')
def show_db():
	# TODO: pass database to template and print in table, example code from userdatabase.py below:
	for row in curs.execute('SELECT id, name FROM users ORDER BY id'):
		print(row)


app.run(port=80, debug=True)

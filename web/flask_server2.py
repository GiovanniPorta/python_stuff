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


app.run(port=80, debug=True)

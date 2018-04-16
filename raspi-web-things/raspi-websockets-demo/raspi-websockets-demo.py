#!/usr/bin/env python
# Main program that serves an HTTP server provided by the Bottle microframework. 

from bottle import route, run, template, SimpleTemplate, post, static_file, error, request

@route('/static/<path:path>')
def static(path):
	return static_file(path, root='static')

@error(404)
def not_found(error):
	return template('notfound')

@route('/')
def index():
	return template("index")

run(host='0.0.0.0', port=8080, reloader=True)

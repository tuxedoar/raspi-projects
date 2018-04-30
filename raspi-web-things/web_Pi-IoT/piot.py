#!/usr/bin/env python

from bottle import route, run, template, SimpleTemplate, post, static_file, error, request
import led_handler
#import sensor_handler

led = led_handler.state()

@route('/static/<path:path>')
def static(path):
	return static_file(path, root='static')

@error(404)
def not_found(error):
	return template('notfound')

@route('/')
def index():
	return template("index")


@route('/sensor')
def sensor():
	return template("sensor")


@route('/led/<pin>/<state>', method='POST')
def led_manager(pin, state=None):
	if state == "on":
		led.control(pin,1)

	elif state == "off":
		led.control(pin,0)
	else:
		return not_found(error)

run(host='0.0.0.0', port=8080, reloader=True)

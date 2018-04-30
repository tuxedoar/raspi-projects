#!/usr/bin/env python

import RPi.GPIO as GPIO

pins = (17, 18, 27)

class state():
	
	def __init__(self):
		# Setup GPIO pins.
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		for pin in pins:
			GPIO.setup(pin, GPIO.OUT)

	def reset_pins(self):
        	for pin in pins:
                	GPIO.setup(pin, GPIO.OUT)
        	GPIO.cleanup()

	def control(self, pin, valor):
		if pin == '17':
			GPIO.output(17, valor)
		elif pin == '18':
			GPIO.output(18, valor)
		elif pin == '27':
			GPIO.output(27, valor)
	

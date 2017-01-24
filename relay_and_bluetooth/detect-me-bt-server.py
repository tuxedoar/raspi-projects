#!/usr/bin/env python
'''
Este script hace de servidor y se ejecuta en la RasPi, esperando que un cliente se conecte y le diga si apagar o encender una lámpara,por medio de un relé.

This script runs in a RasPi and acts as a socket server, waiting until a client gets connected and is instructed whether a lamp controlled by a relay switch, should be turned on or off.   
'''  
import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
        s = socket.socket()
        s.bind(("0.0.0.0", 5000))
        s.listen(5)

        print "Esperando conexion del cliente..."

        conn, addr = s.accept()

        if addr:
                print "Conexion de %s" % addr[0]

        while True:
                data = conn.recv(1024)
                if data == "on":
                        GPIO.output(17, 1)
                elif data == "off":
                        GPIO.output(17, 0)
                else:
                        print  "Error en la conexion con el cliente"
                        break
        conn.close()
        s.close()

except KeyboardInterrupt:
        print "Ejecucion interrumpida!."
finally:
        GPIO.cleanup()          

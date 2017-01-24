#!/usr/bin/env python
'''
Este script actúa como cliente, conectándose a un socket servidor para indicarle si debe o no encender una lámpara por medio de un relé, de acuerdo a si detecta la presencia de un determinado dispositivo bluetooth predefinido.

This script acts as a client, connecting to a socket server whenever detects the presence or absence of a certain (predefined) bluetooth device, and so it gives the instruction to the server to turn a lamp on or off, according to that kind of event.   
'''
import socket
from time import sleep

import bluetooth

try:

        s = socket.socket()
        s.connect(("192.168.0.19", 5000))

        print "Conexion establecida..."

        while True:
                result = bluetooth.lookup_name('1C:66:AA:47:70:D3', timeout=5)
                if (result != None):
                        print "Usuario detectado!"
                        s.send('on')
                else:
                        print "Usuario ausente!"
                        s.send('off')

                sleep(3)

        s.close()

except bluetooth.btcommon.BluetoothError:
        print "Error al utilizar el dispositivo Bluetooth!"
except KeyboardInterrupt:
        print "Ejecucion interrumpida"
except socket.error:
        print "Error al establecer la conexion con el servidor"

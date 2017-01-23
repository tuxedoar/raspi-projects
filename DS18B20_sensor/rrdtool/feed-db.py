#!/usr/bin/env python 
# It feeds the rrdtool db with the temperature values taken from the sensor. 
import re
import rrdtool 

dsaddr="/sys/bus/w1/devices/28-0215821986ff/w1_slave"
file = open(dsaddr, 'r')

try:
        for linea in file.readlines():
                estado = re.match("YES", "YES")
                if estado:
#                               print "Sensor encontrado..."
                        temp = re.findall('[t]\=\d+', linea)
                        if temp:
                                temp = temp[0].split('=')
                                temp = int(float(temp[1])) / 1000.00
                                rrdtool.update('/path/to/temperatures.rrd', 'N:%.2f' % (temp))
                        file.close()
except:
        file.close()
          

#!/usr/bin/env python 
# Lee el sensor y guarda los datos en un archivo CSV. Usar con una tarea programada en "cron".
# It reads the temperature values from the sensor and stores them in a CSV file. Aimed to be used with a 'cron' job.  
import re
import os
import csv
from time import sleep
from datetime import datetime

dsaddr="/sys/bus/w1/devices/28-0215821986ff/w1_slave"
filepath="/path/to/temp-file-records.csv"
tempcsv=open(filepath, 'a')

writer = csv.writer(tempcsv)
file = open(dsaddr, 'r')

if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        pass
else:
        writer.writerow( ('Hora', 'Temperatura') )

try:
        for linea in file.readlines():
                estado = re.match("YES", "YES")
                if estado:
#                               print "Sensor encontrado..."
                        temp = re.findall('[t]\=\d+', linea)
                        hora = datetime.now().strftime('%H:%M:%S')
                        if temp:
                                temp = temp[0].split('=')
                                temp = int(float(temp[1])) / 1000.00
                                writer.writerow(( '{}'.format(hora),'{:05.2f}'.format(temp) ))
finally:
        file.close()

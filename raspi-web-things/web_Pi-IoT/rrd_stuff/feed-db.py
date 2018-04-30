#!/usr/bin/env python 
# It feeds the rrdtool db with the temperature values taken from the sensor. 
import re
import rrdtool 

dsaddr="/sys/bus/w1/devices/28-0215821986ff/w1_slave"

try:
  with open(dsaddr, 'r') as file:
    for line in file.readlines():
      state = re.match("YES", "YES")
      if state:
        temp = re.findall('[t]\=\d+', line)
        if temp:
          temp = temp[0].split('=')
          temp = int(float(temp[1])) / 1000.00
          rrdtool.update('/path/to/rrd_stuff/temperatures.rrd', 'N:%.2f' % (temp))
except Exception as e:
  print "An error ocurred: %s " % (e)

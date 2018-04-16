#!/usr/bin/env python

import sensor_handler
from time import sleep

sensor = sensor_handler.ds_sensor() 

while True:
  temp = sensor.get_temp()
  print temp
  sleep(2)

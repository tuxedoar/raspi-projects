#!/bin/bash
# It creates an rddtool db in which temp values are gonna be updated every 5 minutes.
# Actualizo cada 5 minutos!.
rrdtool create --step 300 temperatures.rrd DS:temp:GAUGE:600:0:50 RRA:MAX:0.5:1:288

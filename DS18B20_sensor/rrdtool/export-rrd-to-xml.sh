#!/usr/bin/env bash 
# Exports the rrdtool db to an XML file. 
rrdtool xport -s now-24h -e now --step 300 \
DEF:temp=temperatura.rrd:temp:MAX \
XPORT:temp:"DS18B20" > temperaturas.xml

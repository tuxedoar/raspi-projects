#!/bin/bash
# It creates a native rrdtool graph according to the temperature values stored in the rrdtool db. 
rrdtool graph temperatura.png --title="Sensor DS18B20" \
-w 785 -h 120 -a PNG --vertical-label "Temperatura C" \
--start -86400 --end now \
--slope-mode \
DEF:temp=temperatura.rrd:temp:MAX \
LINE1:temp#ff0000:"Grados Celcius"

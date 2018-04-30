#!/usr/bin/env bash
# Exports the rrdtool db to an XML file.

TARGET_DIR="/path/to/rrd_stuff/"

cd $TARGET_DIR &&
rrdtool xport -s now-24h -e now --step 300 \
DEF:temp=temperatures.rrd:temp:MAX \
XPORT:temp:"DS18B20" > $TARGET_DIR/temperatures.xml

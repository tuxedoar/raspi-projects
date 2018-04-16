
# This script runs a basic websocket server. It uses the websockets 
# Python library and is based on an example taken from its webpage. See: 
#
# https://websockets.readthedocs.io/en/stable/intro.html
#
# Note that this particular piece of code, was adapted to run with Python 3.4!. 

import asyncio
import websockets
import sensor_handler
from time import sleep

sensor = sensor_handler.ds_sensor() 

@asyncio.coroutine
def random_numbers(websocket, path):
   while True:
     temp = (sensor.get_temp())
     # temp = str(temp)
     yield from websocket.send(temp)
     yield from asyncio.sleep(2)

start_server = websockets.serve(random_numbers, '0.0.0.0', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

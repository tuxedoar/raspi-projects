
import sys
import re
import threading
from time import sleep

class ds_sensor():
  """ It reads the 1-wire DS18B20 temperature sensor """

  def __init__(self):
    """ Initialize the temperature sensor """
    self._dsaddr="/sys/bus/w1/devices/28-0215821986ff/w1_slave"
    self._temp = None
    # Create a lock to syncronize access to hardware from multiple threads.
    self._lock = threading.Lock()
    self._dssensor_thread = threading.Thread(target=self.read_sensor)
    # Start the thread in daemon mode!.
    self._dssensor_thread.daemon = True
    self._dssensor_thread.start()

  def read_sensor(self):
    """ Read the temperature from the DS sensor. """
    file = self._dsaddr
    while True:
      with self._lock:
        with open(file, 'r') as f:
            for linea in f.readlines():
              estado = re.match("YES", "YES")
              if estado:
                self._temp = re.findall('[t]\=\d+', linea)
                if self._temp:
                  self._temp = self._temp[0].split('=')
                  self._temp = int(float(self._temp[1])) / 1000.00
                  self._temp = "{:.1f}".format(self._temp)
              else:
                print("Sorry, can't read the sensor!")
      sleep(2) 

  def get_temp(self):
    """ Get the temperature value (Celsius) from the sensor. """
    with self._lock:
      return self._temp

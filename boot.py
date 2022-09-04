import network
import sys, time, deneyap
from machine import Pin

import esp
esp.osdebug(None)

import gc
gc.collect()



ssid = 'enter your ssid'
password = 'enter your password'

exit_btn = Pin(deneyap.GPKEY, Pin.IN)
print("\n\nHold button to exit..\n")
time.sleep(3)
if not exit_btn.value():
    print("Connection Aborted!\n")
    sys.exit(1)

print("\nConnecting..\n")
station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('\nConnection successful.\n')
print(station.ifconfig())
print('\n')
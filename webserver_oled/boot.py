import network
import sys, time, deneyap
from machine import Pin

import esp
esp.osdebug(None)

import gc
gc.collect()


try:
    from machine import I2C
    import ssd1306
    i2c = I2C(-1, scl=Pin(deneyap.SCL), sda=Pin(deneyap.SDA))
    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    oled_status = True
except:
    oled_status = False

def oprint(s,y,x=0,c=1,startfill=False,endfill=False):
    if oled_status:
        if startfill:
            oled.fill(0)
        oled.text(s,x,y,c)
        if endfill:
            oled.fill(0)
        oled.show()
    else:
        pass


#ssid = 'iphone-suleyman'
#password = 'zapata12'

ssid = 'FiberHGW_TPCB86_2.4GHz'
password = 'cyHRjRXs'

exit_btn = Pin(deneyap.GPKEY, Pin.IN)
print("\n\nHold button to exit..\n")
oprint("HOLD TO EXIT..",20,startfill=True)
time.sleep(3)
if not exit_btn.value():
    print("Connection Aborted!\n")
    sys.exit(1)

print("\nConnecting..\n")
oprint("CONNECTING..",20, startfill=True)
station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('\nConnection successful.\n')
oprint("CONNECTED",20, startfill=True)
oprint("IP:%s" % station.ifconfig()[0],0)
print(station.ifconfig())
print('\n')
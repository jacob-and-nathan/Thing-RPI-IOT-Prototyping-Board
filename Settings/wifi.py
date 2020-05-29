import sys
#Need to make list of dependencies, but keyboard module can be installed with pip3 install getkey. Adafruit circuit python is also needed. Maybe something else to. 
from getkey import getkey, keys
#Above doesn't work, use this
from evdev import InputDevice, categorize, ecodes
sys.path.append('/home/pi/ThingBoard/')

from OLED_Text import print_to_screen, show, clear

#while True:
 #   clear()
  #  key = getkey()
   # print ("Key is " +key)
    #print_to_screen(0, 0, key.upper(), 7, 1)
    #show()

device = InputDevice("/dev/input/event2")
for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        print (categorize(event))

import sys
sys.path.append('/home/pi/ThingBoard/')

from OLED_Text import print_to_screen, show, clear
#import RPI.GPIO as GPIO
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
clear()
print_to_screen(0, 0, "SCRIPT WORKING", 7, 1)
show()

print ("Script working")

from OLED_Text import print_to_screen, show, clear
import os
os.popen("touch run script2.py")
import RPi.GPIO as GPIO
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
from board import SCL, SDA
import os 

print_to_screen(0, 0, "SHUTTING DOWN PLEASE WAIT", 7, 1)
show()
os.popen ("sudo shutdown -h now")

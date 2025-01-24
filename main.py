from apps.files.files import Files
from OLED_Text import print_to_screen, show, clear
from OLED_Icons import folder_icon, python_icon
from src.user_input.user_input_interface import UserInputHandler
import os
# import RPi.GPIO as GPIO
# GPIO.setwarnings(False) 
# GPIO.setmode(GPIO.BCM)
import time
# x = 0
# clicked = False
# folders_entered = 0
# file_prefix = '' 
# back_button = False

# #file_path_list = os.popen("pwd").readlines()
# # file_path = "/home/pi/ThingBoard"
# file_path = "/home/jacob"
# #print (file_path) 
# files = os.popen ("ls " + file_path).readlines()
# print_to_screen(0, 0, files[x].upper(), 7, 1)
# show()
user_input = UserInputHandler("keyboard")

# from board import SCL, SDA

# """SW1 (Top switch)"""
# GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# """SW2 (Left switch)"""
# GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# """SW3(Right switch)"""
# GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# """SW4 (Bottom switch)"""
# GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# """SW5 (Select switch"""
# GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# def right_button() :
#     clear()
#     x = x + 1
#     if x == len(files) :
#         x = 0
#     print_to_screen(0, 0, files[x].upper(), 7, 1)
#     show()

app = Files(user_input)

while True:
    app.loop()
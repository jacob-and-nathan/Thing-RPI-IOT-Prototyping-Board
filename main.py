from OLED_Text import print_to_screen, show, clear
from OLED_Icons import folder_icon, python_icon
from src.user_input.user_input_interface import UserInputHandler
import os
# import RPi.GPIO as GPIO
# GPIO.setwarnings(False) 
# GPIO.setmode(GPIO.BCM)
import time
x = 0
clicked = False
folders_entered = 0
file_prefix = '' 
back_button = False

#file_path_list = os.popen("pwd").readlines()
# file_path = "/home/pi/ThingBoard"
file_path = "/home/jacob"
#print (file_path) 
files = os.popen ("ls " + file_path).readlines()
print_to_screen(0, 0, files[x].upper(), 7, 1)
show()
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

def convert_list_to_string (list) :
    string = ""
    for ele in list :
        string += '/'
        string += ele
    return string

def go_back (file_path_string) :
    file_path_array = file_path_string.split('/')
    length = len(file_path_array)
    del file_path_array[length-1]
    file_path_array = convert_list_to_string(file_path_array)
    return file_path_array


def right_button() :
    clear()
    x = x + 1
    if x == len(files) :
        x = 0
    print_to_screen(0, 0, files[x].upper(), 7, 1)
    show()

while True:
    """NEED TO imporove code for SW2 and SW3"""
    print (x)
    user_input.read_button_states()
    # button_state_SW1 = GPIO.input(17)
    # button_state_SW2 = GPIO.input(27)
    # button_state_SW3 = GPIO.input(22)
    # button_state_SW4 = GPIO.input(23)
    # button_state_SW5 = GPIO.input(24)
    button_state_SW1 = user_input.is_button_on("1")
    button_state_SW2 = user_input.is_button_on("2")
    button_state_SW3 = user_input.is_button_on("3")
    button_state_SW4 = user_input.is_button_on("4")
    button_state_SW5 = user_input.is_button_on("5")
    if button_state_SW3 == False:
        x = x + 1
        clear()
        if x == len(files):
            clear()
            # x = len(files)
            print ("back button is true")
            back_button = True
            print_to_screen(0, 0, "GO BACK", 7, 1)
            show()
            x = -1
        else :
            if x > len(files):
                x = 0 
            print_to_screen(0, 0, files[x].upper(), 7, 1)
            show()
            back_button = False

    elif button_state_SW2 == False:
        clear()
        """Put following if statement inside next if statement, also do with SW2"""
       
        x = x - 1
        # if x == len(files):
        #     clear()
        #     x = 0 
        #     back_button = True
        #     print_to_screen(0, 0, "GO BACK", 7, 1)
        #     show()
        # else:
        if x == -1:
            x = len(files)
            clear()
            # x = 0
            back_button = True
            print_to_screen(0, 0, "GO BACK", 7, 1)
        else:
            if x < -1:
                x = len(files) - 1
            print_to_screen(0, 0, files[x].upper(), 7, 1)
            back_button = False
        show()
    elif button_state_SW5 == False:
        clear()
        "If 'go back' is being displayed, go back one directory"""
        if back_button == True:
            file_path = go_back(file_path)
            x = 0            
            files = os.popen("ls " + file_path).readlines()
            "Run file if the file name contains .py"""
        elif '.py' in files[x] :
            code_result = os.popen ("python3 " + file_path + '/' + files[x]).readlines()
            quit()
            """If the item at position x is not a .py file, go forward one directory"""    
        else:
            file_path = file_path + '/'
            file_path += files[x].rstrip("\n\r")
            if folders_entered > 0 :
                file_prefix = '/'
            folders_entered = folders_entered + 1
            files = os.popen("ls " + file_path).readlines()
            x = 0
        print_to_screen(0, 0, files[x].upper(), 7, 1)
        show ()

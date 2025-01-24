"""
Run the code for the self._files app
"""
import os
from OLED_Text import print_to_screen, show, clear

class Files:
    def __init__(self, user_input):
        self._user_input = user_input
        self._x = 0
        self._folders_entered = 0
        self._file_prefix = '' 
        self._back_button = False

        #self._file_path_list = os.popen("pwd").readlines()
        # self._file_path = "/home/pi/ThingBoard"
        self._file_path = "/home/jacob"
        #print (self._file_path) 
        self._files = os.popen ("ls " + self._file_path).readlines()
        print_to_screen(0, 0, self._files[self._x].upper(), 7, 1)
        show()

    def go_back (self, file_path_string) :
        file_path_array = file_path_string.split('/')
        length = len(file_path_array)
        del file_path_array[length-1]
        file_path_array = self.convert_list_to_string(file_path_array)
        return file_path_array

    def convert_list_to_string (self, list) :
        string = ""
        for ele in list :
            string += '/'
            string += ele
        return string

    def loop(self):
        """
        TODO: Improve code to make it nicer
        """
        print (self._x)
        self._user_input.read_button_states()
        # button_state_SW1 = GPIO.input(17)
        # button_state_SW2 = GPIO.input(27)
        # button_state_SW3 = GPIO.input(22)
        # button_state_SW4 = GPIO.input(23)
        # button_state_SW5 = GPIO.input(24)
        button_state_SW1 = self._user_input.is_button_on("1")
        button_state_SW2 = self._user_input.is_button_on("2")
        button_state_SW3 = self._user_input.is_button_on("3")
        button_state_SW4 = self._user_input.is_button_on("4")
        button_state_SW5 = self._user_input.is_button_on("5")
        if button_state_SW3 == False:
            self._x = self._x + 1
            clear()
            if self._x == len(self._files):
                clear()
                # x = len(self._files)
                print ("back button is true")
                self._back_button = True
                print_to_screen(0, 0, "GO BACK", 7, 1)
                show()
                self._x = -1
            else :
                if self._x > len(self._files):
                    self._x = 0 
                print_to_screen(0, 0, self._files[self._x].upper(), 7, 1)
                show()
                self._back_button = False

        elif button_state_SW2 == False:
            clear()
            """Put following if statement inside next if statement, also do with SW2"""
        
            self._x = self._x - 1
            if self._x == -1:
                self._x = len(self._files)
                clear()
                # x = 0
                self._back_button = True
                print_to_screen(0, 0, "GO BACK", 7, 1)
            else:
                if self._x < -1:
                    self._x = len(self._files) - 1
                print_to_screen(0, 0, self._files[self._x].upper(), 7, 1)
                self._back_button = False
            show()
        elif button_state_SW5 == False:
            clear()
            "If 'go back' is being displayed, go back one directory"""
            if self._back_button == True:
                self._file_path = self.go_back(self._file_path)
                self._x = 0            
                self._files = os.popen("ls " + self._file_path).readlines()
                "Run file if the file name contains .py"""
            elif '.py' in self._files[self._x] :
                code_result = os.popen ("python3 " + self._file_path + '/' + self._files[self._x]).readlines()
                quit()
                """If the item at position x is not a .py file, go forward one directory"""    
            else:
                self._file_path = self._file_path + '/'
                self._file_path += self._files[self._x].rstrip("\n\r")
                if self._folders_entered > 0 :
                    self._file_prefix = '/'
                self._folders_entered = self._folders_entered + 1
                self._files = os.popen("ls " + self._file_path).readlines()
                self._x = 0
            print_to_screen(0, 0, self._files[self._x].upper(), 7, 1)
            show ()

# from board import SCL, SDA
# import busio
from src.graphics.display_engine.display_engine_interface import DisplayEngine
import time
from OLED_Icons import folder_icon, python_icon

# Import the SSD1306 module.
# import adafruit_ssd1306


# Create the I2C interface.
# i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
# display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
#display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)

display = DisplayEngine("emulator", 128, 64)

"Basically, this file is mostly arrays.. then there's a tiny bit of 'real' code"

A_small_arr = [[0, 1, 1, 1, 0],
               [1, 0, 0, 0, 1],
               [1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 0, 0, 0, 1]]

B_small_arr = [[1, 1, 1, 1, 0],
               [1, 0, 0, 0, 1],
               [1, 1, 1, 1, 0],
               [1, 0, 0, 0, 1],
               [1, 1, 1, 1, 0]]

C_small_arr = [[0, 1, 1, 1, 0],
               [1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0]]

D_small_arr = [[1, 1, 1, 0, 0],
               [1, 0, 0, 1, 0],
               [1, 0, 0, 1, 0],
               [1, 0, 0, 1, 0],
               [1, 1, 1, 0, 0]]

E_small_arr = [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 0],
               [1, 1, 1, 0, 0],
               [1, 0, 0, 0, 0],
               [1, 1, 1, 1, 1]]

F_small_arr = [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 0],
               [1, 1, 1, 0, 0],
               [1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0]]

G_small_arr = [[0, 1, 1, 1, 0],
               [1, 0, 0, 0, 0],
               [1, 0, 1, 1, 0],
               [1, 0, 0, 1, 0],
               [0, 1, 1, 0, 0]]

H_small_arr = [[1, 0, 0, 0, 1],
               [1, 0, 0, 0, 1],
               [1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 0, 0, 0, 1]]

I_small_arr = [[0, 1, 1, 1, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0],
               [0, 1, 1, 1, 0]]

J_small_arr = [[0, 0, 0, 0, 1], 
               [0, 0, 0, 0, 1],
               [0, 0, 0, 0, 1],
               [1, 0, 0, 0, 1],
               [0, 1, 1, 1, 0]]

K_small_arr = [[1, 0, 0, 1, 0],
               [1, 0, 1, 0, 0],
               [1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0],
               [1, 0, 0, 1, 0]]

L_small_arr = [[1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0],
               [1, 1, 1, 1, 1]]

M_small_arr = [[1, 0, 0, 0, 1],
               [1, 1, 0, 1, 1],
               [1, 0, 1, 0, 1],
               [1, 0, 0, 0, 1],
               [1, 0, 0, 0, 1]]

N_small_arr = [[1, 0, 0, 0, 1],
               [1, 1, 0, 0, 1],
               [1, 0, 1, 0, 1],
               [1, 0, 0, 1, 1],
               [1, 0, 0, 0, 1]]

O_small_arr = [[0, 1, 1, 1, 0],
               [1, 0, 0, 0, 1],
               [1, 0, 0, 0, 1],
               [1, 0, 0, 0, 1],
               [0, 1, 1, 1, 0]]

P_small_arr = [[1, 1, 1, 0, 0],
               [1, 0, 0, 1, 0],
               [1, 1, 1, 0, 0],
               [1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0]]

Q_small_arr = [[0, 1, 1, 1, 0],
               [1, 0, 0, 0, 1],
               [1, 0, 0, 0, 1],
               [1, 0, 0, 1, 0],
               [0, 1, 1, 0, 1]]

R_small_arr = [[1, 1, 1, 0, 0],
               [1, 0, 0, 1, 0],
               [1, 1, 1, 0, 0],
               [1, 0, 0, 1, 0],
               [1, 0, 0, 0, 1]]

S_small_arr = [[1, 1, 1, 1, 0],
               [1, 0, 0, 0, 0],
               [1, 1, 1, 1, 1],
               [0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1]]

T_small_arr = [[1, 1, 1, 1, 1],
               [0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0]]

U_small_arr = [[1, 0, 0, 0, 1],
               [1, 0, 0, 0, 1],
               [1, 0, 0, 0, 1],
               [1, 0, 0, 0, 1],
               [0, 1, 1, 1, 0]]

V_small_arr = [[1, 0, 0, 0, 1],
               [1, 0, 0, 0, 1],
               [0, 1, 0, 1, 0],
               [0, 1, 0, 1, 0],
               [0, 0, 1, 0, 0]]

W_small_arr = [[1, 0, 1, 0, 1],
               [1, 0, 1, 0, 1],
               [1, 0, 1, 0, 1],
               [1, 0, 1, 0, 1],
               [0, 1, 0, 1, 0]]

X_small_arr = [[1, 0, 0, 0, 1],
               [0, 1, 0, 1, 0],
               [0, 0, 1, 0, 0],
               [0, 1, 0, 1, 0],
               [1, 0, 0, 0, 1]]

Y_small_arr = [[1, 0, 0, 0, 1],
               [0, 1, 0, 1, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0]]

Z_small_arr = [[1, 1, 1, 1, 1],
               [0, 0, 0, 1, 0],
               [0, 0, 1, 0, 0],
               [0, 1, 0, 0, 0],
               [1, 1, 1, 1, 1]]

A_large_arr = [[1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0]]

B_large_arr = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]]

C_large_arr = [[1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]]

D_large_arr = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 0, 1, 0, 0, 0]]

E_large_arr = [[1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]]

F_large_arr = [[1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

G_large_arr = [[1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]]

H_large_arr = [[1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0]]

I_large_arr = [[0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 1, 1, 1, 0, 0, 0]]

def draw_letter (x, y, array, pixel_size) :
    i = 0
    j = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            print (array[i][j])
            display.pixel(x+j, y+i, array[i][j]) 
            display.pixel(x+j+pixel_size, y+i, array[i][j])
            display.pixel(x+j, y+i+pixel_size, array[i][j])
            display.pixel(x+j+pixel_size, y+i+pixel_size, array[i][j])
        y = y + pixel_size

"""The two arrays below are used to convert a letter a user types into an array name"""
letter_arrs = [A_small_arr, B_small_arr, C_small_arr, D_small_arr, E_small_arr, F_small_arr, G_small_arr, H_small_arr, I_small_arr, J_small_arr, K_small_arr, L_small_arr, M_small_arr, N_small_arr, O_small_arr, P_small_arr, Q_small_arr, R_small_arr, S_small_arr, T_small_arr, U_small_arr, V_small_arr, W_small_arr, X_small_arr, Y_small_arr, Z_small_arr]

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

"Print a message to the screen"
def print_to_screen (x, y, message, count, pixel_size) :
    i = 0
    element = 0
    "Cycle through the characters in the message"
    for element in range(0, len(message)):
        "Cycle through the letters in letters array, match the letters in message[element]. Therefore, if message[element] == H then letters[i] = letters[7], draw_letter() is called using letter_arrs[7] as a parameter for 'array' (see draw_letter function)" 
        for i in range(len(letters)) :
            if letters[i] == message[element] :
                draw_letter(x, y, letter_arrs[i], pixel_size)
            i = i + 1
            "If the text display overflows screen, print it on a new line"
            if x > 128 - count:
                x = 0
                y = y + count + 5
        element = element + 1
        x = x + count
def show() :
    display.show()

def clear() :
    display.fill(0)


"""
Manage button input from the keyboard
"""
from src.user_input.base_input_handler import BaseHandler

class KeyboardHandler(BaseHandler):
    def __init__(self):
        self._button_config = {
            "1": "w",
            "2": "a",
            "3": "s",
            "4": "d",
            "5": "f"
        }
        self._button_numbers = list(self._button_config.keys())

    def read_button_states(self):
        """
        Read the button states
        """
        buttons_pressed = input("Press keys, then press enter:")
        button_states = {}
        for number in self._button_numbers:
            if self._button_config[number] in buttons_pressed:
                button_states[number] = "on"
            else:
                button_states[number] = "off"
        return button_states

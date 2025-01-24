"""
Manage user input using various classes
"""
from src.user_input.physical_input_handler import PhysicalHandler
from src.user_input.keyboard_input_handler import KeyboardHandler

class UserInputHandler:
    def __init__(self, input_type):
        if input_type == "physical":
            self._handler = PhysicalHandler()
        elif input_type == "keyboard":
            self._handler = KeyboardHandler()
        else:
            raise ValueError(f"Input type {input_type} not allowed!")

        self.button_states = {}

    def read_button_states(self):
        """
        Read the button states

        Returns:
            dict: The button states
        """
        self.button_states = self._handler.read_button_states()
        return self.button_states

    def is_button_on(self, button_number:str):
        """
        See if a button is on

        Args:
            button_number (str): The button number

        Returns:
            bool: False if the button exists and is on
        """
        if button_number in self.button_states and self.button_states[button_number] == "on":
            return False
        else:
            return True

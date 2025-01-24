"""
Base class to handle input events
"""
from abc import ABC, abstractmethod

class BaseHandler(ABC):
    @abstractmethod
    def read_button_states(self):
        """
        Read the button states

        Returns:
            dict: The button states
        """
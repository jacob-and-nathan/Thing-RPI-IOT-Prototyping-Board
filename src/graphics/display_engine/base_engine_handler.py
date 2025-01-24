"""
Base class for the display engine
"""
from abc import ABC, abstractmethod

class BaseDisplayEngine(ABC):
    def __init__(self, x:int, y:int):
        self._x = x
        self._y = y

    @abstractmethod
    def pixel(self, x:int, y:int, status:int):
        """
        Draw a pixel on the screen

        Args:
            x: The x location
            y: The y location
            status: 0 or 1 (off or on)
        """

    @abstractmethod
    def show(self):
        """
        Show the data in the buffer
        """

    @abstractmethod
    def fill(self, status:int):
        """
        Fill the screen with 0 or 1

        Args:
            status (int): The value to fill the screen with
        """

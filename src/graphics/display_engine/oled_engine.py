"""
Display text on an OLED screen
"""
from src.graphics.display_engine.base_engine_handler import BaseDisplayEngine

class OLEDEngine(BaseDisplayEngine):
    def pixel(self, x:int, y:int, status:int):
        """
        Draw a pixel on the screen

        Args:
            x: The x location
            y: The y location
            status: 0 or 1 (off or on)
        """

    def show(self):
        """
        Show the data in the buffer
        """

    def fill(self, status:int):
        """
        Fill the screen with 0 or 1

        Args:
            status (int): The value to fill the screen with
        """

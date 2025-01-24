"""
Display engine to control how graphics are displayed
"""
from src.graphics.display_engine.emulator_engine import EmulatorEngine
from src.graphics.display_engine.oled_engine import OLEDEngine

class DisplayEngine:
    def __init__(self, engine_type, x:int, y:int):
        if engine_type == "oled":
            self._handler = OLEDEngine(x, y)
        elif engine_type == "emulator":
            self._handler = EmulatorEngine(x, y)
        else:
            raise ValueError(f"Input type {engine_type} not allowed!")

    def pixel(self, x:int, y:int, status:int):
        """
        Draw a pixel on the screen

        Args:
            x: The x location
            y: The y location
            status: 0 or 1 (off or on)
        """
        self._handler.pixel(x, y, status)

    def show(self):
        """
        Show the data in the buffer
        """
        self._handler.show()

    def fill(self, status:int):
        """
        Fill the screen with 0 or 1

        Args:
            status (int): The value to fill the screen with
        """
        self._handler.fill(status)

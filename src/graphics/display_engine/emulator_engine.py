"""
Display text on the computer screen with print
"""
import os
from src.graphics.display_engine.base_engine_handler import BaseDisplayEngine

class EmulatorEngine(BaseDisplayEngine):
    def __init__(self, x:int, y:int):
        super().__init__(x, y)
        self._screen = [[0 for _ in range(x)] for _ in range(y)]


    def pixel(self, x: int, y: int, status: int):
        """
        Draw a pixel on the screen

        Args:
            x: The x location
            y: The y location
            status: 0 or 1 (off or on)
        """
        # Check if the coordinates are within the screen bounds
        if 0 <= x < len(self._screen[0]) and 0 <= y < len(self._screen):
            if status in (0, 1):  # Ensure the status is either 0 or 1
                self._screen[y][x] = status
            else:
                raise ValueError("Status must be 0 or 1")
        else:
            print(f"Coordinates out of bounds: x={x}, y={y}")

    def show(self):
        """
        Show the data in the buffer with a red border
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        # ANSI escape code for red color
        RED = "\033[31m"
        RESET = "\033[0m"

        # Determine the width of the screen
        width = len(self._screen[0])

        # Print the top border
        print(RED + "-" * (width + 2) + RESET)

        # Print each row with side borders
        for row in self._screen:
            print(RED + "|" + RESET, end="")  # Left border
            for pixel in row:
                item = " " if pixel == 0 else "#"
                print(item, end="")
            print(RED + "|" + RESET)  # Right border

        # Print the bottom border
        print(RED + "-" * (width + 2) + RESET)
            

    def fill(self, status:int):
        """
        Fill the screen with 0 or 1

        Args:
            status (int): The value to fill the screen with
        """
        self._screen = [[status for _ in range(self._x)] for _ in range(self._y)]

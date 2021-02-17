from config import *
import colorama
from colorama import Fore, Back, Style
import numpy as np
import random


colorama.init()

class board():
    def __init__(self, rows , cols ,frames):
        self._rows = rows
        self._cols = columns
        self._grid = ([[Back.BLACK + Fore.BLACK + ' ' for col in range(self._cols)]
                       for row in range(self._rows)])

        for val in range(self._cols):
            self._grid[0][val] = Fore.WHITE + 'X'
            self._grid[self._rows - 1][val] = Fore.GREEN + 'X'
            self._grid[self._rows - 2][val] = Fore.GREEN + 'X'
        
        for val in range(self._rows):
            self._grid[val][0] = Fore.WHITE + 'X'
            self._grid[val][self._cols - 1] = Fore.WHITE + 'X'

    def get_grid(self, i , j):
        return self._grid[i][j]
        
    def change_grid(self, i , j,val):
        self._grid[i][j] = val


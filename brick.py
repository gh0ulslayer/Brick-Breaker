import config
import colorama
from colorama import Fore, Back, Style
import numpy as np
import random

colorama.init()

class brick():
    def __init__(self, rows , cols):
        self._thick = 1
        self._len = 3
        self._xpos = rows
        self._ypos = cols
        self._visible = 1
    
class brick4(brick):

    def __init__(self, rows , cols):
        super().__init__(rows, cols)
        self._design = ([[Fore.YELLOW + '▤' for col in range(self._len)]
                            for row in range(self._thick)])
        self._level = 4
    
    def get_brick(self, i , j):
        if(self._visible == 1):
            return self._design[i][j]
        else:
            return ' '
    
class brick3(brick):

    def __init__(self, rows , cols):
        super().__init__(rows, cols)
        self._design = ([[Fore.CYAN + '▤' for col in range(self._len)]
                            for row in range(self._thick)])
        self._level = 3

    def get_brick(self, i , j):
        if(self._visible == 1):
            return self._design[i][j]
        else:
            return ' '

class brick2(brick):

    def __init__(self, rows , cols):
        super().__init__(rows, cols)
        self._design = ([[Fore.BLUE + '▤' for col in range(self._len)]
                            for row in range(self._thick)])
        self._level = 2


    def get_brick(self, i , j):
        if(self._visible == 1):
            return self._design[i][j]
        else:
            return ' '
    
class brick1(brick):

    def __init__(self, rows , cols):
        super().__init__(rows, cols)
        self._design = ([[Fore.MAGENTA  +  '▤' for col in range(self._len)]
                            for row in range(self._thick)])
        self._level = 1


    def get_brick(self, i , j):
        if(self._visible == 1):
            return self._design[i][j]
        else:
            return ' '

class bomb_brick(brick):

    def __init__(self, rows , cols):
        super().__init__(rows, cols)
        self._design = ([[Fore.LIGHTGREEN_EX  +  '▤' for col in range(self._len)]
                            for row in range(self._thick)])
        self._level = 1


    def get_brick(self, i , j):
        if(self._visible == 1):
            return self._design[i][j]
        else:
            return ' '
   
    


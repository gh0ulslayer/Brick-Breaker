import config
import colorama
from colorama import Fore, Back, Style
import numpy as np
import random

colorama.init()

class brick():
    def __init__(self, rows , cols):
        self._thick = 1
        self._len = 4
       

    
class brick1(brick):

    def __init__(self, rows , cols):
        super().__init__(rows, cols)
        self._design = ([[Fore.YELLOW + '$' for col in range(self._len)]
                            for row in range(self._thick)])
    
    def get_brick(self, i , j):
        return self._design[i][j]
    
class brick2(brick):

    def __init__(self, rows , cols):
        super().__init__(rows, cols)
        self._design = ([[Fore.CYAN + '⛶' for col in range(self._len)]
                            for row in range(self._thick)])
    
    def get_brick(self, i , j):
        return self._design[i][j]

class brick3(brick):

    def __init__(self, rows , cols):
        super().__init__(rows, cols)
        self._design = ([[Fore.BLUE + '$' for col in range(self._len)]
                            for row in range(self._thick)])
    
    def get_brick(self, i , j):
        return self._design[i][j]
    
class brick4(brick):

    def __init__(self, rows , cols):
        super().__init__(rows, cols)
        self._design = ([[Fore.MAGENTA + '$' for col in range(self._len)]
                            for row in range(self._thick)])
    
    def get_brick(self, i , j):
        return self._design[i][j]
    
   
    


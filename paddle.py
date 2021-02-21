import config
import colorama
from colorama import Fore, Back, Style
import numpy as np
import random
from board import board

colorama.init()

class movee():
    def __init__(self, rows , cols):
        self._start = 39
        self._paddlelen = 20
        self._design = ([[Fore.RED + '#' for col in range(self._paddlelen)]
                       for row in range(2)])

        
        # self._design = [["*","o","*"],["*"," ","*"],["*","*","*"]]
        # for i in range(3):
            # for j in range(3):
                # self._design[i][j] = Fore.RED + '*'
       
    def change_paddle(self):
        self._design = ([[Fore.RED + '#' for col in range(self._paddlelen)]
                       for row in range(2)])

    def get_paddle(self, i , j):
        return self._design[i][j]
    
    def move_right(self, i ):
        self._start += i

    def move_left(self, i ):
        self._start -= i



    


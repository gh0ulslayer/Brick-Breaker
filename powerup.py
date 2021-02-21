import config
import colorama
from colorama import Fore, Back, Style
import numpy as np
import random

colorama.init()

class powerup():
    def __init__(self, rows , cols):
        self._xpos = rows
        self._ypos = cols
        self._catched = 0

    def position(self):
        arr = []
        arr.append(Fore.WHITE +'P')
        arr.append(self._xpos)
        arr.append(self._ypos)
        return arr    

class expand_paddle(powerup):

    def __init__(self, rows , cols):
        super().__init__(rows, cols)
        
    def position(self):
        arr = []
        arr.append(Fore.WHITE + '►')
        arr.append(self._xpos)
        arr.append(self._ypos)
        return arr    
    
    def x_pos(self):
        if(self._xpos < 26):
            self._xpos += 1
        else:
            if(self._catched == 0):
                self._xpos = 29 
            else:
                self._xpos = 26 

        return self._xpos 
    
class shrink_paddle(powerup):

    def __init__(self, rows , cols):
        super().__init__(rows, cols)
        
    def position(self):
        arr = []
        arr.append(Fore.WHITE + '◄')
        arr.append(self._xpos)
        arr.append(self._ypos)
        return arr    
    
    def x_pos(self):
        if(self._xpos < 26):
            self._xpos += 1
        else:
            if(self._catched == 0):
                self._xpos = 29 
            else:
                self._xpos = 26 

        return self._xpos

class fast_ball(powerup):

    def __init__(self, rows , cols):
        super().__init__(rows, cols)
        
    def position(self):
        arr = []
        arr.append(Fore.WHITE + 'F')
        arr.append(self._xpos)
        arr.append(self._ypos)
        return arr    
    
    def x_pos(self):
        if(self._xpos < 26):
            self._xpos += 1
        else:
            if(self._catched == 0):
                self._xpos = 29 
            else:
                self._xpos = 26 

        return self._xpos


class thru_ball(powerup):

    def __init__(self, rows , cols):
        super().__init__(rows, cols)
        
    def position(self):
        arr = []
        arr.append(Fore.WHITE + 'T')
        arr.append(self._xpos)
        arr.append(self._ypos)
        return arr    
    
    def x_pos(self):
        if(self._xpos < 26):
            self._xpos += 1
        else:
            if(self._catched == 0):
                self._xpos = 29 
            else:
                self._xpos = 26 

        return self._xpos


class grab_ball(powerup):

    def __init__(self, rows , cols):
        super().__init__(rows, cols)
        
    def position(self):
        arr = []
        arr.append(Fore.WHITE + 'G')
        arr.append(self._xpos)
        arr.append(self._ypos)
        return arr    
    
    def x_pos(self):
        if(self._xpos < 26):
            self._xpos += 1
        else:
            if(self._catched == 0):
                self._xpos = 29 
            else:
                self._xpos = 26 

        return self._xpos


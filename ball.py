import config
import colorama
from colorama import Fore, Back, Style
import numpy as np
import random
colorama.init()


class ball_att():
    def __init__(self):
        self._xpos = 20
        self._ypos = 43
        self._xvel = -1
        self._yvel = 1

        self._design = Fore.YELLOW  +  '⬤'
        
        
    def get_ball(self):
        return self._design

    def get_xpos(self):
        if(self._xpos > 1 and self._xpos < 24):
            self._xvel *= 1
        else:
            if(self._xpos < 2):
                self._xvel *= -1
            elif(config.flag == 1):
                self._xvel *= -1
                # config.flag = 0      
                #uncomment before use
            elif(config.flag == 0):
                config.lives -=1
                config.grab = 1
                config.flag_gb = 0
                self._xvel *= -1

        self._xpos += self._xvel
        
        return self._xpos 

    def get_ypos(self):
        if(self._ypos + self._yvel < 89 and self._ypos + self._yvel > 1):
            self._yvel *= 1
            self._ypos += self._yvel
        else:
            self._yvel *= -1
            self._ypos += self._yvel

        return self._ypos 
    



    


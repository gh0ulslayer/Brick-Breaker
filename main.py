from config import *
import colorama
from colorama import Fore, Back, Style
from input import *
import termios
import subprocess as sp
import time
import tty
import sys
import os
from board import *
from paddle import *
from ball import *

colorama.init()

if __name__ == "__main__":
    orig_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)
    input = input()
    input.hide_cursor()
    pos_y = 4
    game_back = board(rows,columns, frames)
    while(1):

        game_paddle = movee(rows,columns)

        if input.input_to():
            val = input.getch()
            # print(rows)
            if(val == 'q' or val == 'Q'):
                break
            elif(val == "a" or val == "A"):
                if(pos_y > 1):
                    pos_y-=1
                else:
                    pos_y = 1
            elif(val == "d" or val == "D"):
                if(pos_y < 89-paddle_len):
                    pos_y+=1
                else:
                    pos_y = 89 - paddle_len  


        for i in range(2):
            for j in range(paddle_len):
                    game_back._grid[25+i][pos_y+j] = game_paddle.get_paddle(i,j)
        
        output_str = ""
        for row in range(rows):
            for col in range(columns):
                    output_str += game_back.get_grid(row,col)
            output_str += '\n'
        
        
        print('\033[H' + output_str)
        if(pos_y > 0 and pos_y  < 89):
            for i in range(2):
                for j in range(paddle_len):
                    if(pos_y  < 89 and pos_y > 0):
                        game_back._grid[25+i][pos_y+j] = ' '
                    elif(pos_y < 1):
                        pos_y = 1
                    elif(pos_y > 89):
                        pos_y = 88
            # Object.render()
    
    input.show_cursor()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
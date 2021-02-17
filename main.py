import config
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
    rows = config.rows
    columns = config.columns
    frames = config.frames
    pos_y = 4
    game_back = board(rows,columns, frames)
    game_paddle = movee(config.rows,config.columns)
    game_ball = ball_att()
    
    while(1):
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
                if(pos_y < 89- game_paddle._paddlelen):
                    pos_y+=1
                else:
                    pos_y = 89 - game_paddle._paddlelen  
            elif(val == "i"):
                game_paddle._paddlelen += 1
                game_paddle.change_paddle()
            
            termios.tcflush(sys.stdin, termios.TCIOFLUSH)
            
        for i in range(2):
            for j in range(game_paddle._paddlelen):
                    game_back._grid[25+i][pos_y+j] = game_paddle.get_paddle(i,j)
        
        ball_x = game_ball.get_xpos()
        ball_y = game_ball.get_ypos()
        if(game_ball.get_ypos() < 89):
            game_back._grid[ball_x][ball_y] = game_ball.get_ball()
        
        output_str = ""
        for row in range(rows):
            for col in range(columns):
                    output_str += game_back.get_grid(row,col)
            output_str += '\n'
        
        
        print('\033[H' + output_str)
        #clearing the previous paddle
        if(pos_y > 0 and pos_y  < 89):
            for i in range(2):
                for j in range(game_paddle._paddlelen):
                    if(pos_y  < 89 and pos_y > 0):
                        game_back._grid[25+i][pos_y+j] = ' '
                    elif(pos_y < 1):
                        pos_y = 1
                    elif(pos_y > 89):
                        pos_y = 88

        #clearing the ball
        game_back._grid[ball_x][ball_y] = ' '
        
        time.sleep(0.05)
            # Object.render()
        

    input.show_cursor()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
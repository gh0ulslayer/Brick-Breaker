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
from brick import *

colorama.init()

if __name__ == "__main__":
    orig_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)
    input = input()
    input.hide_cursor()
    rows = config.rows
    columns = config.columns
    frames = config.frames
    game_back = board(rows,columns, frames)
    game_paddle = movee(config.rows,config.columns)
    game_brick = brick2(config.rows,config.columns)
    game_ball = ball_att()
    b4 = []
    for i in range(10):
        b4.append(brick4(config.rows,config.columns))

    while(1):
        #taking inputs
        if input.input_to():
            val = input.getch()
            # print(rows)

            if(val == 'q' or val == 'Q'):
                break
            elif(val == "a" or val == "A"):
                if(game_paddle._start > 1):
                    game_paddle._start-=1
                else:
                    game_paddle._start = 1
            elif(val == "d" or val == "D"):
                if(game_paddle._start < 89- game_paddle._paddlelen):
                    game_paddle._start+=1
                else:
                    game_paddle._start = 89 - game_paddle._paddlelen  
            elif(val == "i"):
                game_paddle._paddlelen += 1
                game_paddle.change_paddle()
            
            termios.tcflush(sys.stdin, termios.TCIOFLUSH)
            
        #filling paddle in grid
        for i in range(2):
            for j in range(game_paddle._paddlelen):
                    game_back._grid[25+i][game_paddle._start+j] = game_paddle.get_paddle(i,j)
        
        ball_x = game_ball.get_xpos()
        ball_y = game_ball.get_ypos()
        #filling ball in  grid
        if(game_ball.get_ypos() < 89):
            game_back._grid[ball_x][ball_y] = game_ball.get_ball()
        
        #filling bricks
        # for i in range(game_brick._thick):
            # for j in range(game_brick._len):
                    # game_back._grid[10+i][10+j] = game_brick.get_brick(i,j)
        
        for k in range(10):
            newbr = b4[k]
            for i in range(game_brick._thick):
                for j in range(game_brick._len):
                    game_back._grid[10+i][10+j+k + game_brick._len] = newbr.get_brick(i,j)
            
        
        #collision between ball and paddle
        if(ball_y > game_paddle._start and ball_y < game_paddle._start + game_paddle._paddlelen and ball_x == 24):
            config.flag = 1

        #printing the grid
        output_str = ""
        for row in range(rows):
            for col in range(columns):
                    output_str += game_back.get_grid(row,col)
            output_str += '\n'
        print('\033[H' + output_str)

        #clearing the previous paddle
        if(game_paddle._start > 0 and game_paddle._start  < 89):
            for i in range(2):
                for j in range(game_paddle._paddlelen):
                    if(game_paddle._start  < 89 and game_paddle._start > 0):
                        game_back._grid[25+i][game_paddle._start+j] = ' '
                    elif(game_paddle._start < 1):
                        game_paddle._start = 1
                    elif(game_paddle._start > 89):
                        game_paddle._start = 88

        #clearing the ball
        game_back._grid[ball_x][ball_y] = ' '
        time.sleep(0.05)
            # Object.render()
        

    input.show_cursor()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
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
    game_brick = brick3(config.rows,config.columns)
    game_ball = ball_att()
    b1 = []
    for i in range(10):
        b1.append(brick4(5  , 10 + i*5))

    while(1):
        xcoords = []
        ycoords = []

        #taking inputs
        if input.input_to():
            val = input.getch()
            # print(rows)

            if(val == 'q' or val == 'Q'):
                break
            elif(val == "a" or val == "A"):
                if(game_paddle._start > 2):
                    game_paddle._start-=2
                else:
                    game_paddle._start = 1
            elif(val == "d" or val == "D"):
                if(game_paddle._start < 88- game_paddle._paddlelen):
                    game_paddle._start+=2
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
        xcoords.append(ball_x - game_ball._xvel)
        xcoords.append(ball_x)
        ycoords.append(ball_y - game_ball._yvel)
        ycoords.append(ball_y)
        
        #filling ball in  grid
        game_back._grid[xcoords[0]][ycoords[0]] = game_ball.get_ball()
        

        #filling bricks
        for k in range(10):
            newbr = b1[k]
            for i in range(game_brick._thick):
                for j in range(game_brick._len):
                    game_back._grid[newbr._xpos][newbr._ypos + j] = newbr.get_brick(i,j)
            
        
        #collision between ball and paddle
        if(ball_y > game_paddle._start and ball_y < game_paddle._start + game_paddle._paddlelen and ball_x == 24):
            config.flag = 1


        #collision between ball and bricks
        for k in range(10):
            newbr = b1[k]
            xstart = newbr._xpos
            xend = newbr._xpos + newbr._thick 
            ystart = newbr._ypos
            yend = newbr._ypos + newbr._len 
            if(newbr._level == 0):
                newbr._visible = 0
            if(newbr._level > 0):
                if(xcoords[0] > xcoords[1]):
                    if(xcoords[1] == xend):
                        if(ycoords[0] > ycoords[1]):
                            if(yend > ycoords[1] and yend < ycoords[0]):
                                game_ball._xvel *= -1
                                newbr._level -= 1
                            if(ystart > ycoords[1] and ystart < ycoords[0]):
                                newbr._level -= 1
                                game_ball._xvel *= -1
                        if(ycoords[1] > ycoords[0]):
                            if(yend < ycoords[1] and yend > ycoords[0]):
                                newbr._level -= 1
                                game_ball._xvel *= -1
                            if(ystart < ycoords[1] and ystart > ycoords[0]):
                                newbr._level -= 1
                                game_ball._xvel *= -1
                else:
                    if(xcoords[1] == xstart):
                        if(ycoords[0] > ycoords[1]):
                            if(yend > ycoords[1] and yend < ycoords[0]):
                                newbr._level -= 1
                                game_ball._xvel *= -1
                            if(ystart > ycoords[1] and ystart < ycoords[0]):
                                newbr._level -= 1
                                game_ball._xvel *= -1
                        if(ycoords[1] > ycoords[0]):
                            if(yend < ycoords[1] and yend > ycoords[0]):
                                newbr._level -= 1
                                game_ball._xvel *= -1
                            if(ystart < ycoords[1] and ystart > ycoords[0]):
                                newbr._level -= 1
                                game_ball._xvel *= -1
        
        for i in range(10):
            newbr = b1[i]
            if(newbr._level == 3):
                b1[i] = brick3(newbr._xpos  , newbr._ypos)
            if(newbr._level == 2):
                b1[i] = brick2(newbr._xpos  , newbr._ypos)
            if(newbr._level == 1):
                b1[i] = brick1(newbr._xpos  , newbr._ypos)
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
        if(ball_y < 89):
            game_back._grid[xcoords[0]][ycoords[0]] = ' '
        
        time.sleep(0.05)
        

    input.show_cursor()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
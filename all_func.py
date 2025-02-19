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
from powerup import *
from random import *
colorama.init()

#variables start from here
xcoords = []
ycoords = []
rows = config.rows
frames = config.frames
columns = config.columns
game_back = board(rows,columns, frames)

b1 = []
for i in range(10):
    b1.append(brick1(7  , 8 + i*7))
for i in range(10):
    b1.append(brick2(9  , 12 + i*7))
for i in range(10):
    b1.append(brick3(11  , 10 + i*7))


game_paddle = movee(config.rows,config.columns)
game_brick = brick3(config.rows,config.columns)
game_ball = ball_att()
b4 = []
ball_x = game_ball.get_xpos()
ball_y = game_ball.get_ypos()
for i in range(3):
    b4.append(brick4(4  , 30 + i*10))

powers = []
powerx = []
powery = []

for i in range(10):
    var = randint(0,2)
    powers.append(expand_paddle(b1[3*i + var]._xpos,b1[3*i + var]._ypos))
    powerx.append(b1[3*i+var]._xpos)
    powery.append(b1[3*i+var]._ypos)


powers[3] = shrink_paddle(powerx[3],powery[3])
powers[4] = fast_ball(powerx[4],powery[4])
powers[5] = thru_ball(powerx[5],powery[5])
powers[0] = grab_ball(powerx[0],powery[0])
powers[7] = fast_ball(powerx[7],powery[7])
powers[9] = shrink_paddle(powerx[9],powery[9])

powerup_timer = []
for i in range(10):
    powerup_timer.append(0)

bombs = []
for i in range(6):
    bombs.append(bomb_brick(5, 30 + i*5))

#functions start from here


#filling ball in grid
def show_ball():
    if(config.grab == 1):
        game_ball._xpos = 23 
        game_ball._ypos =  game_paddle._start + 4 
        game_back._grid[game_ball._xpos][game_ball._ypos] = game_ball.get_ball()

    else:
        game_back._grid[xcoords[0]][ycoords[0]] = game_ball.get_ball()

        
#powerup run
def powerup_run():
    for i in range(10):
        for j in range(30):
            if(b1[j]._xpos == powerx[i] and b1[j]._ypos == powery[i]):
                newbr = b1[j]
                if(newbr._level == 0):
                    newpr = powers[i]
                    x_newpr = newpr.x_pos()
                    game_back._grid[x_newpr][powers[i].position()[2]] = powers[i].position()[0]

#filling bricks in grid
def show_brick():
    for k in range(30):
        newbr = b1[k]
        for i in range(game_brick._thick):
            for j in range(game_brick._len):
                game_back._grid[newbr._xpos][newbr._ypos + j] = newbr.get_brick(i,j)
    
    for k in range(3):
        newbr = b4[k]
        for i in range(game_brick._thick):
            for j in range(game_brick._len):
                game_back._grid[newbr._xpos][newbr._ypos + j] = newbr.get_brick(i,j)
    
    for k in range(6):
        newbr = bombs[k]
        for i in range(game_brick._thick):
            for j in range(game_brick._len):
                game_back._grid[newbr._xpos][newbr._ypos + j] = newbr.get_brick(i,j)
    
#colour change of brick in collision
def colour_change():
    for i in range(30):
            newbr = b1[i]
            if(newbr._level == 3):
                b1[i] = brick3(newbr._xpos  , newbr._ypos)
            if(newbr._level == 2):
                b1[i] = brick2(newbr._xpos  , newbr._ypos)
            if(newbr._level == 1):
                b1[i] = brick1(newbr._xpos  , newbr._ypos)


#collsion between ball and paddle
def coll_paddle():
    if(ball_y > game_paddle._start and ball_y < game_paddle._start + game_paddle._paddlelen and ball_x == 24):
        config.flag = 1
        if(config.flag_gb == 1):
            config.grab = 1
        else:
            if(ball_y < game_paddle._start + game_paddle._paddlelen/4):
                game_ball._yvel -= 2
            elif(ball_y < game_paddle._start + game_paddle._paddlelen/2):
                game_ball._yvel -= 1
            elif(ball_y < game_paddle._start + game_paddle._paddlelen*3/4):
                game_ball._yvel += 1
            else:
                game_ball._yvel += 2


#collision between powerup and paddle
def coll_powerup():
    for i in range(10):
        newpr = powers[i]
        if( newpr._ypos > game_paddle._start and newpr._ypos < game_paddle._start + game_paddle._paddlelen and newpr._xpos == 24):
            powers[i]._catched = 1
            powerup_timer[i]= time.time()

#activating the powerup
def activating_powerup(): 
    for i in range(10):
        newpr = powers[i]
        if(newpr._catched == 1):
            if(newpr.position()[0] == Fore.WHITE + '►'):
                game_paddle._paddlelen += 2
                game_paddle.change_paddle()
            elif(newpr.position()[0] == Fore.WHITE + '◄'):
                game_paddle._paddlelen -= 2
                game_paddle.change_paddle()
            elif(newpr.position()[0] == Fore.WHITE + 'F'):
                game_ball._yvel *= 2
            elif(newpr.position()[0] == Fore.WHITE + 'T'):
                    config.flag_tb = 1
            elif(newpr.position()[0] == Fore.WHITE + 'G'):
                    config.flag_gb = 1
            
            newpr._catched = 0 


#powerup deactivate
def powerup_deactivate():
    for i in range(10):
        newpr = powers[i]
        t = time.time()
        
        if(powerup_timer[i] > 0):
            # print(powerup_timer[i],t)

            if(t - powerup_timer[i] > 10 ):
                if(newpr.position()[0] == Fore.WHITE + '►'):
                    game_paddle._paddlelen -= 2
                    game_paddle.change_paddle()
                elif(newpr.position()[0] == Fore.WHITE + '◄'):
                    game_paddle._paddlelen += 2
                    game_paddle.change_paddle()
                elif(newpr.position()[0] == Fore.WHITE + 'F'):
                    game_ball._yvel //= 2
                elif(newpr.position()[0] == Fore.WHITE + 'T'):
                        config.flag_tb = 0
                elif(newpr.position()[0] == Fore.WHITE + 'G'):
                        config.flag_gb = 0
                powerup_timer[i] = 0


            newpr._catched = 0 
    

#printing grid
def show_grid():
    output_str = ""
    for row in range(rows):
        for col in range(columns):
                output_str += game_back.get_grid(row,col)
        output_str += '\n'
    
    arr = []
    arr.append(config.lives)
    arr.append(config.score)
    config.time_played = time.time() - config.time_start
    arr.append(config.time_played)
    output_str += "Lives_remaining = "
    output_str += str(arr[0])
    output_str += "     "
    output_str += "Score = "
    output_str += str(arr[1])
    output_str += "     "
    output_str += "Time_played = "
    output_str += str(arr[2])
    output_str += " "
    output_str += '\n'

    print('\033[H' + output_str)
    

#clearing the grid
def clear_grid():
    for i in range(1,config.rows-1):
            for j in range(1,config.columns-1):
                game_back._grid[i][j] = ' '
        
    if(config.lives == 0): 
        for i in range(1,config.rows-1):
            for j in range(1,config.columns-1):
                game_back._grid[i][j] = ' '
            
        game_back._grid[15][40] = Fore.RED  + 'G'
        game_back._grid[15][41] = Fore.RED  + 'A'
        game_back._grid[15][42] = Fore.RED  + 'M'
        game_back._grid[15][43] = Fore.RED  + 'E'
        game_back._grid[15][46] = Fore.RED  + 'O'
        game_back._grid[15][47] = Fore.RED  + 'V'
        game_back._grid[15][48] = Fore.RED  + 'E'
        game_back._grid[15][49] = Fore.RED  + 'R'

        output_strr = ""
        for row in range(rows):
            for col in range(columns):
                    output_strr += game_back.get_grid(row,col)
            output_strr += '\n'
        print('\033[H' + output_strr)
        
#collison of brick with ball
def coll_brick():
    for k in range(30):
        newbr = b1[k]
        xstart = newbr._xpos
        xend = newbr._xpos + newbr._thick 
        ystart = newbr._ypos
        yend = newbr._ypos + newbr._len 
        if(newbr._level == 0):
            newbr._visible = 0
        # print(xcoords)
        if(newbr._level > 0):
            if(xcoords[0] > xcoords[1]):
                if(xcoords[1] == xend):
                        if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._xvel *= -1
                                newbr._level -= 1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
                if(xcoords[1] == xstart):
                        if(ycoords[1] == ystart or ycoords[1] == yend):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._yvel *= -1
                                newbr._level -= 1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
            else:
                if(xcoords[1] == xstart):
                    if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                        config.score += 10
                        # print(config.score)
                        if(config.flag_tb == 0):
                            game_ball._xvel *= -1
                            newbr._level -= 1
                        else:
                            newbr._level = 0
                            newbr._visible = 0
                if(xcoords[1] == xend):
                        if(ycoords[1] == ystart or ycoords[1] == yend):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._yvel *= -1
                                newbr._level -= 1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
    
    for k in range(3):
        newbr = b4[k]
        xstart = newbr._xpos
        xend = newbr._xpos + newbr._thick 
        ystart = newbr._ypos
        yend = newbr._ypos + newbr._len 
        if(newbr._level > 0):
            if(xcoords[0] > xcoords[1]):
                if(xcoords[1] == xend):
                    if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                        config.score += 10
                        # print(config.score)
                        if(config.flag_tb == 0):
                            game_ball._xvel *= -1
                        else:
                            newbr._level = 0
                            newbr._visible = 0
                if(xcoords[1] == xstart):
                    if(ycoords[1] == ystart or ycoords[1] == yend):
                        config.score += 10
                        # print(config.score)
                        if(config.flag_tb == 0):
                            game_ball._yvel *= -1
                        else:
                            newbr._level = 0
                            newbr._visible = 0
            else:
                if(xcoords[0] > xcoords[1]):
                    if(xcoords[1] == xstart):
                        if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._xvel *= -1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
                    if(xcoords[1] == xend):
                        if(ycoords[1] == ystart or ycoords[1] == yend):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._yvel *= -1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
                    
                

#collision for explosive bricks
def coll_explosive():
    for k in range(6):
        newbr = bombs[k]
        xstart = newbr._xpos
        xend = newbr._xpos + newbr._thick 
        ystart = newbr._ypos
        yend = newbr._ypos + newbr._len 
        
        if(newbr._level == 0):
            newbr._visible = 0
            for i in range(30):
                topleftx = b1[i]._xpos
                toplefty = b1[i]._ypos
                bottomleftx = b1[i]._xpos + b1[i]._thick 
                bottomlefty = b1[i]._ypos 
                toprightx = b1[i]._xpos
                toprighty = b1[i]._ypos + b1[i]._len
                bottomrightx = b1[i]._xpos + b1[i]._thick
                bottomrighty = b1[i]._ypos + b1[i]._len

                if(xstart == bottomleftx):
                    if(ystart >= bottomlefty and ystart <= bottomrighty):
                        b1[i]._level = 0
                        b1[i]._visible = 0
                    if(yend >= bottomlefty and yend <= bottomrighty):
                        b1[i]._visible = 0
                        b1[i]._level = 0
                if(xend == topleftx):
                    if(ystart >= bottomlefty and ystart <= bottomrighty):
                        b1[i]._visible = 0
                        b1[i]._level = 0
                    if(yend >= bottomlefty and yend <= bottomrighty):
                        b1[i]._visible = 0
                        b1[i]._level = 0
                if(ystart == toprighty):
                    if(xstart == topleftx):
                        b1[i]._visible = 0
                        b1[i]._level = 0
                if(yend == toplefty):
                    if(xstart == topleftx):
                        b1[i]._visible = 0
                        b1[i]._level = 0
            
            for i in range(3):
                topleftx = b4[i]._xpos
                toplefty = b4[i]._ypos
                bottomleftx = b4[i]._xpos + b1[i]._thick 
                bottomlefty = b4[i]._ypos 
                toprightx = b4[i]._xpos
                toprighty = b4[i]._ypos + b1[i]._len
                bottomrightx = b4[i]._xpos + b1[i]._thick
                bottomrighty = b4[i]._ypos + b1[i]._len

                if(xstart == bottomleftx):
                    if(ystart >= bottomlefty and ystart <= bottomrighty):
                        b4[i]._level = 0
                        b4[i]._visible = 0
                    if(yend >= bottomlefty and yend <= bottomrighty):
                        b4[i]._visible = 0
                        b4[i]._level = 0
                if(xend == topleftx):
                    if(ystart >= bottomlefty and ystart <= bottomrighty):
                        b4[i]._visible = 0
                        b4[i]._level = 0
                    if(yend >= bottomlefty and yend <= bottomrighty):
                        b4[i]._visible = 0
                        b4[i]._level = 0
                if(ystart == toprighty):
                    if(xstart == topleftx):
                        b4[i]._visible = 0
                        b4[i]._level = 0
                if(yend == toplefty):
                    if(xstart == topleftx):
                        b4[i]._visible = 0
                        b4[i]._level = 0
            if(k == 5):
                bombs[k-1]._level = 0
            elif(k==0):
                bombs[k+1]._level = 0
            else:
                bombs[k+1]._level = 0
                bombs[k-1]._level = 0

        
            

        if(newbr._level > 0):
            if(xcoords[0] > xcoords[1]):
                if(xcoords[1] == xend):
                        if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._xvel *= -1
                                newbr._level -= 1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
                if(xcoords[1] == xstart):
                        if(ycoords[1] == ystart or ycoords[1] == yend):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._yvel *= -1
                                newbr._level -= 1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
            else:
                if(xcoords[1] == xstart):
                    if(yend >= ycoords[1] and  ystart <= ycoords[1]):
                        config.score += 10
                        # print(config.score)
                        if(config.flag_tb == 0):
                            game_ball._xvel *= -1
                            newbr._level -= 1
                        else:
                            newbr._level = 0
                            newbr._visible = 0
                if(xcoords[1] == xend):
                        if(ycoords[1] == ystart or ycoords[1] == yend):
                            config.score += 10
                            # print(config.score)
                            if(config.flag_tb == 0):
                                game_ball._yvel *= -1
                                newbr._level -= 1
                            else:
                                newbr._level = 0
                                newbr._visible = 0
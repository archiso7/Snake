# python imports
from pynput import keyboard
import time
import sys

# file imports
from vars import *

global snake_rotation
global snake_position
global snake_len
global screen

snake_rotation = 8
snake_position = [[round(height/2), round(width/2)], [round(height/2)+1, round(width/2)]]
snake_len = 2
screen = []

# check for keypresses
def background():
    with keyboard.Listener(
        on_press=on_press) as listener: # start the keyboard listener
            listener.join()

# the forground thread
def foreground():
    game_space()
    while True:
        time.sleep(0.5)
        Update()

def Update():
    move_snake(snake_rotation)

    display()

def move_snake(dir):
    global screen
    inc = 1
    index = 1
    rindex = 0
    screen[snake_position[1][0]][snake_position[1][1]] = screen[snake_position[1][0]][snake_position[1][1]].replace('\033[0;32;42m', '')
    snake_position.pop(-1)
    if dir in [4, 8]:
        inc = -1
    if dir in [2, 8]:
        index = 0
        rindex = 1
    snake_position.insert(0, [snake_position[0][index]+inc])
    snake_position[0].insert(rindex, snake_position[-1][rindex])
    gen_snake()

# generate the box for the game to be played in
def game_space():
    global screen
    screen = [[' ' for i in range(width-2)] for i in range(height-2)]
    top_line = ['\u2500' for i in range(width-2)]
    bottom_line = ['\u2500' for i in range(width-2)]
    main_line = [' ' for i in range(width-2)]
    top_line.insert(0, '\u250c')    #
    bottom_line.insert(0, '\u2514') # add the first character to each line
    main_line.insert(0, '\u2502')   #
    top_line.append('\u2510')    #
    bottom_line.append('\u2518') # add the last character to each line
    for i in screen:
        i.insert(0, '\u2502')
        i.append('\u2502')
    screen.insert(0, top_line) # add the top line to the start of screen
    screen.append(bottom_line) # add the bottom line to the screen
    gen_snake()
    display()

# create the snake on top of the game space
def gen_snake():
    global screen
    for i in range(len(snake_position)):
        screen[snake_position[i][0]][snake_position[i][1]] = '\033[0;32;42m' + screen[snake_position[i][0]][snake_position[i][1]].replace('\033[0;37;40m', '') # highlight the character in the screen array
        screen[snake_position[i][0]][snake_position[i][1]+1] = '\033[0;37;40m' + screen[snake_position[i][0]][snake_position[i][1]+1].replace('\033[0;37;40m', '') # make sure the lines after it are not highlighted

# print everything
def display():
    global screen
    ts = ''
    for i in screen:
        for n in i:
            ts += n
        ts += '\n'
    print('\033[2J' + '\033[0;0H' + ts)

# what to do when a key is pressed
def on_press(key):
    global snake_rotation
    try:
        if key.char in ['w', 'a', 's', 'd', 'Key.up', 'Key.left', 'Key.down', 'Key.right']:
            if key.char in ['w', 'up']:
                snake_rotation = 8
            elif key.char in ['a', 'left']:
                snake_rotation = 4
            elif key.char in ['s', 'down']:
                snake_rotation = 2
            elif key.char in ['d', 'right']:
                snake_rotation = 6
    except:
        pass
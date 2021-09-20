# python imports
from pynput import keyboard

# file imports
from vars import *

# check for keypresses
def background():
    with keyboard.Listener(
        on_press=on_press) as listener: # start the keyboard listener
            listener.join()

# the forground thread
def foreground():
    game_space()

# generate the box for the game to be played in
def game_space():
    top_line = ['\u2500' for i in range(width-2)]
    bottom_line = ['\u2500' for i in range(width-2)]
    main_line = [' ' for i in range(width-2)]
    top_line.insert(0, '\u250c')    #
    bottom_line.insert(0, '\u2514') # add the first character to each line
    main_line.insert(0, '\u2502')   #
    top_line.append('\u2510')    #
    bottom_line.append('\u2518') # add the last character to each line
    main_line.append('\u2502')   #
    screen = [main_line for i in range(height-2)]
    screen.insert(0, top_line) # add the top line to the start of screen
    screen.append(bottom_line) # add the bottom line to the screen
    print(screen)
    gen_snake()
    display()

# create the snake on top of the game space
def gen_snake():
    screen[1][1] = '\033[0;32;42m ' # highlight the character at 9,29W in the screen array
    screen[1][1] = '\033[0;37;40m ' # make sure the lines after it are not highlighted

# print everything
def display():
    ts = ''
    for i in screen: # loop through every row in the array
        for s in i:  # loop through all charatcers in the array
            ts += s
        ts += '\n'
    print(ts)

# what to do when a key is pressed
def on_press(key):
    pass
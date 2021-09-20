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
    display(gen_snake(screen))

# create the snake on top of the game space
def gen_snake(screen):
    print(screen)
    screen[round(height/2)][round(width/2)] = '\033[0;32;42m ' # highlight the character at 9,29W in the screen array
    screen[round(height/2)][round(width/2)+1] = '\033[0;37;40m ' # make sure the lines after it are not highlighted
    return(screen)

# print everything
def display(screen):
    ts = ''
    for i in screen:
        for n in i:
            ts += n
        ts += '\n'
    print(ts)

# what to do when a key is pressed
def on_press(key):
    exit()
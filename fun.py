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
    for i in range(width - 2): # gen one of each of the base lines
        top_line.append('\u2500')
        bottom_line.append('\u2500')
        main_line.append(' ')
    top_line.append('\u2510')    #
    bottom_line.append('\u2518') # add the last character to each line
    main_line.append('\u2502')   #
    screen.append(top_line) # appened the top line to the screen
    for i in range(height - 2): # add a lot of the main line to the screen
        screen.append(main_line)
    screen.append(bottom_line) # add the bottom line to the screen
    gen_snake()
    display()

# create the snake on top of the game space
def gen_snake():
    print("hhhhh")
    screen[round(height/2)][round(width/2)] = '\033[0;32;42m ' # highlight the character at 9,29W in the screen array
    screen[round(height/2)][round(width/2)+1] = '\033[0;37;40m ' # make sure the lines after it are not highlighted

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
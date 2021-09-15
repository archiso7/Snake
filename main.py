# python imports
import threading

# file imports
from fun import *

# create the treads to allow for the keycheck to run in the background
b = threading.Thread(name='background', target=background)
f = threading.Thread(name='foreground', target=foreground)

# start the threads
b.start()
f.start()
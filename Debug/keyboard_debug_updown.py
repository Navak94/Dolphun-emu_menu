from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()
x = 0
# Press and release space
for x in range(0,4000):
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    
    # Type a lower case A; this will work even if no key on the
    # physical keyboard is labelled 'A'
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    sleep(1)

# Type two upper case As

with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')

# Type 'Hello World' using the shortcut type method
keyboard.type('Hello World')
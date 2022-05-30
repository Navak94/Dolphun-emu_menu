from __future__ import print_function
import os
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import filedialog
from inputs import get_gamepad
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
from time import sleep
import sys
from subprocess import call
x = 0
y = 0
menu_item_select_num = 0
NumberOfGames = 0
instance = 0
analog_info=""
menu_info =""
selected_game=""
x_pos = 640
y_pos = 480

joystick_logic = []
top = Tk()
keyboard = Controller()

# Define the size of the window.
top.geometry("640x480")

img  = Image.open("/home/nhindman/Desktop/Roms/GameCube.jpg") 
photo=ImageTk.PhotoImage(img)
lab=Label(image=photo).place(x=0,y=0)
    
# create Listbox  
gamesListBox=Listbox(top, height = 30, 
                  width = 45, 
                  bg = "grey",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "yellow")

gamesListBox.place(x=50,y=150)
gamesList = []
directory =  "/home/nhindman/Desktop/Roms/GC"

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.iso'):
            gamesList.append(file)
                

for x in range(0,len(gamesList)):
    gamesListBox.insert(x+1, gamesList[x])
    

def selected_item(y):
    
    selected_game = str(gamesListBox.get(y))
    print(selected_game)
    return selected_game

def start_dolphin_emu(instance, selected_game):
    if instance == 1:
        print("only launch once")
#         call("dolphin-emu -e "+ "/home/nhindman/Desktop/Roms/GC/"+""+selected_game+"", shell=True)
        call("cd /home/nhindman/Desktop/Roms/GC/",shell=True)
        call("pwd", shell = True)
        print("dolphin-emu -e" + f""""{selected_game}" """ )
        call("dolphin-emu -e " + f""""{selected_game}" """ , shell=True)
    if instance > 1:
        print("oh hell naw")
    return instance

gamesListBox.activate(5)
gamesListBox.get(0)
gamesListBox.focus_set()
for x in range (0,20):
    top.update()
    keyboard.press(Key.up)
    gamesListBox.focus_set()
while 1:
    top.update()
    events = get_gamepad()
    mouse.position = (x_pos, y_pos)

    for event in events:

        analog_info = str(event.code)
        analog_info= analog_info.replace("ABS_","").replace("SYN_REPORT0","")
        analogState = str(event.state)
        menu_info = analog_info + analogState
        menu_info= menu_info.replace("SYN_REPORT0","")
        if "Y" in menu_info:
            if "255" in menu_info:
                y =  1
            if "127" in menu_info:
                y = 0           
            joystick_logic.append(str(y))
            
            if len(joystick_logic) == 2: 
                if joystick_logic[0] == "1" and joystick_logic[1] =="0":
                    #print("increment")
                    keyboard.press(Key.down)
                    menu_item_select_num = menu_item_select_num + 1
                    if menu_item_select_num > (len(gamesList)-1):
                       menu_item_select_num = len(gamesList)-1
                       gamesListBox.focus_set()
                       

                    
                if joystick_logic[0] == "0" and joystick_logic[1] =="0":
                    #print("de-increment")
                    keyboard.press(Key.up)
                    menu_item_select_num = menu_item_select_num - 1
                    if(menu_item_select_num < 0):
                        menu_item_select_num = 0
                        gamesListBox.focus_set()
                joystick_logic.clear()
            keyboard.release(Key.up)
            keyboard.release(Key.down)
            if str(selected_item(menu_item_select_num)) != "None":
                selected_game = str(selected_item(menu_item_select_num))
        
        if "BTN_BASE4" in menu_info:
            print("selected ===>" + selected_game)
            instance = instance +1
            start_dolphin_emu(instance, selected_game)
            
  

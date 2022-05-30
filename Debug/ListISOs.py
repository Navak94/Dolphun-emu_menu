import os
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import filedialog


top = Tk()
  
# create listbox object
  
# Define the size of the window.
top.geometry("640x480")

img  = Image.open("/home/nhindman/Desktop/Roms/GameCube.jpg") 
photo=ImageTk.PhotoImage(img)
lab=Label(image=photo).place(x=0,y=0)
    
# Define a label for the list.  
label = Label(top, text = " FOOD ITEMS") 
gamesListBox=Listbox(top, height = 50, 
                  width = 45, 
                  bg = "grey",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "yellow")
#gamesListBox.get(gamesList)
gamesListBox.place(x=50,y=150)

gamesList = []

directory =  "/home/nhindman/Desktop/Roms/GC"
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.iso'):
            gamesList.append(file)
                

for x in range(0,len(gamesList)):
    gamesListBox.insert(x+1, gamesList[x])
    

def selected_item():
     
    # Traverse the tuple returned by
    # curselection method and print
    # corresponding value(s) in the listbox
    for i in gamesListBox.curselection():
        print(gamesListBox.get(i))
#btn = Button(top, text='Print Selected', command=selected_item)
#btn.place(x=50,y=350)
from tkinter import *
import tkinter as tk
from tkinter import Menu
root = Tk()

root.geometry("500x500")
root.title("A simple menu bar")
menubar=Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar)
filemenu.add_command(label= "new",command = lambda:print("New file") )
filemenu.add_command(label= "open",command = lambda:print("Open file"))
filemenu.add_command(label= "save",command = lambda:print("Save file"))
filemenu.add_separator()
filemenu.add_command(label= "exit",command = root.quit)
menubar.add_cascade(label="file",menu = filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label= "cut",command = lambda:print("You have pressed cut"))
editmenu.add_command(label= "copy",command = lambda:print("You have pressed copy"))
editmenu.add_command(label= "paste",command = lambda:print("You have pressed paste"))
editmenu.add_separator()
editmenu.add_command(label= "undo",command = lambda:print("You have pressed undo"))
editmenu.add_command(label= "redo",command = lambda:print("You have pressed redo"))
menubar.add_cascade(label="Edit",menu = editmenu)



root.mainloop()
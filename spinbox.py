from tkinter import *
import tkinter as tk
root = Tk()

root.geometry("500x500")
root.title("Spinbox")

spinbox = Spinbox(root,from_=0,to_=10,increment = 1)
spinbox.pack(pady = 2)

spinbox2 = Spinbox(root,values = ("cat","dog","fish","hamster","rabbit"))
spinbox2.pack(pady = 10)

spinbox3 = Spinbox(root,from_=0.5,to_=10,increment = 0.5)
spinbox3.pack(pady = 10)


root.mainloop()
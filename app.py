import tkinter
from tkinter import *
import tkinter.messagebox

top = tkinter.Tk()

def helloCallBack():
   tkinter.messagebox.showinfo( "Hello Python", "Hello World")

top.title("Tkinter Application")
a = Label(top, text="Hello, world!")
B = tkinter.Button(top, text ="Hello", command = helloCallBack)
top.geometry('350x200')

a.pack()
B.pack()
top.mainloop()
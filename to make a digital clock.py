from tkinter import *
#from tkinter.ttk import *
from time import strftime
root=Tk()
root.title("Clock")
def time():
    string=strftime("%a %d-%m-%Y %H:%M:%S %p")
    L1.config(text=string)
    L1.after(1000,time)
L1=Label(root,font=("ds-digital",50),background="black",
            foreground="cyan")
L1.pack(anchor="center")
time()

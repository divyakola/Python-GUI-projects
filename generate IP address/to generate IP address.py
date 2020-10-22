import socket
from tkinter import *
import pyperclip
top=Tk()
top.geometry("400x200")
top.title("Ip Generator App")
top.iconbitmap('ip_address.ico')
ipgen=StringVar()
def ipgenerate():
    hostname=socket.gethostname()
    ip_address=socket.gethostbyname(hostname)
    ipgen.set(ip_address)
def copyip():
    ip_add=ipgen.get()
    pyperclip.copy(ip_add)

Label(top,text="Ip Generator App",font="calibri 20 bold").pack()
Button(top,text="Generate your Ip",command=ipgenerate).pack(pady=7)
Entry(top,textvariable=ipgen).pack(pady=3)
Button(top,text="Copy Ip Address",command=copyip).pack()

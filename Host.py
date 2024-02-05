# pip install pyperclip

import pyperclip # for copy paste clipboard functions
import tkinter as tk
from tkinter import ttk
import socket

window = tk.Tk()

window.title("Get your host")
window.geometry("200x150")
window.eval('tk::PlaceWindow . center')
#window.configure(background="white")
window.resizable(False, False) 

Hostname = socket.gethostname() 
HOST = socket.gethostbyname(socket.gethostname())

# function to copy text to clipboard
def copy_text():
        pyperclip.copy(Hostname + " : " + HOST)

# label displays info
info_label = ttk.Label(window, text="Your host:",
        font=("Arial bold", 11), relief="groove", padding=5)
info_label.pack()

# label displays host number
host_label = ttk.Label(window, state=tk.DISABLED, text="Number: " + HOST,
        font=("Arial bold", 12), padding=5)
host_label.pack()

# label displays host name
hostname_label = ttk.Label(window, state=tk.DISABLED, text="Name: " + Hostname,
        font=("Arial bold", 12), padding=5)
hostname_label.pack()

#button allows to copy host number & name into clipboard 
copy_button = tk.Button(window, text= "Copy", command=copy_text)
copy_button.pack()


window.mainloop()

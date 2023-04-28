import time
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import subprocess, threading, requests
from tkinter import messagebox
root = tk.Tk()
root.title = "Installer"

root.geometry("500x500")

progress = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
def startwarn():
    a = messagebox.showwarning("TOS ! READ !", "the program you are about to install and execute is MALWARE, by pressing ok, you confirm that you are aware of the risk and dangers of installing a malicious program \n and release the creator of this program from any liability (to deny this, and cancel instalation please press 'cancel') \nI hope you enjoy!", type="okcancel")
    if a == "ok":
        return 1
    if a == "cancel":    
        return 0
    
startbtn = Button(root, text="Download & Install", command=lambda: startwarn())

def load():

    progress['value'] = 0
    root.update_idletasks()

threading.Thread(target=load()).start
progress.pack()
startbtn.pack()
startbtn.place(relx=0.5, rely=0.5, anchor=CENTER)
#startbtn.place((500, 500))
root.mainloop()

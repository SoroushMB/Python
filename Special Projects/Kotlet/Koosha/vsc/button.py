import os
import tkinter
from tkinter import *
def changeBg():
   c=clr_entry.get()
   root.config(bg=c)
   r.config(text="change color", bg=c)
os.system("cls")

root=Tk()
root.geometry("300x200+500+250")
root.config(bg="purple")
clr_lbl=Label(root,text="Color: ", fg="blue")
clr_lbl.pack()

clr_entry=Entry(root)
clr_entry.pack()

btn=Button(root, text="Submit and change", bg="cyan" , command=changeBg)
btn.pack()

r=Label(root,text="", bg="yellow")
r.pack()
root.mainloop()
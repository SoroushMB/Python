import os
import tkinter
from tkinter import *
def welcome():
   c=clr_entry.get()
   r.config(text=("welcome",c))

   g=dov.get()
   if g=="":
    d.config(text="Please enter your age")
   elif g<"18":
    d.config(text="you're a kid")
   elif g>="18":
    d.config(text="you're an adult")
os.system("cls")

root=Tk()
root.geometry("500x500")
clr_lbl=Label(root,text="Name:", fg="red")
clr_lbl.pack()

clr_entry=Entry(root)
clr_entry.pack()


r=Label(root,text="", fg="red")
r.pack()
###########################################################
f=Label(root,text="Enter your age:", fg="blue")
f.pack()

dov=Entry(root)
dov.pack()

d=Label(root,text="", fg="red")
d.pack()

btn=Button(root, text="send", bg="white" , command=welcome)
btn.pack()

root.mainloop()
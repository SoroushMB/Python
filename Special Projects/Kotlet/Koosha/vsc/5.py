from tkinter import Tk,Button,Label,Entry
import os
os.system("cls")
root=Tk()
root.geometry('400x300')
root.title("Greeting.exe")
root['bg']="white"

entry1=Entry(root,width=35)
def greeting():
   username=entry1.get()
   greeting=f"hello,{username}"
   eera= Label (root,text=greeting,font=("Arial",10))
   eera.pack()

button1=Button(root,text="press to reveal",width=15,height=5,font="Arial",command=lambda:greeting())

entry1.pack()
button1.pack()
root.mainloop()
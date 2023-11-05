from turtle import forward,left,right,back,circle,up,down
from tkinter import Label,LabelFrame,Entry,Button,Tk,Toplevel
root= Tk()
root.title("HOW!?")
def help():
    a=int(an.get())
    circle(a)
an=Entry(root)   
an.grid(row=1,column=1) 
btn=Button(root,text="Hekp",command=lambda:help())
btn.grid(row=0,column=0)
root.mainloop()
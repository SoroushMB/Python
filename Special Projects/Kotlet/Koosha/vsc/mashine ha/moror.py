from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
roam= Tk()
roam.geometry("300x200")
a=()
def komak():
    global a
    c=str(combany.get())
    if c=="":
        lblerr.config(text="please select something!")
    else:
     lblerr.config(text="")
     if c=="toyota":
        a=("supra",)
        modal.config(values=("supra mk4","landcruise","supra mk5"))
        a=("supra","landcruise")
     elif c=="bmw":
        modal.config(values=("m5 e60","m5 cs","m5 f90"))
     elif c=="benz":
        modal.config(values=("c69","c63","AMG GT"))
def GHASEM():
    hola=Toplevel()
    g=str(modal.get())
    if g=="c69":
     openimg=Image.open("mashina ha/21.jpg") 
    elif g=="c63":
    
    elif g=="AMG GT":
    
    elif g=="m5 e60":
    
    elif g=="m5 f90":
    
    elif g=="m5 cs":
    
    elif g=="supra mk4":
    
    elif g=="supra mk5":
    
    elif g=="landcruise":
lblerr=Label(roam,text="",fg="Red")
lbl_company=Label(roam,text="slp?")
combany=ttk.Combobox(roam,values=("bmw","benz","toyota"))
updatebtn=Button(roam,text="update",command=lambda:komak())
modal=ttk.Combobox(roam,values=a)
submit=Button(roam,text="sumbit",bg="grey",command=lambda:GHASEM())

submit.grid(row=3,column=0,sticky="news",columnspan=3)
lblerr.grid(row=2,column=1,sticky="news",columnspan=2)
lbl_company.grid(row=0,column=0)
combany.grid(row=0,column=1)
modal.grid(row=1,column=1)
updatebtn.grid(row=0,column=2)


roam.mainloop()
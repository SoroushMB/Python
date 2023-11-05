# Intro of Tkinter
from tkinter import Tk,Label,Button,Entry,Spinbox,IntVar,StringVar,BooleanVar,DoubleVar,Frame,LabelFrame,Toplevel,Checkbutton,Radiobutton
from tkinter.ttk import Combobox

hamintori = {
    "font" : ("Product Sans Medium",20),
    "width" : 10,
    "height" : 10
}
root = Tk()
# root.geometry("400x680+100+100")
root.title("Jasem&Ghasem")
root.config(bg="green")

name1 = Label(master=root,text="Hello, World!",cnf=hamintori,bg="darkred",fg="white")
name2 = Label(master=root,text="Hello, World!",cnf=hamintori,bg="white",fg="black")
name3 = Label(master=root,text="Hello, World!",cnf=hamintori,bg="darkgreen",fg="white")

name1.grid(row=0,column=0)
name2.grid(row=0,column=1)
name3.grid(row=0,column=2)

root.mainloop()
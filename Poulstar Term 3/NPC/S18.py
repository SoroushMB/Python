# bind , unbind , delete , insert , cnf
from turtle import fd,lt,rt,pensize,pencolor,done,speed,circle
from tkinter import Label,Tk,Entry,Button
from tkinter.ttk import Combobox

# Shapes : Hexagon - Square - Triangle - Rectangle - Circle
def shapes(shape):
    size = ...
    if shape == "Hexagon":
        for _ in range(6):
            fd(size)
            lt(60)
    elif shape == "Square":
        for _ in range(4):
            fd(size)
            lt(90)
    elif shape == "Triangle":
        for _ in range(3):
            fd(size)
            lt(120)
    elif shape == "Rectangle":
        for _ in range(2):
            fd(size)
            lt(90)
            fd(size/2)
            lt(90)
    elif shape == "Circle":
        circle(radius=size)
# 3 Label - 1 Combobox - 1 Spinbox - 1 Entry
lbls_cnf = {
    "bg" : "#2a9d8f",
    "fg" : "#264653",
    "font" : ("Gotham-Medium",18),
    "relief" : "raised",
    "border" : 20
}
root = Tk()
shape_lbl = Label(master=root,text="Shape : ",cnf=lbls_cnf)
color_lbl = Label(master=root,text="Color : ",cnf=lbls_cnf)
size_lbl = Label(master=root,text="Size : ",cnf=lbls_cnf)

shape_lbl.grid(row=0,column=0,sticky="nsew")
color_lbl.grid(row=1,column=0,sticky="nsew")
size_lbl.grid(row=2,column=0,sticky="nsew")
root.mainloop()
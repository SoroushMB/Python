from tkinter import Tk,Button,Entry,Toplevel,Label
from tkinter.ttk import Checkbutton
from turtle import fd,rt,circle,pencolor,bgcolor,pensize,shape

def Square():
    global e1,e2
    Size = int(e1.get())
    for i in range(4):
        fd(Size)
        rt(90)

def Rectangle():
    global e1,e2
    SizeW = int(e1.get())
    SizeL = int(e2.get())
    for i in range(2):
        fd(SizeW)
        rt(90)
        fd(SizeL)
        rt(90)

def Triangle():
    global e1,e2
    Size = int(e1.get())
    for i in range(3):
        fd(Size)
        rt(120)

def CircleExtra():
    global e1,e2
    Size = int(e1.get())
    circle(radius=Size)

def SecondPG():
    pensize(int(PenSizeEntry.get()))
    pencolor(PenColorEntry.get())
    shape(ShapeOfTurtleEntry.get())
    bgcolor(BackgroundEntry.get())
    
    global e1,e2
    root = Toplevel()
    root.title("Shapes")
    b1 = Button(master=root,text=" Square ",cnf=ConfigurationsBTN,command=Square)
    b2 = Button(master=root,text=" Rectangle ",cnf=ConfigurationsBTN,command=Rectangle)
    b3 = Button(master=root,text=" Triangle ",cnf=ConfigurationsBTN,command=Triangle)
    b4 = Button(master=root,text=" Circle ",cnf=ConfigurationsBTN,command=CircleExtra)

    e1 = Entry(master=root,cnf=ConfigurationsENT)
    e2 = Entry(master=root,cnf=ConfigurationsENT)

    b1.grid(row=0,column=0,sticky="nsew")
    b2.grid(row=1,column=0,sticky="nsew")
    b3.grid(row=2,column=0,sticky="nsew")
    b4.grid(row=3,column=0,sticky="nsew")

    e1.grid(row=0,column=1,rowspan=2,sticky="nsew")
    e2.grid(row=2,column=1,rowspan=2,sticky="nsew")
    root.mainloop()

ConfigurationsLBL = {
    "padx" : 26,
    "pady" : 13,
    "bg" : "#0d1321",
    "fg" : "#f0ebd8",
    "font" : ("JetBrains Mono",15),
    "relief" : "raised",
    "border" : 20
}
ConfigurationsBTN = {
    "padx" : 26,
    "pady" : 13,
    "bg" : "#0d1321",
    "fg" : "#f0ebd8",
    "font" : ("JetBrains Mono",15),
    "relief" : "raised",
    "border" : 20
}
ConfigurationsENT = {
    "bg" : "#1d2d44",
    "fg" : "#f0ebd8",
    "font" : ("JetBrains Mono",20),
    "relief" : "sunken",
    "border" : 20,
    "justify" : "center"
}

main_page = Tk()
main_page.title("Settings")

PenSizeLabel = Label(master=main_page,text="Pen Size :",cnf=ConfigurationsLBL)
PenColorLabel = Label(master=main_page,text="Pen Color :",cnf=ConfigurationsLBL)
ShapeOfTurtleLabel = Label(master=main_page,text="Shape :",cnf=ConfigurationsLBL)
BackgroundLabel = Label(master=main_page,text="Background Color :",cnf=ConfigurationsLBL)

PenSizeEntry = Entry(master=main_page,cnf=ConfigurationsENT)
PenColorEntry = Entry(master=main_page,cnf=ConfigurationsENT)
ShapeOfTurtleEntry = Entry(master=main_page,cnf=ConfigurationsENT)
BackgroundEntry = Entry(master=main_page,cnf=ConfigurationsENT)

drawer_btn = Button(master=main_page,text="Press to draw!",cnf=ConfigurationsBTN,command=SecondPG)

PenSizeLabel.grid(row=0,column=0,sticky="nsew")
PenColorLabel.grid(row=1,column=0,sticky="nsew")
ShapeOfTurtleLabel.grid(row=2,column=0,sticky="nsew")
BackgroundLabel.grid(row=3,column=0,sticky="nsew")

PenSizeEntry.grid(row=0,column=1,sticky="nsew")
PenColorEntry.grid(row=1,column=1,sticky="nsew")
ShapeOfTurtleEntry.grid(row=2,column=1,sticky="nsew")
BackgroundEntry.grid(row=3,column=1,sticky="nsew")

drawer_btn.grid(row=4,column=0,columnspan=2,sticky="nsew")

main_page.mainloop()
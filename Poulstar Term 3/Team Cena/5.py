from tkinter import Tk,Button,Entry,Toplevel,Label,PhotoImage,BooleanVar
from tkinter.ttk import Checkbutton
from turtle import fd,rt,circle,pencolor,bgcolor,pensize,shape
from tkinter.messagebox import showerror

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

def ThemeSelector():
    global ButtonIO
    if ButtonIO.get() == True:
        bgcolor("Black")
    else:
        bgcolor("White")

def SpecialShapeDrawer():
    global DistrictsCountEntry,ColorOfShapeEntry,PenSizEntry
    DistrictsCountEntryResult = int(DistrictsCountEntry.get())
    ColorOfShapeEntryResult = ColorOfShapeEntry.get()
    PenSizEntryResult = int(PenSizEntry.get())

    pencolor(ColorOfShapeEntryResult)
    pensize(PenSizEntryResult)
    for i in range(DistrictsCountEntryResult):
        fd(100)
        rt(360/DistrictsCountEntryResult)

def SpecialShape():
    global DistrictsCountEntry,ColorOfShapeEntry,PenSizEntry,ButtonIO,SpecialShapeWindow
    MainPG.iconify()
    SpecialShapeWindow = Toplevel()
    SpecialShapeWindow.title("Special Shape")
    SpecialShapeIcon = PhotoImage(file="spongebob.png")
    SpecialShapeWindow.iconphoto(False,SpecialShapeIcon)

    ButtonIO = BooleanVar()

    DistrictsCountLabel = Label(master=SpecialShapeWindow,text="Districts Count : ",cnf=ConfigurationsLBL)
    ColorOfShapeLabel = Label(master=SpecialShapeWindow,text="Color Of Shape : ",cnf=ConfigurationsLBL)
    PenSizLabel = Label(master=SpecialShapeWindow,text="Pensize : ",cnf=ConfigurationsLBL)

    DistrictsCountEntry = Entry(master=SpecialShapeWindow,cnf=ConfigurationsENT)
    ColorOfShapeEntry = Entry(master=SpecialShapeWindow,cnf=ConfigurationsENT)
    PenSizEntry = Entry(master=SpecialShapeWindow,cnf=ConfigurationsENT)

    SpecialShapeButton = Button(master=SpecialShapeWindow,text="Press to draw!",cnf=ConfigurationsBTN,command=SpecialShapeDrawer)
    ThemeButton = Checkbutton(master=SpecialShapeWindow,text="Dark | Light!",onvalue=True,offvalue=False,variable=ButtonIO,command=ThemeSelector)

    DistrictsCountLabel.grid(row=0,column=0,sticky="nsew")
    ColorOfShapeLabel.grid(row=1,column=0,sticky="nsew")
    PenSizLabel.grid(row=2,column=0,sticky="nsew")
    
    DistrictsCountEntry.grid(row=0,column=1,sticky="nsew")
    ColorOfShapeEntry.grid(row=1,column=1,sticky="nsew")
    PenSizEntry.grid(row=2,column=1,sticky="nsew")
    
    SpecialShapeButton.grid(row=3,column=0,columnspan=2,sticky="nsew")
    ThemeButton.grid(row=4,column=0,columnspan=2,sticky="nsew")
    
    SpecialShapeWindow.mainloop()

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
    try:
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
    except:
        showerror(title="Alert!",message="There is something wrong!")

MainPG = Tk()
MainPG.title("Settings")

PenSizeLabel = Label(master=MainPG,text="Pen Size :",cnf=ConfigurationsLBL)
PenColorLabel = Label(master=MainPG,text="Pen Color :",cnf=ConfigurationsLBL)
ShapeOfTurtleLabel = Label(master=MainPG,text="Shape :",cnf=ConfigurationsLBL)
BackgroundLabel = Label(master=MainPG,text="Background Color :",cnf=ConfigurationsLBL)

PenSizeEntry = Entry(master=MainPG,cnf=ConfigurationsENT)
PenColorEntry = Entry(master=MainPG,cnf=ConfigurationsENT)
ShapeOfTurtleEntry = Entry(master=MainPG,cnf=ConfigurationsENT)
BackgroundEntry = Entry(master=MainPG,cnf=ConfigurationsENT)

DrawerButton = Button(master=MainPG,text="Press to draw!",cnf=ConfigurationsBTN,command=SecondPG)
SpecialShapeButton = Button(master=MainPG,text="Special\nShape",cnf=ConfigurationsBTN,command=SpecialShape)
ExitButton = Button(master=MainPG,text="Exit",cnf=ConfigurationsBTN,command=lambda:MainPG.destroy())

PenSizeLabel.grid(row=0,column=0,sticky="nsew")
PenColorLabel.grid(row=1,column=0,sticky="nsew")
ShapeOfTurtleLabel.grid(row=2,column=0,sticky="nsew")
BackgroundLabel.grid(row=3,column=0,sticky="nsew")

PenSizeEntry.grid(row=0,column=1,sticky="nsew")
PenColorEntry.grid(row=1,column=1,sticky="nsew")
ShapeOfTurtleEntry.grid(row=2,column=1,sticky="nsew")
BackgroundEntry.grid(row=3,column=1,sticky="nsew")

DrawerButton.grid(row=4,column=0,columnspan=2,sticky="nsew")
SpecialShapeButton.grid(row=0,column=2,rowspan=4,sticky="nsew")
ExitButton.grid(row=4,column=2,sticky="nsew")

MainPG.mainloop()

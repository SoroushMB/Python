from tkinter import Button,Entry,Frame,Label,Toplevel,Tk,PhotoImage,Checkbutton,BooleanVar
from tkinter.ttk import Combobox,OptionMenu,Treeview,Notebook
from tkinter.messagebox import showerror,showinfo
from tkinter.filedialog import FileDialog,SaveFileDialog,LoadFileDialog
from json import load,dump
from database import Database

def ConnectingToDB():
    global IconPhoto
    HostE = HostEnt.get()
    PassE = PassEnt.get()
    UserE = UserEnt.get()
    DataE = DataEnt.get()
    FirstDB = Database(Host=HostE,Pass=PassE,User=UserE,Data=DataE)
    FirstDB.ConnectToDB()
    
    SecondPage = Toplevel()
    SecondPage.title("Library")
    SecondPage.resizable(0,0)
    SecondPage.iconphoto(False,IconPhoto)
    
    Gatherer = Notebook(master=SecondPage)
    SearchFrame = Frame(master=Gatherer,width=510,height=680)
    InsertFrame = Frame(master=Gatherer,width=510,height=680)
    DeleteFrame = Frame(master=Gatherer,width=510,height=680)
    OrderFrame = Frame(master=Gatherer,width=510,height=680)
    
    Gatherer.add(child=SearchFrame,text="Search")
    Gatherer.add(child=InsertFrame,text="Insert")
    Gatherer.add(child=DeleteFrame,text="Delete")
    Gatherer.add(child=OrderFrame,text="Order")
    
    Gatherer.pack()
    SecondPage.mainloop()

def HideAndShow():
    global ShowVar,PassEnt
    if ShowVar.get() == True:
        PassEnt.config(show="")
    elif ShowVar.get() == False:
        PassEnt.config(show="*")
        
settings = {
    "LBL":{
        "fg" : "black",
        "bg" : "#ddecef",
        "font" : ("JetBrains Mono",16),
        "relief" : "raised",
        "border" : 20,
        "anchor" : "w"
    },
    "ENT":{
        "fg" : "black",
        "bg" : "#a9c2c7",
        "font" : ("JetBrains Mono",16),
        "relief" : "raised",
        "border" : 20,
        "justify" : "center"
    },
    "BTN":{
        "fg" : "black",
        "bg" : "#7ba3bd",
        "font" : ("JetBrains Mono",16),
        "relief" : "raised",
        "border" : 20,
        "justify" : "center"
    }
}
LoginPage = Tk()
LoginPage.title(string="Connect To Database!")
LoginPage.resizable(0,0)
LoginPage.config(bg="#abd3db")
IconPhoto = PhotoImage(file="Library.png")
LoginPage.iconphoto(False,IconPhoto)

ShowVar = BooleanVar()

HostLbl = Label(master=LoginPage,text="Host Name: ",cnf=settings["LBL"])
PassLbl = Label(master=LoginPage,text="Password: ",cnf=settings["LBL"])
UserLbl = Label(master=LoginPage,text="Username: ",cnf=settings["LBL"])
DataLbl = Label(master=LoginPage,text="Database: ",cnf=settings["LBL"])

HostEnt = Entry(master=LoginPage,cnf=settings["ENT"])
PassEnt = Entry(master=LoginPage,cnf=settings["ENT"],show="*")
UserEnt = Entry(master=LoginPage,cnf=settings["ENT"])
DataEnt = Entry(master=LoginPage,cnf=settings["ENT"])

ContBTN = Button(master=LoginPage,text="Click to connect!",cnf=settings["BTN"],command=ConnectingToDB)
ShowBTN = Checkbutton(master=LoginPage,text="Click to show!",variable=ShowVar,onvalue=True,offvalue=False,cnf=settings["BTN"],command=lambda:HideAndShow())

HostLbl.grid(row=0,column=0,sticky="nsew",padx=20,pady=20)
PassLbl.grid(row=1,column=0,sticky="nsew",padx=20,pady=20)
UserLbl.grid(row=2,column=0,sticky="nsew",padx=20,pady=20)
DataLbl.grid(row=3,column=0,sticky="nsew",padx=20,pady=20)

HostEnt.grid(row=0,column=1,sticky="nsew",padx=20,pady=20)
PassEnt.grid(row=1,column=1,sticky="nsew",padx=20,pady=20)
UserEnt.grid(row=2,column=1,sticky="nsew",padx=20,pady=20)
DataEnt.grid(row=3,column=1,sticky="nsew",padx=20,pady=20)

ShowBTN.grid(row=4,column=0,columnspan=2,sticky="nsew",padx=20,pady=20)
ContBTN.grid(row=5,column=0,columnspan=2,sticky="nsew",padx=20,pady=20)

LoginPage.mainloop()
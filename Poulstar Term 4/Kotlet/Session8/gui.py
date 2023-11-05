from tkinter import Tk,Label,Button,Entry,Frame,Checkbutton,BooleanVar
from tkinter.ttk import Notebook,Combobox
from tkinter.messagebox import showinfo,showerror
import datetime
from database import Database

settings = {
    "LBL":{
        "bg": "#b392ac",
        "fg": "Black",
        "font": ("JetBrains Mono",16),
        "border": 20,
        "relief": "raised",
        "anchor": "w",
        "padx": 20,
        "pady": 20
    },
    "BTN":{
        "bg": "#f7d1cd",
        "fg": "black",
        "font": ("JetBrains Mono",16),
        "border": 20,
        "relief": "raised",
        "padx": 20,
        "pady": 20
    },
    "ENT":{
        "bg": "#d1b3c4",
        "fg": "black",
        "font": ("JetBrains Mono",16),
        "border": 20,
        "relief": "raised",
        "justify": "center"
    }
}
LogInPage = Tk()
LogInPage.title("Login Page")
LogInPage.config(bg="#735d78")

show_var = BooleanVar()

UserLbls = Label(master=LogInPage,text="Username: ",cnf=settings["LBL"])
PassLbls = Label(master=LogInPage,text="Password: ",cnf=settings["LBL"])
HostLbls = Label(master=LogInPage,text="Host Name: ",cnf=settings["LBL"])
DataLbls = Label(master=LogInPage,text="Database: ",cnf=settings["LBL"])

UserEnts = Entry(master=LogInPage,cnf=settings["ENT"])
PassEnts = Entry(master=LogInPage,cnf=settings["ENT"])
HostEnts = Entry(master=LogInPage,cnf=settings["ENT"])
DataEnts = Entry(master=LogInPage,cnf=settings["ENT"])

DataBtns = Button(master=LogInPage,text="Click to connect!",cnf=settings["BTN"])
ShowBtns = Checkbutton(master=LogInPage,text="Click to show!",cnf=settings["BTN"],onvalue=True,offvalue=False,variable=show_var)


UserLbls.grid(row=0,column=0,sticky="nsew")
PassLbls.grid(row=1,column=0,sticky="nsew")
HostLbls.grid(row=2,column=0,sticky="nsew")
DataLbls.grid(row=3,column=0,sticky="nsew")

UserEnts.grid(row=0,column=1,sticky="nsew")
PassEnts.grid(row=1,column=1,sticky="nsew")
HostEnts.grid(row=2,column=1,sticky="nsew")
DataEnts.grid(row=3,column=1,sticky="nsew")

ShowBtns.grid(row=4,column=0,columnspan=2,sticky="nsew")
DataBtns.grid(row=5,column=0,columnspan=2,sticky="nsew")
LogInPage.mainloop()
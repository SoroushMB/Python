# main.py

from database import Database
from tkinter import Tk, Label, Button, Entry


configurations = {
    "lbls" : {
        "bg" : "black",
        "fg" : "white",
        "font" : ("JetBrains Mono",16),
        "border" : 20,
        "relief" : "raised",
        "anchor" : "w"
    },
    "ents" : {
        "bg" : "white",
        "fg" : "black",
        "font" : ("JetBrains Mono",16),
        "border" : 20,
        "relief" : "sunken"
    },
    
}
root = Tk()
root.title("Connecting to database")

Database_lbl = Label(master=root,text="Database: ",cnf=configurations["lbls"])
Host_lbl = Label(master=root,text="Host: ",cnf=configurations["lbls"])
Name_lbl = Label(master=root,text="Name: ",cnf=configurations["lbls"])
Password_lbl = Label(master=root,text="Password: ",cnf=configurations["lbls"])

Database_ent = Entry(master=root,cnf=configurations["ents"])
Host_ent = Entry(master=root,cnf=configurations["ents"])
Name_ent = Entry(master=root,cnf=configurations["ents"])
Password_ent = Entry(master=root,cnf=configurations["ents"])

Database_lbl.grid(row=0,column=0,sticky="nsew")
Host_lbl.grid(row=1,column=0,sticky="nsew")
Name_lbl.grid(row=2,column=0,sticky="nsew")
Password_lbl.grid(row=3,column=0,sticky="nsew")

Database_ent.grid(row=0,column=1,sticky="nsew")
Host_ent.grid(row=1,column=1,sticky="nsew")
Name_ent.grid(row=2,column=1,sticky="nsew")
Password_ent.grid(row=3,column=1,sticky="nsew")

root.mainloop()
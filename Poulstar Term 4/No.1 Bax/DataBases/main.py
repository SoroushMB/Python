from tkinter import Tk, Label, Entry, Button

from time import sleep


configurations = {
    "lbls": {
        "bg" : "black",
        "fg" : "white",
        "font" : ("JetBrains Mono",16),
        "relief" : "raised",
        "border" : 20,
        "anchor" : "w"
    },
    "btns": {
        "bg" : "darkred",
        "fg" : "black",
        "font" : ("JetBrains Mono",16),
        "relief" : "ridge",
        "border" : 20
    },
    "ents": {
        "bg" : "gray50",
        "fg" : "black",
        "font" : ("JetBrains Mono",16),
        "relief" : "raised",
        "border" : 20
    }
}
root = Tk()
root.title("Connecting")

host_lbl = Label(master=root,text="Host: ",cnf=configurations["lbls"])
user_lbl = Label(master=root,text="User: ",cnf=configurations["lbls"])
pass_lbl = Label(master=root,text="Pswd: ",cnf=configurations["lbls"])
dbnm_lbl = Label(master=root,text="DMNM: ",cnf=configurations["lbls"])

host_ent = Entry(master=root,cnf=configurations["ents"])
user_ent = Entry(master=root,cnf=configurations["ents"])
pass_ent = Entry(master=root,cnf=configurations["ents"])
dbnm_ent = Entry(master=root,cnf=configurations["ents"])

connecting_btn = Button(master=root,text="Connect",cnf=configurations["btns"],command=connecting)
host_lbl.grid(row=0,column=0,sticky="nsew")
user_lbl.grid(row=1,column=0,sticky="nsew")
pass_lbl.grid(row=2,column=0,sticky="nsew")
dbnm_lbl.grid(row=3,column=0,sticky="nsew")
host_ent.grid(row=0,column=1,sticky="nsew")
user_ent.grid(row=1,column=1,sticky="nsew")
pass_ent.grid(row=2,column=1,sticky="nsew")
dbnm_ent.grid(row=3,column=1,sticky="nsew")
connecting_btn.grid(row=4,column=0,columnspan=2,sticky="nsew")
root.mainloop()
from tkinter import Tk,Label,Entry,Button
from tkinter.messagebox import showerror,showinfo
from database import Database


def cnt_main():
    hostname = host_ent.get()
    username = user_ent.get()
    password = pass_ent.get()
    database = data_ent.get()
    try:
        cntdb = Database(host=hostname,dbname=database,user=username,pswd=password)
        cntdb.connectToDB()
    except:
        showerror(title="Alarm!",message="The values entered are wrong!🤔")
    else:
        showinfo(title="Successful!",message="Access granted!😁")


configurations = {
    "lbls" : {
        "bg" : "#081c15",
        "fg" : "#74c69d",
        "font" : ("JetBrains Mono",16),
        "relief" : "raised",
        "anchor" : "w",
        "border" : 20
    },
    "ents" : {
        "bg" : "#2d6a4f",
        "fg" : "#d8f3dc",
        "font" : ("JetBrains Mono",16),
        "relief" : "raised",
        "border" : 20
    },
    "btns" : {
        "bg" : "#d8f3dc",
        "fg" : "#081c15",
        "font" : ("JetBrains Mono",16),
        "relief" : "raised",
        "border" : 20
    }
}

root = Tk()
root.title("Connecting!")
root.config(bg="#ffd166")
root.resizable(0,0)

host_lbl = Label(master=root,text="Host : ",cnf=configurations["lbls"])
user_lbl = Label(master=root,text="Username : ",cnf=configurations["lbls"])
pass_lbl = Label(master=root,text="Password : ",cnf=configurations["lbls"])
data_lbl = Label(master=root,text="Database : ",cnf=configurations["lbls"])

host_ent = Entry(master=root,cnf=configurations["ents"])
user_ent = Entry(master=root,cnf=configurations["ents"])
pass_ent = Entry(master=root,cnf=configurations["ents"])
data_ent = Entry(master=root,cnf=configurations["ents"])

cnts_btn = Button(master=root,text="Connect",cnf=configurations["btns"],command=cnt_main)

host_lbl.grid(row=0,column=0,sticky="nsew")
user_lbl.grid(row=1,column=0,sticky="nsew")
pass_lbl.grid(row=2,column=0,sticky="nsew")
data_lbl.grid(row=3,column=0,sticky="nsew")

host_ent.grid(row=0,column=1,sticky="nsew")
user_ent.grid(row=1,column=1,sticky="nsew")
pass_ent.grid(row=2,column=1,sticky="nsew")
data_ent.grid(row=3,column=1,sticky="nsew")

cnts_btn.grid(row=4,column=0,columnspan=2,sticky="nsew")

root.mainloop()
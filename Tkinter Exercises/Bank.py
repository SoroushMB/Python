# NoteBook , Text , Label , Frame , Button , Checkbutton , Entry , Toplevel , Combobox
# showerror , showinfo , showwarning
# pack , place , grid
# txt , json
#  ? : File
#  ? : Library
import json
from os.path import isfile
from tkinter import Entry,Label,Button,Tk,Toplevel,Frame,Text
from tkinter.ttk import Checkbutton,Combobox
from tkinter.messagebox import showerror,showinfo,showwarning
# Registry
def register():
    global username,password
    username = username_entry.get()
    password = password_entry.get()
    file_existence = isfile(r"C:\Users\DELL\Documents\Codes\Python\Tkinter Exercises\users.json")
    if file_existence:
        with open(r"C:\Users\DELL\Documents\Codes\Python\Tkinter Exercises\users.json") as users_file:
            json_file = json.load(users_file)
        json_file.append({
            "Username" : "username",
            "Password" : "password"
        })
    if not file_existence:
        with open("users.json","w") as new_users_file:
            print("The JSON file is created")
def login():
   ...
registry_configs = {
    "buttons" : {
        "bg" : "#231942",
        "fg" : "gray95",
        "font" : ("Product Sans Medium",16),
        "border" : 25,
        "relief" : "ridge",
        "width" : 14
    },
    "labels" : {
        "bg" : "#5e548e",
        "fg" : "gray95",
        "font" : ("Product Sans Medium",16),
        "border" : 25,
        "relief" : "raised",
        "width" : 12
    },
    "entries" : {
        "bg" : "#e0b1cb",
        "fg" : "gray5",
        "font" : ("Product Sans Medium",16),
        "border" : 25,
        "relief" : "sunken",
        "width" : 16
    }
}

registry_page = Tk()

login_button = Button(master=registry_page,text="Login",cnf=registry_configs["buttons"],command=lambda:login())
register_button = Button(master=registry_page,text="Register",cnf=registry_configs["buttons"],command=lambda:register())

username_label = Label(master=registry_page,text="Username: ",cnf=registry_configs["labels"])
username_entry = Entry(master=registry_page,cnf=registry_configs["entries"])
password_label = Label(master=registry_page,text="Password: ",cnf=registry_configs["labels"])
password_entry = Entry(master=registry_page,cnf=registry_configs["entries"])

login_button.grid(row=2,column=0,sticky="nsew")
register_button.grid(row=2,column=1,sticky="nsew")
username_label.grid(row=0,column=0,sticky="nsew")
username_entry.grid(row=0,column=1,sticky="nsew")
password_label.grid(row=1,column=0,sticky="nsew")
password_entry.grid(row=1,column=1,sticky="nsew")
registry_page.mainloop()
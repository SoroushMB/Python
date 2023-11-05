from tkinter import Entry,Label,Button,Tk,Toplevel,Frame,Text
from tkinter.ttk import Checkbutton,Combobox
from tkinter.messagebox import showerror,showinfo,showwarning
# Registry
def register():
    username , password = username_entry.get() , password_entry.get()
    with open("Initial_User_Info.txt","a") as main_file:
        main_file = open("Initial_User_Info.txt","r")
        for line_number, line in enumerate(iterable=main_file):
            if username in line:
                showinfo(title="Pay Attention!",message="Your username does exist in our databases!")
                break
        else:
            main_file = open("Initial_User_Info.txt","a")
            main_file.write(f"Username : {username}\nPassword : {password}")

def login():
    with open("Initial_User_Info.txt","r") as main_file:
        for line_number, line in enumerate(iterable=main_file):
            if username_entry.get() in line:
                showinfo(title="Pay Attention!",message="Access Granted!")
                break
        else:
            showwarning(title="Pay Attention!",message="Your info didn't found in our databases!")
            
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
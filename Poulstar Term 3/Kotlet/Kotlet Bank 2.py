# Profile , Withdraw , Deposit , Donation(Red Cross)
from json import load
from tkinter import Entry,Label,Button,Tk,Toplevel,Frame,Text
from tkinter.ttk import Checkbutton,Combobox,Notebook
from tkinter.messagebox import showerror,showinfo,showwarning
# Openings
with open("main_configs.json","r") as main_page_configs:
    main_page_info = load(main_page_configs)
with open("registry_configs.json","r") as file:
    registry_configs = load(file)

def main_page():
    ...
    

def register():
    global username
    username , password = username_entry.get() , password_entry.get()
    with open(f"{username.get()}_Info.txt","a") as main_file:
        main_file = open(f"{username.get()}_Info.txt","r")
        for line_number, line in enumerate(iterable=main_file):
            if username in line:
                showinfo(title="Pay Attention!",message="Your username does exist in our databases!")
                break
        else:
            main_file = open(f"{username.get()}_Info.txt","a")
            main_file.write(f"Username : {username}\nPassword : {password}")

def login():
    with open(f"{username.get()}_Info.txt","r") as main_file:
        for line_number, line in enumerate(iterable=main_file):
            if username_entry.get() in line:
                showinfo(title="Pay Attention!",message="Access Granted!")
                main_page()
                break
        else:
            showwarning(title="Pay Attention!",message="Your info didn't found in our databases!")


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
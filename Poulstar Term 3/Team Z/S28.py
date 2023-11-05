# Label , Button , Text , Notebook , Frame , CheckButton , Combobox
# Bank : Profile , Withdraw , Deposit , Loan
from tkinter import Label,Button,Text,Frame,Checkbutton,Tk,Toplevel,Entry
from tkinter.ttk import Combobox,Notebook
from tkinter.messagebox import showerror,showinfo

def register():
    username = username_entry.get()
    password = password_entry.get()
    user_info_file = open("UserInfo.txt","a")
    user_info_file.write(f"Username: {username}\nPassword: {password}")
    user_info_file.close()
    showinfo(title="Pay Attention!",message="We have entered your info!")

def login():
    ...
    
login_button_configs = {
    "bg" : "#40916c",
    "fg" : "#d8f3dc",
    "font" : ("Product Sans Medium",16),
    "relief" : "ridge",
    "border" : 20,
    "width" : 14
}
login_label_configs = {
    "bg" : "#2d6a4f",
    "fg" : "gray99",
    "font" : ("Product Sans Medium",16),
    "relief" : "raised",
    "border" : 20,
    "width" : 12
}
login_entry_configs = {
    "bg" : "#081c15",
    "fg" : "gray99",
    "font" : ("Product Sans Medium",16),
    "relief" : "raised",
    "border" : 20,
    "width" : 16
}
registry_page = Tk()
registry_page.title("Registry")

login_button = Button(master=registry_page,text="Login",cnf=login_button_configs)
register_button = Button(master=registry_page,text="Register",cnf=login_button_configs,command=lambda:register())

username_label = Label(master=registry_page,text="Username:",cnf=login_label_configs)
password_label = Label(master=registry_page,text="Password:",cnf=login_label_configs)
username_entry = Entry(master=registry_page,cnf=login_entry_configs)
password_entry = Entry(master=registry_page,cnf=login_entry_configs)

login_button.grid(row=2,column=0,sticky="nsew")
register_button.grid(row=2,column=1,sticky="nsew")
username_label.grid(row=0,column=0,sticky="nsew")
password_label.grid(row=1,column=0,sticky="nsew")
username_entry.grid(row=0,column=1,sticky="nsew")
password_entry.grid(row=1,column=1,sticky="nsew")
registry_page.mainloop()
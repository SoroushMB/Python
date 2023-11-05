from tkinter import Tk,Toplevel,Label,LabelFrame,Button,Checkbutton
# First Page - Functions
def login():
    username_counter = 0
    passwd_counter = 0
    login_username = ...
    login_password = ...
    first_file = open("Registration Info.txt","r")
    first_file_rls = first_file.readlines()
    
    for user in first_file_rls:
        if login_username in user:
            username_counter += 1
    
    for passwd in first_file_rls:
        if login_password in passwd:
            passwd_counter += 1

def registration():
    ...
# Configurations

initial_config = {
    "font" : ("Consolas",16),
    "bg" : "blue",
    "fg" : "white"
}    
# First Page - Tk Window Setup
first_page = Tk()
first_page.title("Initial Registery")
first_page.after(ms=500)

login_btn = Button(first_page,text="Login",cnf=initial_config,command=lambda:login())
registration_btn = Button(first_page,text="Registration",cnf=initial_config,command=lambda:registration())
username_lbl = Label(first_page,text="Username: ",cnf=initial_config)
password_lbl = Label(first_page,text="Password: ",cnf=initial_config)
# Layout
first_page.mainloop()
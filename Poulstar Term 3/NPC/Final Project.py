from tkinter import Tk,Label,StringVar,Button,Entry,Checkbutton,PhotoImage,Toplevel,Frame
from tkinter.messagebox import showerror,showinfo
from tkinter.ttk import Notebook, Combobox
from json import dumps,load

configurations_root = {
    "lbls":{
        "bg":"#a3caeb",
        "fg":"black",
        "font":("SpaceMono Nerd Font",16),
        "border":15,
        "relief":"ridge"
    },
    "btns":{
        "bg":"#59a0da",
        "fg":"white",
        "font":("SpaceMono Nerd Font",16),
        "border":15,
        "relief":"raised"
    },
    "ents":{
        "bg":"#daeaf7",
        "fg":"black",
        "font":("SpaceMono Nerd Font",16),
        "border":15,
        "relief":"sunken"
    },
    "cbxs":{
        "background":"#daeaf7",
        "foreground":"black",
        "font":("SpaceMono Nerd Font",16),
        "border":15,
        "relief":"sunken"
    } 
}

def test(event):
    global to_cbx
    to_cbx.config(state="normal",values=list(range(0,10)))

def second_page():
    global configurations_root, username, to_cbx
    root.deiconify()
    app = Toplevel()
    icon_img = PhotoImage(file="smurf.png")
    app.title(string="Exchange")
    app.iconphoto(False,icon_img)
    
    exchanges = Notebook(master=app,width=640,height=960)
    crypto_currency = Frame(master=exchanges)
    normal_currency = Frame(master=exchanges)
    total = Frame(master=exchanges)
    
    greeting_lbl = Label(master=crypto_currency,text=f"Hi {username}!Welcome to Poulstar Exchange!",cnf=configurations_root["lbls"])
    greeting_lbl = Label(master=crypto_currency,text=f"Hi {username}!Welcome to Poulstar Exchange!",cnf=configurations_root["lbls"])
    greeting_lbl = Label(master=crypto_currency,text=f"Hi {username}!Welcome to Poulstar Exchange!",cnf=configurations_root["lbls"])
    
    from_cbx = Combobox(master=crypto_currency,values=list(range(0,9)),background="#daeaf7",foreground="black",font=("SpaceMono Nerd Font",16))
    to_cbx = Combobox(master=crypto_currency,background="#daeaf7",foreground="black",font=("SpaceMono Nerd Font",16),state="disabled")
    exchanges.add(child=crypto_currency,text="Crypto Currency")
    exchanges.add(child=normal_currency,text="Normal Currency")
    exchanges.add(child=total,text="Total")
    exchanges.pack()
    
    greeting_lbl.grid(row=0,column=0,sticky="nsew")
    from_cbx.grid(row=1,column=0,sticky="nsew")
    to_cbx.grid(row=2,column=0,sticky="nsew")
    
    from_cbx.bind(sequence="<<ComboboxSelected>>",func=test)
    app.mainloop()

def show_pass():
    ack = watcher.get()
    if ack == "off":
        password_ent.config(show="*")
    elif ack == "on":
        password_ent.config(show="")


def registering():  # sourcery skip: move-assign
    global username,password
    username = username_ent.get()
    password = password_ent.get()
    
    length_of_user = len(username)
    length_of_pass = len(password)
    if length_of_pass >= 8:
        if length_of_user >= 3:    
            user_info = {
                "Username" : username,
                "Password" : password
            }
            dumping = dumps(obj=user_info,indent=2)
            with open(f"{username}.json","w") as file:
                file.write(dumping)
            showinfo(title="Successful",message="Registered Successfully!")
        else:
            showerror(title="Alert!!!",message="Your username is too short!")
    else:
        showerror(title="Alert!!!",message="Your password is too weak!")

def login():
    global username,password
    username = username_ent.get()
    password = password_ent.get()
    try:
        with open(f"{username}.json","r") as file:
            example = load(file)

        if username in example["Username"]:
            if password in example["Password"]:
                showinfo(title="Succeed!",message="Access granted!")
                second_page()
            else:
                showerror(title="Alert!",message="Password isn't correct!")
        else:
            showerror(title="Alert!",message="Username not found!")
    except FileNotFoundError:
        showerror(title="Not found!",message="The user hasn't been registered!")

root = Tk()
icon_img = PhotoImage(file="smurf.png")
root.iconphoto(False,icon_img)
root.title(string="Smurf Exchange")
root.config(bg="#4695D6")

watcher = StringVar()
username_lbl = Label(master=root, text="Username : ", cnf=configurations_root["lbls"])
password_lbl = Label(master=root, text="Password : ", cnf=configurations_root["lbls"])
username_ent = Entry(master=root, cnf=configurations_root["ents"])
password_ent = Entry(master=root, cnf=configurations_root["ents"], show="*")
login_btn = Button(master=root, text="Login", cnf=configurations_root["btns"],command=login)
regis_btn = Button(master=root, text="Register", cnf=configurations_root["btns"],command=registering)
show_pass_ckb = Checkbutton(master=root, text="Show Password!",variable=watcher,offvalue="off",onvalue="on",command=show_pass, cnf=configurations_root["btns"])

username_lbl.grid(row=0 ,column=0 ,sticky="nsew")
password_lbl.grid(row=1 ,column=0 ,sticky="nsew")
username_ent.grid(row=0 ,column=1 ,sticky="nsew")
password_ent.grid(row=1 ,column=1 ,sticky="nsew")
show_pass_ckb.grid(row=2 ,column=0 ,columnspan=2 ,sticky="nsew")
login_btn.grid(row=3 ,column=0 ,columnspan=2 ,sticky="nsew")
regis_btn.grid(row=4 ,column=0 ,columnspan=2 ,sticky="nsew")
root.mainloop()
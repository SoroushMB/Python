from tkinter import Tk,Label,StringVar,Button,Entry,Checkbutton,PhotoImage,Toplevel,Frame
from tkinter.messagebox import showerror,showinfo
from tkinter.ttk import Notebook 
from json import dumps,load

configurations_root = {
    "lbls" : {
        "bg":"#a3ceab",
        "fg":"black",
        'font':("SpaceMono Nerd Font",16),
        "border":15,
        "relief":"ridge"

    },
    "btns":{
        "bg":"#59a0da",
        "fg":"white",
        "font":('SpaceMono Nerd Font',16),
        "border":15,
        "relief":"raised"

    },
    "ents":{
        "bg":"#daea71",
        "fg":"black",
        "font":("SpaceMono Nerd Font",16),
        "border":15,
        "relief":"sunken"
    }
}

def secoond_page():
    global configurations_root
    root.deiconify()
    app=Toplevel()
    icon_img = PhotoImage(file=r"C:\Users\DELL\Pictures\smurf.png")
    app.title(string="Exchange")
    app.iconphoto(False,icon_img)

    exchanges = Notebook(master=app,width=640,height=960)
    crypto_currency = Frame(master=exchanges)
    normal_currency = Frame(master=exchanges)
    total = Frame(master=exchanges)

    l1 = Label(master=crypto_currency,text="For Test!",cnf=configurations_root["lbls"])
    l2 = Label(master=normal_currency,text="For Test!",cnf=configurations_root["lbls"])
    l3 = Label(master=total,text="For Test!",cnf=configurations_root["lbls"])

    exchanges.add(child=crypto_currency,text="Crypto Currency")

    exchanges.add(child=normal_currency,text="Normal Currency")

    exchanges.add(child=total,text="Total")

    l1.grid(row=0,column=0,sticky="news")
    l2.grid(row=0,column=0,sticky="news")
    l3.grid(row=0,column=0,sticky="news")
    app.mainloop()

def showpass():
    ack = watcher.get()
    if ack == "off":
        password_ent.config(show="*")
    elif ack == "on-":
        password_ent.config(show="")
def registering():
    global username,password
    username = username_ent.get()
    password = password_ent.get()

    lenght_of_user = len(username)
    lenght_of_pass = len(password)
    if lenght_of_pass >= 8:
        if lenght_of_user >= 3:
            user_info = {
                "Username" : username,
                "Password" : password
            }
            dumping = dumps(obj=user_info,indent=2)
            with open(f"{username}.json","w") as file:
                file.write(dumping)
            showinfo(title="Successful",message="Re+9gistered Successfully!")
        else:
            showinfo(title="Alert!!!",message="Your username is too short!")
    else:
        showerror(title="Alert!!!",message="Your password is to weak!")
def login():
    global username,password
    username = username_ent.get()
    password = password_ent.get()

    try:
        with open(f"{username}.json","r") as file:
            example = load(file)
        if username in example["Username"]:
            if password in example["Password"]:
                showinfo(title='Succeed!',message="Access granted!")
            else:
                showerror(title="Alert!",message="Password isn't correct!")
        else:
            showerror(tittle="Alert!",message="User not found!")
    except FileNotFoundError:
        showerror(title="Not found!",message="The user hasn't been registered!")

root = Tk()
icon_img = PhotoImage(file=r"C:\Users\DELL\Pictures\smurf.png")
root.iconphoto(False,icon_img)
root.title(string="Sarafi Bemola")
root.config(bg="#4695D6")

watcher = StringVar()

username_lbl = Label(master=root,text="Username :",cnf=configurations_root["lbls"])
password_lbl = Label(master=root,text="Password :",cnf=configurations_root["lbls"])
username_ent = Entry(master=root,cnf=configurations_root["ents"])
password_ent = Entry(master=root,cnf=configurations_root["ents"])
login_btn = Button(master=root,text="Login",cnf=configurations_root["btns"],command=login)
regis_btn = Button(master=root,text="Register",cnf=configurations_root["btns"],command=registering)
show_pass_ckb = Checkbutton(master=root,text="ShowPassword",variable=watcher,offvalue="off",onvalue="on",command=showpass,cnf=configurations_root["btns"])

username_lbl.grid(row=0,column=0,sticky="news")
password_lbl.grid(row=1,column=0,sticky="news")
username_ent.grid(row=0,column=1,sticky="news")
password_ent.grid(row=1,column=1,sticky="news")
show_pass_ckb.grid(row=2,column=0,sticky="news",columnspan=2)
login_btn.grid(row=3,column=0,sticky="news",columnspan=2)
regis_btn.grid(row=4,column=0,sticky="news",columnspan=2)
root.mainloop()
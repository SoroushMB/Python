from  tkinter import Tk,Label,Button,LabelFrame,StringVar,Entry,Checkbutton
from tkinter.messagebox import showinfo,showerror
from json import dumps,load

def show_pass():
    ack=watcher.get()
    if ack== "Bye":
        password_ent.config(show="*")
    elif ack =="Hi":
        password_ent.config(show="")

def registering():
    global username,password
    username=username_ent.get()
    password=password_ent.get()
    lenghth_of_user = len(username)
    lenghth_of_pass = len(password)
    if lenghth_of_pass >=8:
        if lenghth_of_user >=3:
            user_info ={
                "Username":username,
                "Password":password
            }           
            writing_json=dumps(obj=user_info,indent=2)
            with open(f"{username}.json","w") as file:
                file.write(writing_json)
            showinfo(title="Successful",message="Registered successfully!")
        else:
            showerror(title="Alert!!!",message="Your username is too short")
    else:
        showerror(title="Alert!!!",message="Your password is too week!")

def login():
    global username,password
    username=username_ent.get()
    password=password_ent.get()
    try:
        with open(f"{username}.json") as test:
            example = load(test)
        if username in example["Username"]:
            if password in example["Password"]:
                showinfo(message="Access granted")
            else:
                showerror(message="Password isnt correct!")
        else:
            showerror(message="Username not found!")
    except FileNotFoundError:
        showerror(title="Not found",message="The user hasnt been registered")

configs_root = {
    "lbls" : {
        "bg" : "white",
        "fg" : "Black",
        "relief" : "groove",
        "border" : 14,
        "font" : ("Gotham-Medium",16)
    },
    "btns" : {
        "bg": "white",
        "fg" : "Black",
        "relief" : "groove",
        "border" : 14,
        "font" : ("Gotham-Medium",16)
    },

}


root=Tk()
root.title("final")
root.config(bg="snow")

watcher=StringVar()

username_lbl=Label(master=root,text="Username:",cnf=configs_root["lbls"])
password_lbl=Label(master=root,text="PassWord:",cnf=configs_root["lbls"])

login_btn=Button(master=root,text="Login",cnf=configs_root["btns"],command=lambda:login())
register_btn=Button(master=root,text="Register",cnf=configs_root["btns"],command=registering)
show_pass_ckb = Checkbutton(master=root,text="show password!",variable=watcher,offvalue="Bye",onvalue="Hi",cnf=configs_root["btns"],command=show_pass)

username_ent=Entry(master=root,font=("Consolas",16),borderwidth=10)
password_ent=Entry(master=root,font=("Consolas",16),borderwidth=10,show="*")

username_lbl.grid(row=0,column=0,sticky="news ")
password_lbl.grid(row=1,column=0,sticky="news ")
show_pass_ckb.grid(row=2,column=0,columnspan=2,sticky="news")
login_btn.grid(row=3,column=0,rowspan=1,columnspan=3,sticky="news ")
register_btn.grid(row=4,column=0,rowspan=1,columnspan=3,sticky="news ")
username_ent.grid(row=0,column=1,columnspan=1,rowspan=1,sticky="news")
password_ent.grid(row=1,column=1,columnspan=1,rowspan=1,sticky="news")

root.mainloop()

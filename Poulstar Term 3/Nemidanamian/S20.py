from tkinter import Label,Tk,Button,Checkbutton,Entry,BooleanVar,Toplevel
from tkinter.messagebox import showinfo,showerror
# -----Functions-----
def exiting():
    global store_page
    store_page.deiconify()

def showing():
    manager = receiver.get()
    if manager == False:
        users_ent.config(show="*")
    elif manager == True:
        users_ent.config(show="")

def opening_window():
    global store_page,registry_page
    registry_page.iconify()
    username = users_ent.get()
    if len(username) != 0:
        store_page = Toplevel()
        greeting_lbl = Label(master=store_page,cnf=settings["lbls"],text=f"Hello, {username}!")
        exiting_btn = Button(master=store_page,cnf=settings["btns"],text="Exit!",command=exiting)
        
        greeting_lbl.pack(anchor="center")
        exiting_btn.pack(anchor="center")
        store_page.mainloop()
    else:
        showerror(title="Failed to open!",message="Please enter your username!")
        registry_page.deiconify()
        
# -----Configurations-----
settings = {
    "lbls" : {
        "font" : ("JetBrains Mono",16),
        "bg" : "Black",
        "fg" : "Orange",
        "padx" : 20,
        "pady" : 20,
        "relief" : "ridge",
        "border" : 20
    },
    "ents" : {
        "font" : ("JetBrains Mono",16),
        "bg" : "Black",
        "fg" : "White",
        "relief" : "sunken",
        "border" : 20
    },
    "btns" : {
        "font" : ("JetBrains Mono",16),
        "bg" : "Black",
        "fg" : "LightSteelBlue1",
        "relief" : "raised",
        "border" : 20
    },
    "chkbtns" : {
        "font" : ("JetBrains Mono",16),
        "bg" : "Black",
        "fg" : "LightGreen",
        "relief" : "solid",
        "border" : 20
    }
}
# -----Registry Window-----
registry_page = Tk()
registry_page.title(string="Registry Page")
registry_page.config(bg="black")

receiver = BooleanVar()

title_bar = Label(master=registry_page,text="PoulStore",cnf=settings["lbls"])
users_lbl = Label(master=registry_page,text="Username:",cnf=settings["lbls"])
users_ent = Entry(master=registry_page,cnf=settings["ents"])
showing_chkbtn = Checkbutton(master=registry_page,text="Show as emoji!",variable=receiver,offvalue=False,onvalue=True,cnf=settings["chkbtns"],command=lambda:showing())
opening_btn = Button(master=registry_page,text="Open the store!",cnf=settings["btns"],command=opening_window)

title_bar.grid(row=0,column=0,columnspan=2,sticky="nsew")
users_lbl.grid(row=1,column=0,sticky="nsew")
users_ent.grid(row=1,column=1,sticky="nsew")
showing_chkbtn.grid(row=2,column=0,columnspan=2,sticky="nsew")
opening_btn.grid(row=3,column=0,columnspan=2,sticky="nsew")
registry_page.mainloop()

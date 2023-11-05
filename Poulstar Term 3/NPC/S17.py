from tkinter import Entry,Button,Tk,Label,Text

def saving():
    age = int(age_etr.get())
    name = name_etr.get()
    info = info_txt.get(index1="1.0",index2="end")
    with open("User_info.txt","a") as saver:
        saver.write(f"\nName : {name}\nAge : {age}\nInfo : {info}")
    print("Saved!")
    
lbl_config = {
    "font" : ("JetBrains Mono",16),
    "bg" : "darkred",
    "fg" : "white",
    "relief" : "raised",
    "border" : 20,
    "padx" : 10,
    "pady" : 10
}
etr_config = {
    "font" : ("JetBrains Mono",16),
    "bg" : "darkred",
    "fg" : "white",
    "relief" : "ridge",
    "border" : 20,
    "borderwidth" : 10
}
btn_config = {
    "font" : ("JetBrains Mono",16),
    "bg" : "darkblue",
    "fg" : "white",
    "relief" : "sunken",
    "border" : 20,
}

root = Tk()

name_lbl = Label(master=root,text="Name : ",cnf=lbl_config)
age_lbl = Label(master=root,text="Age : ",cnf=lbl_config)
info_lbl = Label(master=root,text="Info : ",cnf=lbl_config)

name_etr = Entry(master=root,cnf=etr_config)
age_etr = Entry(master=root,cnf=etr_config)
info_txt = Text(master=root,cnf=etr_config,height=5)

save_button = Button(master=root,text="Save!",cnf=btn_config,command=saving)

name_lbl.grid(row=0 ,column=0 ,sticky="nsew")
age_lbl.grid(row=1 ,column=0 ,sticky="nsew")
name_etr.grid(row=0 ,column=1 ,sticky="nsew")
age_etr.grid(row=1 ,column=1 ,sticky="nsew")
info_lbl.grid(row=2 ,column=0 ,sticky="nsew")
info_txt.grid(row=2 ,column=1 ,sticky="nsew")
save_button.grid(row=3 ,column=0 ,columnspan=2 ,sticky="nsew")

root.mainloop()
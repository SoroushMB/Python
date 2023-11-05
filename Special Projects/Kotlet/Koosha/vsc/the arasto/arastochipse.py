from  tkinter import Tk,Label,Button,Spinbox,LabelFrame
configs = {
    "lbls" : {
        "bg" : "gray15",
        "fg" : "gray55",
        "relief" : "groove",
        "border" : 14,
        "font" : ("Gotham-Medium",16)
    },
    "btns" : {
        "bg": "gray10",
        "fg" : "gray50",
        "relief" : "groove",
        "border" : 14,
        "font" : ("Gotham-Medium",16)
    },
}
root=Tk()
root.title("--Store--")
root.config(bg="black")

the_title = LabelFrame(master=root,text="Poulstar Store")

chips_lbl = Label(master=the_title,text="Chips",cnf=configs["lbls"])
cheese_puffs_lbl = Label(master=the_title,text="Cheese Puff",cnf=configs["lbls"])
popcorn_lbl=Label(master=the_title,text="Popcorn",cnf=configs["lbls"])

chips_up=Button(master=the_title,text="↑",cnf=configs["btns"])
chips_down=Button(master=the_title,text="↓",cnf=configs["btns"])

cheese_puffs_up=Button(master=the_title,text="↑",cnf=configs["btns"])
cheese_puffs_down=Button(master=the_title,text="↓",cnf=configs["btns"])

popcorn_up=Button(master=the_title,text="↑",cnf=configs["btns"])
popcorn_down=Button(master=the_title,text="↓",cnf=configs["btns"])

final_price_btn=Button(master=root,text="Final Price",cnf=configs["btns"])

price_lbl=Label(master=the_title,text=f"Price : $",cnf=configs["lbls"])

coins=Spinbox(master=the_title,from_=0.5,to=10,background="black",foreground="grey44",increment=0.5,font=("Gotham-Medium",16),relief="groove",border=15)
bill=Button(master=the_title,text="Billing",cnf=configs["btns"])

the_title.grid(row=0,column=0,sticky="news")
chips_lbl.grid(row=0,column=0,sticky="news")
cheese_puffs_lbl.grid(row=0,column=1,sticky="news")
popcorn_lbl.grid(row=0,column=2,sticky="news")
chips_up.grid(row=1,column=0,sticky="news")
chips_down.grid(row=2,column=0,sticky="news")
cheese_puffs_up.grid(row=1,column=1,sticky="news")
cheese_puffs_down.grid(row=2,column=1,sticky="news")
popcorn_up.grid(row=1,column=2,sticky="news")
popcorn_down.grid(row=2,column=2,sticky="news")
final_price_btn.grid(row=3,column=0,columnspan=3,sticky="news")
price_lbl.grid(row=4,column=0,rowspan=2,sticky="news")
coins.grid(row=4,column=1,columnspan=2,sticky="news")
bill.grid(row=5,column=1,columnspan=2,sticky="news")

root.mainloop()
from tkinter import Tk,Label,Button,Spinbox,LabelFrame

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
chipsA = 0
def add_chips(chips):
    global chipsA
    if chips == "chipsup":
        chipsA +=1
        chips_up.config(text=f"↑:{chipsA}")
        chips_down.config(text=f"↓:{chipsA}")
        
    elif chips == "chipsdown":
        chipsA -=1
        chips_up.config(text=f"↑:{chipsA}")
        chips_down.config(text=f"↓:{chipsA}")
        
puffsA = 0
def add_cheese_puffs(cheese_puffs):
    global puffsA
    if cheese_puffs == "cheesepuffsup":
        puffsA +=1
        cheese_puffs_up.config(text=f"↑:{puffsA}")
        cheese_puffs_down.config(text=f"↓:{puffsA}")
    elif cheese_puffs == "cheesepuffsdown":
        puffsA -=1
        cheese_puffs_up.config(text=f"↑:{puffsA}")
        cheese_puffs_down.config(text=f"↓:{puffsA}")
        
popA = 0
def add_popcorn(popcorn):
    global popA
    if popcorn == "popcornup":
        popA +=1
        popcorn_up.config(text=f"↑:{popA}")
        popcorn_down.config(text=f"↓:{popA}")
    elif popcorn == "popcorndown":
        popA-=1
        popcorn_up.config(text=f"↑:{popA}")
        popcorn_down.config(text=f"↓:{popA}")


text=f"↑:{add_chips}"



root=Tk()
root.title("--Store--")
root.config(bg="black")

the_title = LabelFrame(master=root,text="Poulstar Store")
    
chips = Label(master=the_title,text="chips",cnf=configs["lbls"])
cheese_puffs = Label(master=the_title,text="Cheese Puff",cnf=configs["lbls"])
popcorn = Label(master=the_title,text="Popcorn",cnf=configs["lbls"])

chips_up = Button(master=the_title,text=f"↑:{chipsA}",cnf=configs["btns"],command=lambda:add_chips("chipsup"))
chips_down = Button(master=the_title,text=f"↓:{chipsA}",cnf=configs["btns"],command=lambda:add_chips("chipsdown"))

cheese_puffs_up = Button(master=the_title,text=f"↑:{puffsA}",cnf=configs["btns"],command=lambda:add_cheese_puffs("cheesepuffsup"))
cheese_puffs_down = Button(master=the_title,text=f"↓:{puffsA}",cnf=configs["btns"],command=lambda:add_cheese_puffs("cheesepuffsdown"))

popcorn_up = Button(master=the_title,text=f"↑:{popA}",cnf=configs["btns"],command=lambda:add_popcorn("popcornup"))
popcorn_down = Button(master=the_title,text=f"↓:{popA}",cnf=configs["btns"],command=lambda:add_popcorn("popcorndown"))

final_price_btn = Button(master=root,text="Final Price",cnf=configs["btns"])

price_lbl = Label(master=the_title,text=f"Price : $",cnf=configs["lbls"])

coins = Spinbox(master=the_title,from_=0.5,to=50,wrap=True,background="black",foreground="grey44",increment=0.5,font=("Gotham-Medium",16),relief="groove",border=15)
bill = Button(master=the_title,text="Billing",cnf=configs["btns"])

the_title.grid(row=0,column=0,sticky="news")
chips.grid(row=0,column=0,sticky="news")
cheese_puffs.grid(row=0,column=1,sticky="news")
popcorn.grid(row=0,column=2,sticky="news")
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
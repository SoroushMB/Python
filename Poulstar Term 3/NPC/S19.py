from tkinter import Button,Label,LabelFrame,Tk,Spinbox
from tkinter.messagebox import showerror

configs = {
    "lbls" : {
        "bg" : "gray15",
        "fg" : "gray55",
        "relief" : "groove",
        "border" : 14,
        "font" : ("Gotham-Medium",16),
        "width" : 12
    },
    "btns" : {
        "bg" : "gray10",
        "fg" : "gray50",
        "relief" : "groove",
        "border" : 14,
        "font" : ("Gotham-Medium",16)
    }
}

chips = 0
cheese_puffs = 0
popcorn = 0

def upper(btn):

    global chips,cheese_puffs,popcorn
    if chips > -1 and cheese_puffs > -1 and popcorn > -1:
        if btn == "chips_up":
            chips += 1
            chips_lbl.config(text=f"Chips : {chips}")
        elif btn == "cheese_puffs_up":
            cheese_puffs += 1
            cheese_puffs_lbl.config(text=f"Cheese Puff : {cheese_puffs}")
        elif btn == "popcorn_up":
            popcorn += 1
            popcorn_lbl.config(text=f"Popcorn : {popcorn}")
    else:
        showerror(title="Alert",message="The count of products can't be negative!")
        if chips < 0:
            chips += 1
            chips_lbl.config(text=f"Chips : {chips}")
        if cheese_puffs < 0:
            cheese_puffs += 1
            cheese_puffs_lbl.config(text=f"Cheese Puff : {cheese_puffs}")
        if popcorn < 0:
            popcorn += 1
            popcorn_lbl.config(text=f"Popcorn : {popcorn}")

def lower(btn):

    global chips,cheese_puffs,popcorn
    if chips > -1 and cheese_puffs > -1 and popcorn > -1:
        if btn == "chips_down":
            chips -= 1
            chips_lbl.config(text=f"Chips : {chips}")
        elif btn == "cheese_puffs_down":
            cheese_puffs -= 1
            cheese_puffs_lbl.config(text=f"Cheese Puff : {cheese_puffs}")
        elif btn == "popcorn_down":
            popcorn -= 1
            popcorn_lbl.config(text=f"Popcorn : {popcorn}")
    else:
        showerror(title="Alert",message="The count of products can't be negative!")
        if chips < 0:
            chips += 1
            chips_lbl.config(text=f"Chips : {chips}")
        if cheese_puffs < 0:
            cheese_puffs += 1
            cheese_puffs_lbl.config(text=f"Cheese Puff : {cheese_puffs}")
        if popcorn < 0:
            popcorn += 1
            popcorn_lbl.config(text=f"Popcorn : {popcorn}")


def checkout():
    
    global total_price
    current_money = int(coins.get())
    price_lbl.config(text=f"Price : ${total_price - current_money}")

def showing():
    
    global total_price
    chips_price = chips*2
    cheese_puffs_price = cheese_puffs*2.5
    popcorn_price = popcorn*2
    total_price =  chips_price + cheese_puffs_price + popcorn_price
    price_lbl.config(text=f"Price : ${total_price}")
    with open("Transaction.txt","a") as saving_file:
        saving_file.write(f"\nChips : {chips} \nCheese Puff : {cheese_puffs} \nPopcorn : {popcorn} \nFinal Price : {total_price}")

root = Tk()
root.title("--Store--")
root.config(bg="Black")

the_title = LabelFrame(master=root,text="Poulstar Store")

chips_lbl = Label(master=the_title,text="Chips : 0",cnf=configs["lbls"])
cheese_puffs_lbl = Label(master=the_title,text="Cheese Puff : 0",cnf=configs["lbls"])
popcorn_lbl = Label(master=the_title,text="Popcorn : 0",cnf=configs["lbls"])

chips_up = Button(master=the_title,text="↑",cnf=configs["btns"],command=lambda:upper(btn="chips_up"))
chips_down = Button(master=the_title,text="↓",cnf=configs["btns"],command=lambda:lower(btn="chips_down"))

cheese_puffs_up = Button(master=the_title,text="↑",cnf=configs["btns"],command=lambda:upper(btn="cheese_puffs_up"))
cheese_puffs_down = Button(master=the_title,text="↓",cnf=configs["btns"],command=lambda:lower(btn="cheese_puffs_down"))

popcorn_up = Button(master=the_title,text="↑",cnf=configs["btns"],command=lambda:upper(btn="popcorn_up"))
popcorn_down = Button(master=the_title,text="↓",cnf=configs["btns"],command=lambda:lower(btn="popcorn_down"))

final_price_btn = Button(master=the_title,text="Final Price",cnf=configs["btns"],command=showing)
price_lbl = Label(master=the_title,text="Price : $0",cnf=configs["lbls"])

coins = Spinbox(master=the_title,from_=1,to=100,state="readonly",background="Black",foreground="grey44",font=("Gotham-Medium",16),relief="groove",border=15)
bill = Button(master=the_title,text="Billing",cnf=configs["btns"],command=checkout)

the_title.grid(row=0 ,column=0 ,sticky="nsew")
chips_lbl.grid(row=0 ,column=0 ,sticky="nsew")
cheese_puffs_lbl.grid(row=0 ,column=1,sticky="nsew")
popcorn_lbl.grid(row=0 ,column=2 ,sticky="nsew")
chips_up.grid(row=1 ,column=0 ,sticky="nsew")
chips_down.grid(row=2 ,column=0 ,sticky="nsew")
cheese_puffs_up.grid(row=1 ,column=1 ,sticky="nsew")
cheese_puffs_down.grid(row=2 ,column=1 ,sticky="nsew")
popcorn_up.grid(row=1 ,column=2 ,sticky="nsew")
popcorn_down.grid(row=2 ,column=2 ,sticky="nsew")
final_price_btn.grid(row=3 ,column=0,columnspan=3,sticky="nsew")
price_lbl.grid(row=4 ,column=0,rowspan=2,sticky="nsew")
coins.grid(row=4 ,column=1 ,columnspan=2 ,sticky="nsew")
bill.grid(row=5 ,column=1 ,columnspan=2, sticky="nsew")

root.mainloop()

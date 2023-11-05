# Cookie - __init__(capacity=12) - deposit - withdraw - show🍪
""" 
This program will simulate how a cookie factory will create 
&
fill their boxes!
"""
from tkinter import Button,Entry,Label,Tk
from tkinter.messagebox import showerror

class Cookie_Factory:
    
    def __init__(self,capacity:int,current:int):
        self.capacity = capacity
        self.current = current
        current = capacity

    def deposit(self,increment:int):
        if self.current < self.capacity and increment <= self.capacity-self.current:
            return self.current + increment
        else:
            showerror(title="Increasing Alert!",message=f"The income is more than box's capacity!\nCapacity : {self.capacity}")

    def withdraw(self,decrement:int):
        if decrement < self.current:
            return self.current - decrement
        else:
            showerror(title="Decreasing Alert!",message=f"Insufficient availability!\nAvailability : {self.current}")
        
    def show(self,mode:str):
        if mode == "Current":
            return "🍪 " * self.current
        elif mode == "Capacity":
            return "🍪 " * self.capacity
        
    def r_and_c(self,mode):
        if mode == "Remained":
            remained = Cookie_Factory.show("Current")
            remained_lbls.config(text = f"{remained}")
        elif mode == "Capacity":
            capacity = Cookie_Factory.show("Capacity")
            capacity_lbls.config(text = f"{capacity}")

configurations = {
    "lbls":{
        "fg":"Black",
        "bg":"#EFE2B2",
        "font":("JetBrains Mono",12),
        "border":20,
        "relief":"groove",
        "width":54,
        "anchor":"w"
    },
    "btns":{
        "fg":"White",
        "bg":"#5A2C22",
        "font":("JetBrains Mono",16),
        "border":20
    },
    "ents":{
        "fg":"Black",
        "bg":"#BD8C61",
        "font":("JetBrains Mono",16),
        "border":20,
        "relief":"sunken"
    }
}
Nadi = Cookie_Factory(capacity=12,current=11)

root = Tk()
root.config(relief="raised",bg="#84563C")

# Showing the amount remained in the boxes!
remained_lbls = Label(master=root,text="To see the remained amount please press the button on the left side",cnf=configurations["lbls"])
capacity_lbls = Label(master=root,text="To see the capacity please press the button on the left side",cnf=configurations["lbls"])

remained_btns = Button(master=root,text="Remained",cnf=configurations["btns"],command=lambda:(Nadi.r_and_c("Remained")))
capacity_btns = Button(master=root,text="Capacity",cnf=configurations["btns"],command=lambda:(Nadi.r_and_c("Capacity")))

# # Decreasing | Increasing the amount of cookies available in boxes!
increasing_ent = Entry(master=root,cnf=configurations["ents"])
decreasing_ent = Entry(master=root,cnf=configurations["ents"])
increasing_lbl = Label(master=root,text="Increasing : ",cnf=configurations["lbls"])
decreasing_lbl = Label(master=root,text="Decreasing : ",cnf=configurations["lbls"])
increasing_btn = Button(master=root,text="Increase",cnf=configurations["btns"],command=lambda:Nadi.deposit(increment=int(increasing_ent.get())))
decreasing_btn = Button(master=root,text="Decrease",cnf=configurations["btns"],command=lambda:Nadi.withdraw(decrement=int(decreasing_ent.get())))

remained_btns.grid(row=0,column=0,sticky="nsew")
capacity_btns.grid(row=1,column=0,sticky="nsew")
remained_lbls.grid(row=0,column=1,sticky="nsew")
capacity_lbls.grid(row=1,column=1,sticky="nsew")
increasing_ent.grid(row=2 ,column=1 ,sticky="nsew")
decreasing_ent.grid(row=3 ,column=1 ,sticky="nsew")
increasing_lbl.grid(row=2 ,column=0 ,sticky="nsew")
decreasing_lbl.grid(row=3 ,column=0 ,sticky="nsew")
increasing_btn.grid(row=4 ,column=0 ,columnspan=2 ,sticky="nsew")
decreasing_btn.grid(row=5 ,column=0 ,columnspan=2 ,sticky="nsew")
root.mainloop()
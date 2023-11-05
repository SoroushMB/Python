# Cookie - __init__(capacity=12) - deposit - withdraw - show🍪
""" 
This program will simulate how a cookie factory will create 
&
fill their boxes!
"""
from tkinter import Button,Entry,Label,Tk
import tkinter

class Cookie_Factory:
    
    def __init__(self,capacity:int,current:int):
        self.capacity = capacity
        self.current = current
        current = capacity

    def deposit(self,increment:int):
        if self.current < self.capacity and increment <= self.capacity-self.current:
            return self.current + increment
        else:
            print("The jar doesn't have enough space left!")
    
    def withdraw(self,decrement:int):
        if decrement < self.current:
            return self.current - decrement
        else:
            print("Insufficient availability!")
            
    def show(self,mode:str):
        if mode == "Current":
            return "🍪 " * self.current
        elif mode == "Capacity":
            return "🍪 " * self.capacity
        
    def r_and_c(self,mode):
        if mode == "Remained":
            remained = Nadi.show("Current")
            remained_lbls.config(text = f"{remained}")
        elif mode == "Capacity":
            capacity = Nadi.show("Capacity")
            capacity_lbls.config(text = f"{capacity}")

configurations = {
    "lbls":{
        "fg":"Black",
        "bg":"#EFE2B2",
        "font":("JetBrains Mono",15),
        "border":20,
        "width":66,
        "anchor":"w"
    },
    "btns":{
        "fg":"White",
        "bg":"#5A2C22",
        "font":("JetBrains Mono",16),
        "border":20
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
# Entry()
# Entry()
# Label()
# Label()
remained_btns.grid(row=0,column=0,sticky="nsew")
capacity_btns.grid(row=1,column=0,sticky="nsew")
remained_lbls.grid(row=0,column=1,sticky="nsew")
capacity_lbls.grid(row=1,column=1,sticky="nsew")

root.mainloop()
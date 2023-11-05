# Dictionary - JSON Writing - Login(Entry Filling) - Bind - MassageBox - Picture
from tkinter import Tk,Label,Button,Entry,Spinbox
from tkinter.ttk import Combobox
from json import load,dump
from tkinter.messagebox import showerror

def selected(event):
    selected_pet = pets_cbx.get()
    if selected_pet == "Cats":
        selected_pets_cbx.config(state="readonly",values=final_result["Cats"],font=("Product Sans Medium",16))
    elif selected_pet == "Dogs":
        selected_pets_cbx.config(state="readonly",values=final_result["Dogs"],font=("Product Sans Medium",16))

def making_sure(event):
    global sure
    sure = username.get()
    if sure == True:
        counter.config(state="readonly",from_=0,to=9,wrap=True)
    else:
        showerror(title="Warning!",message="You haven't enter your username in the section mentioned!")

root = Tk()

with open("Pets.json","r") as result:
    final_result = load(result)
kinds_of_pets = list(final_result.keys())

username = Entry(master=root,font=("Product Sans Medium",16))
pets_cbx = Combobox(master=root,values=kinds_of_pets,state="readonly",font=("Product Sans Medium",16))
selected_pets_cbx = Combobox(master=root,state="disabled",values=sure)
counter = Spinbox(master=root,state="disabled",font=("Product Sans Medium",16))


pets_cbx.bind("<<ComboboxSelected>>",selected)
selected_pets_cbx.bind("<Button-1>",making_sure)

username.pack()
pets_cbx.pack()
selected_pets_cbx.pack()
counter.pack()

root.mainloop()
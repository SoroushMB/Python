from tkinter import Button,Entry,Label,LabelFrame,Frame,Tk
from tkinter.ttk import Spinbox,Combobox
from PIL import ImageTk, Image


class Pokemon:
    
    def __init__(self,Type:str,name:str,HP:int,Weakness:str,generation:int=1):
        self.Type = Type
        self.name = name
        self.HP = HP
        self.Weakness = Weakness
        self.generation = generation

    def defense_classification(self):
        if 140 <= self.HP <= 180:
            return "Defense Low Level"
        elif 181 <= self.HP <= 220:
            return "Defense Mid Level"
        else:
            return "Defense High Level"
        
    def gen_classification(self):
        if 1 <= self.generation <= 2:
            return "Low Level"
        elif 3 <= self.generation <= 5:
            return "Mid Level"
        else:
            return "High Level"


first_character = Pokemon(Type="Fairy",name="Wigglytuff",Weakness="Poison",HP=140,generation=6)
first_character_img = Image.open(fp="../assets/images/wigglytuff.png")
second_character = Pokemon(Type="Poison",name="Etenatus",Weakness="Dragon",HP=255)
third_character = Pokemon(Type="Dragon",name="Guzzlord",Weakness="Ice",HP=223)
fourth_character = Pokemon(Type="Ice",name="Cetitan",Weakness="Steel",HP=170)
fifth_character = Pokemon(Type="Steel",name="Nihon",Weakness="Fairy",HP=190)

configurations = {
    "lbls":{"bg":"yellow",
            "fg":"black",
            "font":("JetBrains Mono",20),
            "relief":"groove",
            "bd":20,
            "padx":10,
            "pady":10,},
    "btns":{"bg":"red",
            "fg":"black",
            "font":("JetBrains Mono",20),
            "relief":"groove",
            "bd":20,
            "padx":10,
            "pady":10,},
    "ents":{"bg":"gray75",
            "fg":"black",
            "font":("JetBrains Mono",20),
            "relief":"groove",
            "bd":20,
            "padx":10,
            "pady":10,}}

root = Tk()

f1 = LabelFrame(text="search",bg="black",fg="yellow")

nl = Label(master=f1,cnf=configurations["lbls"],text="NAME")
tl = Label(master=f1,cnf=configurations["lbls"],text="TYPE")
hl = Label(master=f1,cnf=configurations["lbls"],text="HEALTH")
sl = Label(master=f1,cnf=configurations["lbls"],text="SHOW")
gb = Button(master=f1,cnf=configurations["btns"],text="GO TO GAME")

ne = Entry(master=f1,cnf=configurations["ents"])
te = Entry(master=f1,cnf=configurations["ents"])
le = Entry(master=f1,cnf=configurations["ents"])

f1.grid(row=1,column=1)
nl.grid(row=0,column=1,sticky="nsew")
tl.grid(row=1,column=1,sticky="nsew")
hl.grid(row=2,column=1,sticky="nsew")
sl.grid(row=0,column=8,rowspan=3,sticky="nsew")
ne.grid(row=0,column=4,sticky="nsew")
te.grid(row=1,column=4,sticky="nsew")
le.grid(row=2,column=4,sticky="nsew")
gb.grid(row=4,column=1,sticky="nsew",columnspan=10)

root.mainloop()

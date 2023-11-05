from tkinter import Label,Tk,Button,Frame
from tkinter.ttk import Notebook,Combobox

def print1(event):
    nissan_models.config(state="normal",values=nissan_names)
def print2(event):
    print("2")
def print3(event):
    print("3")

root = Tk()

car_shop = Notebook(master=root)
toyota = Frame(master=car_shop,
               width=400,
               height=600)
nissan = Frame(master=car_shop,
               width=400,
               height=600)
pagani = Frame(master=car_shop,
               width=400,
               height=600)

toyota_names = ["Prius","Supra","LandCruiser","Prado","Prius FR"]
nissan_names = ["Leaf","GTR R34","370z","GTR R35","X-Trail"]
pagani_names = ["Zonda F","Huayra","Zonda R","Zonda Cirque"]

toyota_models = Combobox(master=toyota,
                        font=("JetBrains Mono",16),
                        values=toyota_names,
                        background="#4cc9f0",
                        foreground="gray7")
nissan_models = Combobox(master=nissan,
                        font=("JetBrains Mono",16),
                        state="disabled",
                        background="#4cc9f0",
                        foreground="gray7")
pagani_models = Combobox(master=pagani,
                        font=("JetBrains Mono",16),
                        state="normal",
                        values=pagani_names,
                        background="#4cc9f0",
                        foreground="gray7")

toyota_models.bind("<<ComboboxSelected>>",print1)
nissan_models.bind("<<ComboboxSelected>>",print2)
pagani_models.bind("<<ComboboxSelected>>",print3)

car_shop.pack()
toyota.pack()
pagani.pack()
nissan.pack()
toyota_models.grid(row=0,column=0)
nissan_models.grid(row=0,column=0)
pagani_models.grid(row=0,column=0)
car_shop.add(child=toyota,text="Toyota")
car_shop.add(child=nissan,text="Nissan")
car_shop.add(child=pagani,text="Pagani")

root.mainloop()

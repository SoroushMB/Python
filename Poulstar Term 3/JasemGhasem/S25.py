from tkinter import Label,Tk,Button,Frame,Spinbox,Toplevel
from tkinter.ttk import Notebook,Combobox

def print1(agree):
    if agree == "Yes":
        model = toyota_models.get()
        if model == "Prius":
            root1 = Toplevel()
            root1.mainloop()
        elif model == "Supra":
            print("Supra")
        elif model == "LandCruiser":
            print("LandCruiser")
        elif model == "Prado":
            print("Prado")
    else:
        pass
            
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

toyota_models = Spinbox(master=toyota,
                        font=("JetBrains Mono",16),
                        values=toyota_names,
                        background="#4cc9f0",
                        foreground="gray7")
nissan_models = Combobox(master=nissan,
                        font=("JetBrains Mono",16),
                        values=nissan_names,
                        background="#4cc9f0",
                        foreground="gray7")
pagani_models = Combobox(master=pagani,
                        font=("JetBrains Mono",16),
                        values=pagani_names,
                        background="#4cc9f0",
                        foreground="gray7")

toyota_models.bind("<Button-1>",lambda _:print1(agree="Yes"))
nissan_models.bind("<<ComboboxSelected>>",lambda _:print2())
pagani_models.bind("<<ComboboxSelected>>",lambda _:print3())

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

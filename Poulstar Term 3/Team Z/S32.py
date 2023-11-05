from tkinter import *

from json import load

from tkinter.ttk import Notebook,Combobox

def print1(event):

    print("1")

def print2(event):

    print("2")

def print3(event):

    print("3")

def continue1():
    
    toyota_models1=toyota_models.get()

    nissan_models1=nissan_models.get()

    pagani_models1=pagani_models.get()

    all=(pagani_models1,nissan_models1,toyota_models1)

    root.destroy()

    root1 = Tk()

    lbl2=Label(root1 , text=f"your final order : {all[0]},{all[1]},{all[2]}")

    money1=1000000

    lbl3=Label(root1 , text=f"money: {all[0][toyota_models1]+all[1][nissan_models1]+all[2][pagani_models1]}")

    lbl2.pack()

    lbl3.pack()

    root1.mainloop()

root=Tk()

root.title("car dealership")

btn = Button(root,text="continue",command=lambda:continue1())

car_shop = Notebook(master=root)

toyota = Frame(master=root,

    width = 400,

    height=600)

nissan = Frame(master = car_shop,
        width=400,
        height=600)

pagani = Frame(master = car_shop,
               width=400,
               height=600)

money=1000000

lbl1=Label(root , text=f"money: {money}")

toyota_names = ["Prius","Supra MK4","landCruiser","Prado",'GR Yaris']

nissan_names = ["leaf" , "gtr r34","370z","gtr r35", "x-trail"]

pagani_names=["zonda f ", "huayra", "zonda r" , "zonda cirque"]

toyota_models = Combobox(master=toyota,values=toyota_names)

nissan_models = Combobox(master=nissan,values=nissan_names)

pagani_models = Combobox(master=pagani,values=pagani_names)

toyota_models.bind("<<ComboboxSelected>>",print1)

nissan_models.bind("<<ComboboxSelected>>",print2)

pagani_models.bind("<<ComboboxSelected>>",print3)

car_shop.pack()

toyota.pack()

nissan.pack()

btn.pack()

lbl1.pack()

toyota_models.grid(row=0,column=0)

nissan_models.grid(row=0,column=0)

pagani_models.grid(row=0,column=0)

car_shop.add(child=toyota,text="toyota")

car_shop.add(child=nissan,text="nissan")

car_shop.add(child=pagani,text="pagani")

root.mainloop()
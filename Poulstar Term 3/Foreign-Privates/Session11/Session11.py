from tkinter import Tk,Label,Checkbutton,IntVar

def printing():
    if hamintori.get() == 0:
        print("Off")
    elif hamintori.get() == 1:
        print("On")

root = Tk()

hamintori = IntVar()
l1 = Label(master=root,text="Hello for first time!",font=("Consolas",20))
ckb1 = Checkbutton(master=root,
                   text="Print Something!",
                   onvalue=1,
                   offvalue=0,
                   variable=hamintori,
                   command=printing)

l1.pack()
ckb1.pack()
root.mainloop()
from tkinter import Tk,Button,Entry

def entering(btn):
    if btn == "ent":
        equation = e1.get()
        result = eval(equation)
        e1.delete(first=0,last=len(equation))
        e1.insert(index=0,string=result)
    elif btn == "del":
        e1.delete(first=0,last=len(e1.get()))
    else:
        e1.insert(index=len(e1.get()),string=btn)

counter = 0
def lock():
    global counter
    counter += 1
    if counter % 2 == 1:    
        l1.config(state="disabled",bg="red")
        l2.config(state="disabled",bg="red")
        l3.config(state="disabled",bg="red")
        l4.config(state="disabled",bg="red")
        l5.config(state="disabled",bg="red")
        l6.config(state="disabled",bg="red")
        l7.config(state="disabled",bg="red")
        l8.config(state="disabled",bg="red")
        l9.config(state="disabled",bg="red")
        l0.config(state="disabled",bg="red")
    else:
        l1.config(state="normal",bg="#42a7f5")
        l2.config(state="normal",bg="#42a7f5")
        l3.config(state="normal",bg="#42a7f5")
        l4.config(state="normal",bg="#42a7f5")
        l5.config(state="normal",bg="#42a7f5")
        l6.config(state="normal",bg="#42a7f5")
        l7.config(state="normal",bg="#42a7f5")
        l8.config(state="normal",bg="#42a7f5")
        l9.config(state="normal",bg="#42a7f5")
        l0.config(state="normal",bg="#42a7f5")
        
configurations_btn = {
    "padx" : 26,
    "pady" : 13,
    "bg" : "#0d1321",
    "fg" : "#f0ebd8",
    "font" : ("JetBrains Mono",15),
    "relief" : "raised",
    "border" : 20
}
configurations_ent = {
    "bg" : "#1d2d44",
    "fg" : "#f0ebd8",
    "font" : ("JetBrains Mono",20),
    "relief" : "sunken",
    "border" : 20
}

root = Tk()
root.resizable(0,0)
e1 = Entry(master=root,cnf=configurations_ent)
l1 = Button(master=root,text="1",cnf=configurations_btn,command=lambda:entering(btn="1"))
l2 = Button(master=root,text="2",cnf=configurations_btn,command=lambda:entering(btn="2"))
l3 = Button(master=root,text="3",cnf=configurations_btn,command=lambda:entering(btn="3"))
l4 = Button(master=root,text="4",cnf=configurations_btn,command=lambda:entering(btn="4"))
l5 = Button(master=root,text="5",cnf=configurations_btn,command=lambda:entering(btn="5"))
l6 = Button(master=root,text="6",cnf=configurations_btn,command=lambda:entering(btn="6"))
l7 = Button(master=root,text="7",cnf=configurations_btn,command=lambda:entering(btn="7"))
l8 = Button(master=root,text="8",cnf=configurations_btn,command=lambda:entering(btn="8"))
l9 = Button(master=root,text="9",cnf=configurations_btn,command=lambda:entering(btn="9"))
l0 = Button(master=root,text="0",cnf=configurations_btn,command=lambda:entering(btn="0"))
ldot = Button(master=root,text=".",cnf=configurations_btn,command=lambda:entering(btn="."))
lplu = Button(master=root,text="+",cnf=configurations_btn,command=lambda:entering(btn="+"))
lmin = Button(master=root,text="-",cnf=configurations_btn,command=lambda:entering(btn="-"))
lmul = Button(master=root,text="*",cnf=configurations_btn,command=lambda:entering(btn="*"))
ldiv = Button(master=root,text="/",cnf=configurations_btn,command=lambda:entering(btn="/"))
lnum = Button(master=root,text="nl",cnf=configurations_btn,command=lambda:lock())
lent = Button(master=root,text="ent",cnf=configurations_btn,command=lambda:entering(btn="ent"))
ldel = Button(master=root,text="del",cnf=configurations_btn,command=lambda:entering(btn="del"))

e1.grid(row=0, column=0, columnspan=4 ,sticky="nsew")
l1.grid(row=4, column=0, sticky="nsew")
l2.grid(row=4, column=1, sticky="nsew")
l3.grid(row=4, column=2, sticky="nsew")
l4.grid(row=3, column=0, sticky="nsew")
l5.grid(row=3, column=1, sticky="nsew")
l6.grid(row=3, column=2, sticky="nsew")
l7.grid(row=2, column=0, sticky="nsew")
l8.grid(row=2, column=1, sticky="nsew")
l9.grid(row=2, column=2, sticky="nsew")
l0.grid(row=5, column=0, columnspan=2 ,sticky="nsew")
ldot.grid(row=5, column=2, sticky="nsew")
lplu.grid(row=2, column=3, rowspan=2, sticky="nsew")
lmin.grid(row=1, column=3, sticky="nsew")
lmul.grid(row=1, column=2, sticky="nsew")
ldiv.grid(row=1, column=1, sticky="nsew")
lnum.grid(row=1, column=0, sticky="nsew")
lent.grid(row=4, column=3, rowspan=2, sticky="nsew")
ldel.grid(row=6, column=0, columnspan=4, sticky="nsew")
root.mainloop()

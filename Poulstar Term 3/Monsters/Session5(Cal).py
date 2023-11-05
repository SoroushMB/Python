from tkinter import Tk,Entry,Button,Toplevel,Label,END
from tkinter.messagebox import showinfo
from json import dump,load


settings = {
    "LBL" : {
        "fg" : "#d9d9d9",
        "bg" : "#284b63",
        "font" : ("JetBrains Mono",16),
        "relief" : "raised",
        "border" : 20,
        "justify" : "center"
    },
    "BTN" : {
        "fg" : "#d9d9d9",
        "bg" : "#274c77",
        "font" : ("JetBrains Mono",16),
        "relief" : "raised",
        "border" : 20,
        "justify" : "center"
    }
}

def Num0Com():
    HeadUpDisplay.insert(index=END,string="0")
def Num1Com():
    HeadUpDisplay.insert(index=END,string="1")
def Num2Com():
    HeadUpDisplay.insert(index=END,string="2")
def Num3Com():
    HeadUpDisplay.insert(index=END,string="3")
def Num4Com():
    HeadUpDisplay.insert(index=END,string="4")
def Num5Com():
    HeadUpDisplay.insert(index=END,string="5")
def Num6Com():
    HeadUpDisplay.insert(index=END,string="6")
def Num7Com():
    HeadUpDisplay.insert(index=END,string="7")
def Num8Com():
    HeadUpDisplay.insert(index=END,string="8")
def Num9Com():
    HeadUpDisplay.insert(index=END,string="9")
def PlusCom():
    HeadUpDisplay.insert(index=END,string="+")

def result():
    final = HeadUpDisplay.get()
    final_result = eval(final)
    HeadUpDisplay.delete(first=0,last=END)
    HeadUpDisplay.insert(index=END,string=f"{final_result}")
    HeadUpDisplay.config(state="readonly")
    
root = Tk()
root.title("Calculator(Babaei Edition)")
# root.state(newstate="zoomed")
HeadUpDisplay = Entry(master=root,state="normal",cnf=settings["LBL"])
Num0 = Button(master=root,text="0",cnf=settings["BTN"],command=Num0Com)
Num1 = Button(master=root,text="1",cnf=settings["BTN"],command=Num1Com)
Num2 = Button(master=root,text="2",cnf=settings["BTN"],command=Num2Com)
Num3 = Button(master=root,text="3",cnf=settings["BTN"],command=Num3Com)
Num4 = Button(master=root,text="4",cnf=settings["BTN"],command=Num4Com)
Num5 = Button(master=root,text="5",cnf=settings["BTN"],command=Num5Com)
Num6 = Button(master=root,text="6",cnf=settings["BTN"],command=Num6Com)
Num7 = Button(master=root,text="7",cnf=settings["BTN"],command=Num7Com)
Num8 = Button(master=root,text="8",cnf=settings["BTN"],command=Num8Com)
Num9 = Button(master=root,text="9",cnf=settings["BTN"],command=Num9Com)

NumLock = Button(master=root,text="num\nlock",cnf=settings["BTN"])
DivBtn = Button(master=root,text="/",cnf=settings["BTN"])
MulBtn = Button(master=root,text="*",cnf=settings["BTN"])
MinBtn = Button(master=root,text="-",cnf=settings["BTN"])
PluBtn = Button(master=root,text="+",cnf=settings["BTN"],command=PlusCom)
EntBtn = Button(master=root,text="E",cnf=settings["BTN"],command=result)
DotBtn = Button(master=root,text=".",cnf=settings["BTN"])

HeadUpDisplay.grid(row=0,column=0,columnspan=4,sticky="nsew")
Num0.grid(row=5,column=0,columnspan=2,sticky="nsew")
Num1.grid(row=4,column=0,sticky="nsew")
Num2.grid(row=4,column=1,sticky="nsew")
Num3.grid(row=4,column=2,sticky="nsew")
Num4.grid(row=3,column=0,sticky="nsew")
Num5.grid(row=3,column=1,sticky="nsew")
Num6.grid(row=3,column=2,sticky="nsew")
Num7.grid(row=2,column=0,sticky="nsew")
Num8.grid(row=2,column=1,sticky="nsew")
Num9.grid(row=2,column=2,sticky="nsew")

NumLock.grid(row=1,column=0,sticky="nsew")
DivBtn.grid(row=1,column=1,sticky="nsew")
MulBtn.grid(row=1,column=2,sticky="nsew")
MinBtn.grid(row=1,column=3,sticky="nsew")
PluBtn.grid(row=2,column=3,rowspan=2,sticky="nsew")
EntBtn.grid(row=4,column=3,rowspan=2,sticky="nsew")
DotBtn.grid(row=5,column=2,sticky="nsew")

root.mainloop()

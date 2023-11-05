from tkinter.ttk import Combobox
from tkinter import Tk,Label,Button,Toplevel,Entry,LabelFrame
from random import choice


def second_page():
    global mhr
    mhr = Tk()
    ali = LabelFrame(mhr,borderwidth=15)
    ali.grid(row=0,column=0)




    appel_combobx = ["k1","k1.25","k2.30","k3.35"]
    Bnanan_combobx= ["k1.30","k2.60","K3.90"]
    Strawberry_combobx= ["k1.40","k2.80","K3.120"]
    Garlic_combobx= ["k1.50","k2.100","K.150"]
    Cucumber_combobx = ["K1.15","K2.300","k3"]
    Lettuce_combobx= ["k1.2","k2.4","K3.100","k3.500"]
    Potato_combobx= ["k1.5","k2.10","K4.150"]
    tomato_combobx= ["k1.6","k2.12","K.18"]
    watermelon_combobx=["K3","K2.30","k4","k5"]
    Orange_combobx=["k1.50","k2","k2.600","k3","K3.90"]
    Pomegranate_Combobox=["k1.3","k2.200","K.15"]
    Mushroom_combobx=["k1.50","k2","k2.60","k3","K3.90"]
    Apricot_combobx= ["k1","k1.50","k2","k3","k3.40","k4","k4.300"]
    Cherry_combobx=["k1","k1.50","k2","k3","k3.40","k4","k4.700","k5.200"]
    carrot_combobx=["k1","k1.50","k2","k3","k3.400","k4","k4.700","k5.200","k6"]
    Fig_Combobx=["k1","k1.50","k2","k3","k3.400","k4","k4.700","k5.200","k6","k6.500"]
    Onion_combobx=["k1","k1.50","k2","k3","k3.400","k4","k4.700","k5.200","k6","k6.500","k7"]
    plum_combobx=["k1","k1.50","k2","k3","k3.400","k4","k4.700","k5.200","k6","k6.500","k7","k7.400"]
    Eggplant_combobx=["k1","k1.50","k2","k3","k3.400","k4","k4.700","k5.200","k6","k6.500","k7","k7.400","k8"]
    fenugreek_combobx=["k1","k1.50","k2","k3","k3.400","k4","k4.700","k5.200","k6","k6.500","k7","k7.400","k8","k8.350"]
    pineapple_combobx=["k1","k1.50","k2","k3","k3.400","k4","k4.700","k5.200","k6","k6.500","k7","k7.400","k8","k8.350","k8.400","k9"]
    pear_combobx=["k1","k1.50","k2","k3","k3.400","k4","k4.700","k5.200","k6","k6.500","k7","k7.400","k8","k8.350","k8.400","k9","k9.400","k10"]
    persimmon_combobx=["k1","k1.50","k2","k3","k3.400","k4","k4.700","k5.200","k6","k6.500","k7","k7.400","k8","k8.350","k8.400","k9.400","9.500","k10"]

    Appel_Label = Label(ali,text="Appel:سیب",font=("consolas",16))
    Appel_Label.grid(row=10,column=0)
    Appel_Combobox = Combobox(ali,values=appel_combobx,font="12")
    Appel_Combobox.grid(row=10,column=1)

    Mushroom_Label = Label(ali,text="Mushroom : قارچ",font=("consolas",16))
    Mushroom_Label.grid(row=10,column=2)
    Mushroom_Combobox = Combobox(ali,values=Mushroom_combobx,font="12")
    Mushroom_Combobox.grid(row=10,column=3)

    watermelon_Label = Label(ali,text="watermelon:هندوانه",font=("consolas",16))
    watermelon_Label.grid(row=9,column=0)
    watermelon_Combobox = Combobox(ali,values=watermelon_combobx,font="12")
    watermelon_Combobox.grid(row=9,column=1)

    orange_Label = Label(ali,text="Orange : پرتقال",font=("consolas",16))
    orange_Label.grid(row=8,column=0)
    orange_Combobox = Combobox(ali,values=Orange_combobx,font="12")
    orange_Combobox.grid(row=8,column=1)

    Pomegranate_Label = Label(ali,text="Pomegranate : انار",font=("consolas",16))
    Pomegranate_Label.grid(row=0,column=0)
    Pomegranate_Combobox = Combobox(ali,values=Pomegranate_Combobox,font="12")
    Pomegranate_Combobox.grid(row=0,column=1)

    Bnanan_Label = Label(ali,text="Bnanan:موز",font=("consolas",16))
    Bnanan_Label.grid(row=1,column=0)
    Bnanan_Combobox = Combobox(ali,values=Bnanan_combobx,font="12")
    Bnanan_Combobox.grid(row=1,column=1)

    Apricot_Label = Label(ali,text="Apricot : زردآلو",font=("consolas",16))
    Apricot_Label.grid(row=0,column=2)
    Apricot_Combobox = Combobox(ali,values=Apricot_combobx,font="12")
    Apricot_Combobox.grid(row=0,column=3)

    carrot_Label = Label(ali,text="carrot:هویچ",font=("consolas",16))
    carrot_Label.grid(row=2,column=2)
    carrot_Combobox = Combobox(ali,values=carrot_combobx,font="12")
    carrot_Combobox.grid(row=2,column=3)

    Fig_Label = Label(ali,text="Fig: انجیر",font=("consolas",16))
    Fig_Label.grid(row=3,column=2)
    Fig_Combobox = Combobox(ali,values=Fig_Combobx,font="12")
    Fig_Combobox.grid(row=3,column=3)

    Onion_Label = Label(ali,text="Onion:پیاز",font=("consolas",16))
    Onion_Label.grid(row=4,column=1)
    Onion_Combobox = Combobox(ali,values=Onion_combobx,font="12")
    Onion_Combobox.grid(row=3,column=1)

    plum_Label = Label(ali,text="plum:آلوچه",font=("consolas",16))
    plum_Label.grid(row=4,column=2)
    plum_Combobox = Combobox(ali,values=plum_combobx,font="12")
    plum_Combobox.grid(row=4,column=3)

    Eggplant_Label = Label(ali,text="Eggplant:بادمجان",font=("consolas",16))
    Eggplant_Label.grid(row=5,column=2)
    Eggplant_Combobox = Combobox(ali,values=Eggplant_combobx,font="12")
    Eggplant_Combobox.grid(row=5,column=3)

    fenugreek_Label = Label(ali,text="fenugreek:شنبلیله",font=("consolas",16))
    fenugreek_Label.grid(row=6,column=2)
    fenugreek_Combobox = Combobox(ali,values=fenugreek_combobx,font="12")
    fenugreek_Combobox.grid(row=6,column=3)

    pineapple_Label = Label(ali,text="pineapple:آناناس",font=("consolas",16))
    pineapple_Label.grid(row=7,column=2)
    pineapple_Combobox = Combobox(ali,values=pineapple_combobx,font="12")
    pineapple_Combobox.grid(row=7,column=3)

    pear_Label = Label(ali,text="pear:گلابی",font=("consolas",16))
    pear_Label.grid(row=8,column=2)
    pear_Combobox = Combobox(ali,values=pear_combobx,font="12")
    pear_Combobox.grid(row=8,column=3)

    persimmon_Label = Label(ali,text="persimmon:خُرمالو",font=("consolas",16))
    persimmon_Label.grid(row=9,column=2)
    persimmon_Combobox = Combobox(ali,values=persimmon_combobx,font="12")
    persimmon_Combobox.grid(row=9,column=3)

    Cherry_Label = Label(ali,text="cherry: گیلاس",font=("consolas",16))
    Cherry_Label.grid(row=1,column=2)
    Cherry_Combobox = Combobox(ali,values=Cherry_combobx,font="12")
    Cherry_Combobox.grid(row=1,column=3)

    Strawberry_Label = Label(ali,text="Strawberry:فرنگی توت",font=("consolas",16))
    Strawberry_Label.grid(row=2,column=0)
    Strawberry_Combobox = Combobox(ali,values=Strawberry_combobx,font="12")
    Strawberry_Combobox.grid(row=2,column=1)

    Garlic_Label = Label(ali,text="Garlic:سیر",font=("consolas",16))
    Garlic_Label.grid(row=3,column=0)
    Garlic_Combobox = Combobox(ali,values=Garlic_combobx,font="12")
    Garlic_Combobox.grid(row=3,column=1)

    Cucumber_Label = Label(ali,text="Cucumber:خیار",font=("consolas",16))
    Cucumber_Label.grid(row=4,column=0)
    Cucumber_Combobox = Combobox(ali,values=Cucumber_combobx,font="12")
    Cucumber_Combobox.grid(row=4,column=1)

    Lettuce_Label = Label(ali,text="Lettuce:کاهو",font=("consolas",16))
    Lettuce_Label.grid(row=5,column=0)
    Lettuce_Combobox = Combobox(ali,values=Lettuce_combobx,font="12")
    Lettuce_Combobox.grid(row=5,column=1)

    Potato_Label = Label(ali,text="Potato:زمینی سیب",font=("consolas",16))
    Potato_Label.grid(row=6,column=0)
    Potato_Combobox = Combobox(ali,values=Potato_combobx,font="12")
    Potato_Combobox.grid(row=6,column=1)

    tomato_Label = Label(ali,text="tomato:فرنگی خوجه ",font=("consolas",16))
    tomato_Label.grid(row=7,column=0)
    tomato_Combobox = Combobox(ali,values=tomato_combobx,font="12")
    tomato_Combobox.grid(row=7,column=1)

    Save_Button = Button(ali,text="Save",font=("consolas",16))
    Save_Button.grid(row=0,column=4)
    exit_Button = Button(ali,text="exit",font=("consolas",16),command=lambda:exit())
    exit_Button.grid(row=0,column=5)

def exit():
    mhr.destroy()
def Signin(btn):
    if btn == "Next":
        mainpage = Toplevel()
        mainpage.title("Sign in page")
        number1 = ["1","2","3","4","5","6","7","8","9"]        
        number2 = ["0","1","2","3","4","5","6","7","8","9"]
        number3 = ["0","1","2","3","4","5","6","7","8","9"]
        number4 = ["0","1","2","3","4","5","6","7","8","9"]
        number1Choice = choice(number1)
        number2Choice = choice(number2)
        number3Choice = choice(number3)
        number4Choice = choice(number4)
        Code = [f"{number1Choice}{number2Choice}{number3Choice}{number4Choice}"]
        CodeFile = open("Mehrbod 444.txt","a")
        CodeFile.write(30*"[....]")
        CodeFile.write(f"\nHi!\nUse:{Code}as Mehrbod Airlines account security code.")
        CodeFile.close()
        CodeLabel = Label(mainpage,text="Code",bg="#c9680e",fg="black",font=("Arial",16),height=1)
        CodeEntry = Entry(mainpage,font=("Arial",16))
        SinginButton = Button(mainpage,text="Sing in",bg="#0e97c9",fg="black",font=("Arial",18)
                            ,height=1,command=lambda:second_page())
        
        CodeLabel.grid(row=0 , column=0 , sticky="nsew")
        CodeEntry.grid(row=1 , column=0 , sticky="nsew")
        SinginButton.grid(row=2,column=0,sticky="nsew")

    elif btn == "sign":
        window = Toplevel()
        window.title("Sign in page")
        UserNameL = Label(window,text="Username",font=("Arila",18))
        PasswordL = Label(window,text="Password ",font=("Arila",18))
        UserNameE = Entry(window,font=("Arial",18))
        PasswordE = Entry(window,font=("Arial",18))
        NextSingnin = Button(window,text="Next",bg="#0e97c9",fg="black",font=("Arila",18),command=lambda:Signin("Next"))
    
        UserNameL.grid(row=0 , column=0 , sticky="nsew")
        PasswordL.grid(row=0 , column=1 , sticky="nsew")
        UserNameE.grid(row=1 , column=0 , sticky="nsew")
        PasswordE.grid(row=1 , column=1 , sticky="nsew")
        NextSingnin.grid(row=2 , column=0,columnspan=2, sticky="nsew")
        
        
        window.mainloop()





root = Tk()
root.title("Mehrbod king")

WelcomeLabel = Label(root,text="Welocme to fruit shop!",bg="#3266a8",fg="black",height=3,font=("Arial",15))
SighinButton = Button(root,text="Sign in",bg="#32a840",fg="black",height=1,font=("Arial",15),command=lambda:Signin("sign"))

WelcomeLabel.grid(row=0 , column=0 ,sticky="nsew")
SighinButton.grid(row=1 , column=0 ,sticky="nsew")


root.mainloop()

import turtle
t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor("black")

t.width(2)
t.speed(0)

col=('white','pink','cyan')

for i in range(300):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)
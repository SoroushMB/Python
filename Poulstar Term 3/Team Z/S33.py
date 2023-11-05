##########################IMPORT#########################

from tkinter import Label,Button,Text,Frame,Checkbutton,Tk,Toplevel,Entry
from tkinter.ttk import Combobox,Notebook
from tkinter.messagebox import showinfo
from os import system
from platform import system as sys

root1=Tk()
root1.geometry("790x330")
root1.title("keyword off me")
root1.config(bg="#424949")#808080
root1.resizable(0,0)

#########################################################

def terminal_cleaner():
    os_name = sys()
    if os_name == "Windows":
        system("cls")
    elif os_name == "Linux" or os_name == "Darwin":
        system("clear")
terminal_cleaner()

def keyboard(key):
    if key == "a":
        entry1.insert(index=len(entry1.get()),string="a")
    if key == "Clear":
        entry1.delete(first=len(entry1.get())-1,last=len(entry1.get()))
#################ENTRY###################

entry1=Entry(root1,font=("Product Sans Medium",16),border= 10,relief="sunken")

#####################BUTTON###########################

btn1=Button(root1,text="Tab",
bg="#808080",fg="gray1",
border=15)

btn2=Button(root1,text="Q",
bg="#808080",fg="gray1",
border=15)

btn3=Button(root1,text="W",
bg="#808080",fg="gray1",
border=15)

btn4=Button(root1,text="E",
bg="#808080",fg="gray1",
border=15)

btn5=Button(root1,text="R",
bg="#808080",fg="gray1",
border=15)

btn6=Button(root1,text="T",
bg="#808080",fg="gray1",
border=15)

btn7=Button(root1,text="Y",
bg="#808080",fg="gray1",
border=15)

btn8=Button(root1,text="U",
bg="#808080",fg="gray1",
border=15)

btn9=Button(root1,text="I",
bg="#808080",fg="gray1",
border=15)

btn10=Button(root1,text="O",
bg="#808080",fg="gray1",
border=15)

btn11=Button(root1,text="P",
bg="#808080",fg="gray1",
border=15)

btn12=Button(root1,text="SING",
bg="dodger blue",fg="gray1",
border=15,command=lambda:keyboard(key="Clear"))

btn13=Button(root1,text="Enter",
bg="#808080",fg="gray1",
border=15)

btn14=Button(root1,text="Shft",
bg="#808080",fg="gray1",
border=15)

btn15=Button(root1,text="A",
bg="#808080",fg="gray1",
border=15,command=lambda:keyboard("a"))

btn16=Button(root1,text="S",
bg="#808080",fg="gray1",
border=15)

btn17=Button(root1,text="D",
bg="#808080",fg="gray1",
border=15)

btn18=Button(root1,text="F",
bg="#808080",fg="#17202A",
border=15)

btn19=Button(root1,text="G",
bg="#808080",fg="#17202A",
border=15)

btn20=Button(root1,text="H",
bg="#808080",fg="#17202A",
border=15)

btn21=Button(root1,text="J",
bg="#808080",fg="#17202A",
border=15)

btn22=Button(root1,text="K",
bg="#808080",fg="#17202A",
border=15)

btn23=Button(root1,text="L",
bg="#808080",fg="#17202A",
border=15)

btn24=Button(root1,text="Z",
bg="#808080",fg="#17202A",
border=15)

btn25=Button(root1,text="X",
bg="#808080",fg="#17202A",
border=15)

btn27=Button(root1,text="C",
bg="#808080",fg="#17202A",
border=15)

btn28=Button(root1,text="V",
bg="#808080",fg="#17202A",
border=15)

btn29=Button(root1,text="B",
bg="#808080",fg="#17202A",
border=15)

btn30=Button(root1,text="N",
bg="#808080",fg="#17202A",
border=15)

btn31=Button(root1,text="M",
bg="#808080",fg="#17202A",
border=15)

btn32=Button(root1,text="</",
bg="#808080",fg="#17202A",
border=15)

btn33=Button(root1,text=">?",
bg="#808080",fg="#17202A",
border=15)

btn34=Button(root1,text="Shift",
bg="#808080",fg="#17202A",
border=15)

btn35=Button(root1,text="Ctrl",
bg="#808080",fg="#17202A",
border=15)

btn36=Button(root1,text="Alt",
bg="#808080",fg="#17202A",
border=15)

btn37=Button(root1,text="Space",
bg="#808080",fg="#17202A",
border=15)

btn38=Button(root1,text="Alt",
bg="#808080",fg="#17202A",
border=15)


#######################PLACE############################

entry1.place(x=10,
y=10,
height=50,width=500)

btn1.place(x=10,
y=70,
width=60,
height=60)

btn2.place(x=75,
y=70,
width=60,
height=60)

btn3.place(x=140,
y=70,
width=60,
height=60)

btn4.place(x=205,
y=70,
width=60,
height=60)

btn5.place(x=270,
y=70,
width=60,
height=60)

btn6.place(x=335,
y=70,
width=60,
height=60)

btn7.place(x=400,
y=70,
width=60,
height=60)

btn8.place(x=465,
y=70,
width=60,
height=60)

btn9.place(x=530,
y=70,
width=60,
height=60)
btn10.place(x=595,
y=70,
width=60,
height=60)

btn11.place(x=660,
y=70,
width=60,
height=60)

btn12.place(x=725,
y=70,
width=60,
height=60)

btn13.place(x=660,
y=135,
width=125,
height=60)

btn14.place(x=10,
y=135,
width=60,
height=125)

btn15.place(x=75,
y=135,
width=60,
height=60)

btn16.place(x=140,
y=135,
width=60,
height=60)

btn17.place(x=205,
y=135,
width=60,
height=60)

btn18.place(x=270,
y=135,
width=60,
height=60)

btn19.place(x=335,
y=135,
width=60,
height=60)

btn20.place(x=400,
y=135,
width=60,
height=60)

btn21.place(x=465,
y=135,
width=60,
height=60)

btn22.place(x=530,
y=135,
width=60,
height=60)

btn23.place(x=595,
y=135,
width=60,
height=60)

btn24.place(x=75,
y=200,
width=60,
height=60)

btn25.place(x=140,
y=200,
width=60,
height=60)

btn27.place(x=205,
y=200,
width=60,
height=60)

btn28.place(x=270,
y=200,
width=60,
height=60)

btn29.place(x=335,
y=200,
width=60,
height=60)

btn30.place(x=400,
y=200,
width=60,
height=60)

btn31.place(x=465,
y=200,
width=60,
height=60)

btn32.place(x=530,
y=200,
width=60,
height=60)

btn33.place(x=595,
y=200,
width=60,
height=60)

btn34.place(x=660,
y=200,
width=125,
height=60)

btn35.place(x=10,
y=265,
width=60,
height=60)

btn36.place(x=75,
y=265,
width=125,
height=60)

btn37.place(x=205,
y=265,
width=450,
height=60)

btn38.place(x=660,
y=265,
width=125,
height=60)

##########################!!!!FINISH!!!!##########################

root1.mainloop()


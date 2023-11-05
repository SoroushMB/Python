from tkinter import Button,Entry,LabelFrame,Toplevel,Tk,Label
from turtle import fd,lt,pencolor
root=Tk()
b=Tk()

def Harekatt(): 
    for i in range(3):
       fd(20)
    # lt(120)
    pencolor("green")
Harekat=Button(root,text="lets Go!",command=lambda:Harekatt(),bg="darkblue",fg='white').pack()
...
def moving_forward2():
    lt(10)
    # pencolor("pink")
jahat=Button(root,text="Jahat",command=lambda:moving_forward2(),bg="darkblue",fg="white").pack()
...
def moving_forward3():
    lt(-10)
    # pencolor("pink")
jahat_manfi=Button(root,text="Jahat_manfi",command=lambda:moving_forward3(),bg="darkblue",fg="white").pack()
...
def triangle():
        for i in range(4):
            fd(30)
            lt(120)
            pencolor("red")
mosalas = Button(root,text="Triangle",command=lambda:triangle(),bg="black",fg="white").pack()
...
def Square():
     for i in range(5):
        lt(90)
        fd(20)
        pencolor('blue')
morabae = Button(root,text="Square",command=lambda:Square(),bg="black",fg="white").pack()
...
entry1 = Entry(b)
def naming():
    label1=Label(b,text=f"Hi!{entry1.get()}",fg="white",bg="pink")
    label1.grid(row=1,column=0,columnspan=2,sticky="news")
button1 = Button(b,text=f"Whats your name?!",command=lambda:naming())

# -------GRID._.----------
button1.grid(row=0,column=1,sticky="news")
entry1.grid(row=0,column=0,sticky="news")

b.mainloop()
root.mainloop()
from tkinter import Tk,Button,Label,Entry
import os
os.system("cls")
root=Tk()
root.geometry('400x300')
root.title("jam.exe")
root['bg']="white"

entry1=Entry(root,width=20)
entry2=Entry(root,width=20)
def calc_jam():
    adad1=entry1.get()
    adad2=entry2.get()
    jvb=int(adad1)+int(adad2)
    eera= Label (root,text=jvb,font=("Arial",10))
    eera.grid(row=4,column=2)

def calc_menha():
    adad1=entry1.get()
    adad2=entry2.get()
    jvb=int(adad1)-int(adad2)
    eera= Label (root,text=jvb,font=("Arial",10))
    eera.grid(row=4,column=2)

def calc_zarb():
    adad1=entry1.get()
    adad2=entry2.get()
    jvb=int(adad1)*int(adad2)
    eera= Label (root,text=jvb,font=("Arial",10))
    eera.grid(row=4,column=2)

def calc_taghsim():
    adad1=entry1.get()
    adad2=entry2.get()
    jvb=int(adad1)/int(adad2)
    eera= Label (root,text=jvb,font=("Arial",10))
    eera.grid(row=4,column=2)
   

button1=Button(root,text="jam",width=15,height=1,font="Arial",command=lambda:calc_jam())
button2=Button(root,text="menha",width=15,height=1,font="Arial",command=lambda:calc_menha())
button3=Button(root,text="zarb",width=15,height=1,font="Arial",command=lambda:calc_zarb())
button4=Button(root,text="taghsim",width=15,height=1,font="Arial",command=lambda:calc_taghsim())
labelone=Label(root,text="first number",fg="red")
labeltwo=Label(root,text="second number",fg="red")
op=Label(root,text="Operator",fg="red")

labelone.grid(row=1,column=1)
entry1.grid(row=1,column=2)
labeltwo.grid(row=2,column=1)
entry2.grid(row=2,column=2)
op.grid(row=3,column=1)
button1.grid(row=4,column=1)
button2.grid(row=5,column=1)
button3.grid(row=6,column=1)
button4.grid(row=7,column=1)
root.mainloop()
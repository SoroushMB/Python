import os
import tkinter
from tkinter import*
os.system("cls")

def dokme(btn):
   global temp
   if btn=="up":
      temp +=1
      l2.config(text=str(temp)+"°C")
   elif btn=="down":
      temp -=1
      l2.config(text=str(temp)+"°C")
   if temp>=60:
      l3.config(text="Cooler on",bg="red")
   elif temp<60:
      l3.config(text="Cooler off",bg="grey")
temp=50
root=Tk()
root.geometry("160x100")

l1=Label(root,text="temp:",width=7,height=2,bg="grey",fg="black")
l2=Label(root,text=str(temp)+"°C",width=4,height=2,bg="grey",fg="black")
l3=Label(root,text="Cooler off",width=10,height=2,bg="grey",fg="black")
up=Button(root,text="up",width=4,height=1,bg="cyan",command=lambda:dokme("up"))
down=Button(root,text="down",width=4,height=1,bg="cyan",command=lambda:dokme("down"))

l1.grid(row=3,column=1)
l2.grid(row=3,column=2)
l3.grid(row=3,column=3)
up.grid(row=2,column=3)
down.grid(row=5,column=3)
root.mainloop()
# Tk , Label
# Entry
# Dynamic Variable : String , Integer , Boolean
# StringVar , IntVar , BooleanVar
from tkinter import Tk,Label,Entry,StringVar

root = Tk()

l1 = Label(master=root,text="Hello",font=("JetBrains Mono",18))
e1 = Entry(master=root,width=60,font=("JetBrains Mono",16))
user_age = e1.get()
l2 = Label(master=root,text=f"Age : {user_age}",font=("JetBrains Mono",16))

l1.pack()
l2.pack()
e1.pack()

root.mainloop()
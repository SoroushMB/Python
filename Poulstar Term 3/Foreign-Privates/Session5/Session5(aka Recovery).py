from tkinter import Label,Entry,Button,Tk
# Widgets : Label , Entry , Button , ...
root = Tk()
root.geometry("400x300")
root.config(background="black")

l1 = Label(master=root,text="Hello, Maya!",font=("Consolas",16),bg="darkred",fg="white")
l2 = Label(root,text="Hello, Artin!",font=("Consolas",16),bg="darkgreen",fg="white")
l3 = Label(root,text="Hello, AryoBarzan!",font=("Consolas",16),bg="darkblue",fg="white")

l1.grid(row=0,column=0,sticky="wens")
l2.grid(row=1,column=0,sticky="wens")
l3.grid(row=2,column=0,sticky="wens")
root.mainloop()
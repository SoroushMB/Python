from tkinter import Tk,Label,Button,Entry
from tkinter.messagebox import showinfo

root = Tk()

def main():
    showinfo(message=f"Result : {int(e1.get())+ int(e2.get())}")

configs = {
    "font":("JetBrains Mono",16),
    "bg":"yellow",
    "fg":"black",
    "relief":"raised",
    "border":20
}
l1 = Label(master=root,text="Number 1",cnf=configs)
l2 = Label(master=root,text="Number 2",cnf=configs)
b1 = Button(master=root,text="Show!",font=("JetBrains Mono",16),bg="blue",fg="white",relief="ridge",border=20,command=main)
e1 = Entry(master=root,font=("JetBrains Mono",16),show="*",bg="red",fg="black",relief="sunken",border=20)
e2 = Entry(master=root,font=("JetBrains Mono",16),show="*",bg="red",fg="black",relief="sunken",border=20)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
b1.grid(row=2,column=0,columnspan=2,sticky="nsew")

root.mainloop()
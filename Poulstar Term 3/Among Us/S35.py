from tkinter import Tk,Entry,Label,Button
from tkinter.messagebox import showinfo
def main():
    real_equation = eval(real.get())
    showinfo(message=f"Result : {real_equation}")

root = Tk()

Equation = Label(master=root,text="Equation : ",font=("JetBrains Mono",18),relief="raised",border=20).grid(row=0,column=0,sticky="nsew")
real = Entry(master=root,font=("JetBrains Mono",18),relief="raised",border=20)
Showing = Button(master=root,text="Showing",font=("JetBrains Mono",18),relief="raised",border=20,command=main)
Showing.grid(row=1,column=0,columnspan=2,sticky="nsew")
real.grid(row=0,column=1,sticky="nsew")
root.mainloop()
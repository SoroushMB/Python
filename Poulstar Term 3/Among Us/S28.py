from tkinter import Tk,Toplevel,Button,Label

def alaki():
    win = Toplevel()
    win.geometry("200x70+0+0")
    l1plus = Label(win,text="Didi chi shod!!!",font=("VT323",22))
    l1plus.grid(row=0,column=0,sticky="nsew")
    
root = Tk()
l1 = Label(root,text="Salam! Dokme ro feshar bede!",font=("VT323",22))
b1 = Button(root,text="Mano befeshar!",relief="raised",fg="white",border=20,bg="#559977",font=("VT323",22),padx=10,pady=10,command=lambda:alaki())

l1.grid(row=1,column=0,sticky="nsew")
b1.grid(row=0,column=0,sticky="nsew")
root.mainloop()
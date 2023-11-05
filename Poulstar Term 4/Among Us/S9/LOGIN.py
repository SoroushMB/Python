from tkinter import Entry,Tk,Label,Checkbutton,Button
root = Tk()

a = Label(text="username:",master=root,font=("VT323"))
b = Label(root,text="password:",font=("VT323"))
c = Button(root,text="register")
d = Button(root,text="login")
e = Button(root,text="cancel")
f = Entry(root)
g = Entry(root)


a.grid(row=2,column=1)
b.grid(row=3,column=1)
c.grid(row=2,column=4)
d.grid(row=3,column=4)
e.grid(row=3,column=3)
f.grid(row=3,column=4)
g.grid(row=4,column=3)






root.mainloop()
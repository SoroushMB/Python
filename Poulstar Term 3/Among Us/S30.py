# Notebook
from tkinter import Tk,Label,Button,Entry,Frame
from tkinter.ttk import Notebook

root = Tk()
spy_x_family = Notebook(master=root)
spy_x_family.pack(pady=10, expand=True)

anya = Frame(master=spy_x_family,width=600,height=400)
yor = Frame(master=spy_x_family,width=600,height=400)
loid = Frame(master=spy_x_family,width=600,height=400)
bond = Frame(master=spy_x_family,width=600,height=400)

anya.pack(fill="both",expand=True)
yor.pack(fill="both",expand=True)
loid.pack(fill="both",expand=True)
bond.pack(fill="both",expand=True)

anya_label = Label(master=anya,text="I know you know but he doesn't know that you know that I know!",font=("JetBrains Mono",16),bg="dark khaki",fg="DeepSkyBlue4",relief="raised",border=20)
yor_label = Label(master=yor,text="I know you know but he doesn't know that you know that I know!",font=("JetBrains Mono",16),bg="CadetBlue4",fg="blue2",relief="raised",border=20)
loid_label = Label(master=loid,text="I know you know but he doesn't know that you know that I know!",font=("JetBrains Mono",16),bg="IndianRed3",fg="DarkGoldenrod1",relief="raised",border=20)
bond_label = Label(master=bond,text="I know you know but he doesn't know that you know that I know!",font=("JetBrains Mono",16),bg="darkgreen",fg="DeepSkyBlue2",relief="raised",border=20)

spy_x_family.add(child=anya,text="Anya",image="Android.jpg")
spy_x_family.add(child=yor,text="Yor",image="Android.jpg")
spy_x_family.add(child=loid,text="Loid",image="Android.jpg")
spy_x_family.add(child=bond,text="Bond",image="Android.jpg")

anya_label.grid(row=0,column=0,sticky="nsew")
yor_label.grid(row=0,column=0,sticky="nsew")
loid_label.grid(row=0,column=0,sticky="nsew")
bond_label.grid(row=0,column=0,sticky="nsew")

root.mainloop()
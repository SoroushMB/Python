from tkinter import Label,Button,Entry,Tk

window = Tk()
window.title("Nemidunam")
# window.state("zoomed")
# window.resizable(1,1)
window.config(background="SlateBlue3")
# window.geometry("400x300+0+0")

nemidunam0 = Label(master=window,text="Hello,World!",fg="goldenrod",bg="#42f5bc",font=("Product Sans Medium",22),relief="raised",border=40)
nemidunam1 = Label(master=window,text="Hello,World!",fg="goldenrod",bg="SlateBlue4",font=("Product Sans Medium",22),relief="ridge",border=40)
nemidunam2 = Label(master=window,text="Hello,World!",fg="goldenrod",bg="SlateBlue4",font=("Product Sans Medium",22),relief="groove",border=40)
nemidunam3 = Label(master=window,text="Hello,World!",fg="goldenrod",bg="SlateBlue4",font=("Product Sans Medium",22),relief="flat",border=40)
nemidunam4 = Label(master=window,text="Hello,World!",fg="goldenrod",bg="SlateBlue4",font=("Product Sans Medium",22),relief="sunken",border=40)
nemidunam5 = Label(master=window,text="Hello,World!",fg="goldenrod",bg="SlateBlue4",font=("Product Sans Medium",22),relief="solid",border=40)

nemidunam0.grid(row=0,column=0)
nemidunam1.grid(row=1,column=0)
nemidunam2.grid(row=2,column=0)
nemidunam3.grid(row=3,column=0)
nemidunam4.grid(row=4,column=0)
nemidunam5.grid(row=5,column=0)

window.mainloop()
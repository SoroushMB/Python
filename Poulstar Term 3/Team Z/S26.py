from tkinter import Tk, Label, Button, Entry,Checkbutton

root = Tk()
# Relieves : Sunken , Groove , Ridge , Raised , Solid , Flat
# root.geometry("300x400+100+300")
root.title("Morris")
root.resizable(1, 1)
# root.state("zoomed")
root.config(background="#008C8C")
namel = Label(
    master=root,
    text="AMD®",
    bg="red",
    fg="black",
    width=5,
    height=1,
    font=("Product Sans Medium", 30),
    relief="sunken",
    border=100,
)
nameb = Button(
    master=root,
    text="AMD®",
    bg="red",
    fg="black",
    width=5,
    height=1,
    font=("Product Sans Medium", 30),
    relief="raised",
    border=100,
    command=lambda: print("Hey Nigga!"),
)
namee = Entry(
    master=root,
    bg="red",
    fg="black",
    width=10,
    font=("Product Sans Medium", 30),
    relief="raised",
    border=100,
)
ckb1 = Checkbutton(master=root,text="Alaki!")
ckb2 = Checkbutton(master=root,text="Alaki!")

namee.insert(string="Saman", index=0)
namel.pack()
nameb.pack()
namee.pack()
ckb1
ckb2
root.mainloop()

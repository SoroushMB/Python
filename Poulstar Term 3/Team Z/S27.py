from tkinter import Button,Tk,Entry,Label,Frame
from tkinter.ttk import Notebook

def calculator():
    equation = importer.get()
    if "x" in equation:
        equation = equation.replace("x","*")
    elif "X" in equation:
        equation = equation.replace("X","*")
    finalist = eval(f"{equation}")
    showman.config(text=f"Result : {finalist}")

root = Tk()
root.config(background="azure")

prime = Notebook(master=root)
gatherer = Frame(master=prime,bg="azure")
fake_gatherer = Frame(master=prime,bg="azure")

showman = Label(master=gatherer,
                                    text="You will see the result here!",
                                    font=("Product Sans Medium",16),
                                    bg="lavender",
                                    fg="gray10",
                                    relief="raised",
                                    border=20)
actor = Button(master=gatherer,
                               text="Tab to see!",
                               font=("Product Sans Medium",16),
                               bg="gainsboro",
                               width=22,
                               fg="gray10",
                               relief="raised",
                               border=20,
                               command=lambda:calculator())
importer = Entry(master=gatherer,
                                   font=("Product Sans Medium",16),
                                   bg="gainsboro",
                                   fg="gray10",
                                   relief="raised",
                                   border=20)

prime.grid(row=0,column=0,sticky="nsew",columnspan=2)
gatherer.pack(fill='both', expand=True)
fake_gatherer.pack(fill='both', expand=True)
showman.grid(row=0,column=0,sticky="nsew",columnspan=2)
actor.grid(row=1,column=0,sticky="nsew")
importer.grid(row=1,column=1,sticky="nsew")

prime.add(gatherer, text="Simple Calculator")
prime.add(fake_gatherer, text="Hamintori!")

root.mainloop()
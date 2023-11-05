from tkinter import Tk,Label,Entry,Button
# Widgets : Label,Entry,Checkbutton,Radiobutton,...
def sum():
    shomare1 = int(number1.get())
    shomare2 = int(number2.get())
    result = shomare1 + shomare2
    name_l.config(text=f"Natijeh : {result}")

win = Tk()
# win.geometry("200x150+700+200")
win.title("Samiar")
win.config(background="#008C8C")

name_l = Label(master=win,
                            text="Hello, World!",
                            bg="#69c8d6",
                            fg="black",
                            font=("Product Sans Medium",20),
                            border=20,
                            width=10,
                            height=3,
                            relief="groove")
nameb1 = Button(master=win,
                            text="Hello, World!",
                            bg="#008C8C",
                            fg="black",
                            font=("Product Sans Medium",20),
                            border=20,
                            width=10,
                            height=3,
                            relief="raised",
                            command=lambda: print("Hello, Everybody1!"))
nameb2 = Button(master=win,
                            text="Hello, World!",
                            bg="#69c8d6",
                            fg="black",
                            font=("Product Sans Medium",20),
                            border=20,
                            width=10,
                            height=3,
                            relief="raised",
                            command=lambda: sum())
number1 = Entry(master=win,
                            bg="#ff6054",
                            fg="black",
                            font=("Product Sans Medium",20),
                            border=20,
                            width=10,
                            relief="raised")
number2 = Entry(master=win,
                            bg="#ff6054",
                            fg="black",
                            font=("Product Sans Medium",20),
                            border=20,
                            width=10,
                            relief="raised")
name_l.grid()
nameb1.grid()
nameb2.grid()
number1.grid()
number2.grid()
win.mainloop()
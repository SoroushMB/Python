from tkinter import Tk,Label,Entry,Button
# Widgets : Label,Entry,Checkbutton,Radiobutton,...
win = Tk()
# win.geometry("200x150+700+200")
win.title("Samiar")
win.config(background="#008C8C")

name = Label(master=win,
                            text="Hello, World!",
                            bg="#008C8C",
                            fg="black",
                            font=("Product Sans Medium",20),
                            border=20,
                            width=10,
                            height=3,
                            relief="groove")

name.grid(row=0,column=0)
win.mainloop()
from tkinter import Tk,Label,Button,Entry

win = Tk()
win.geometry("300x400+0+100")
# win.state("zoomed")
win.resizable(1,1)
win.config(background="#ffffff")

name = Label(master=win,
                            text="Hello, Haj Taha!",
                            font=("Product Sans Medium",20),
                            bg="#008c8c",
                            fg="white",
                            border=20,
                            relief="sunken",
                            width=20,
                            height=10)
name.pack()
win.mainloop()
from tkinter import Tk,Label,Button,Entry
win = Tk()
win.geometry("600x600+0+0")
# win.state("zoomed")
win.resizable(0,1)
win.title("Sam")
=>
win.config(background="orchid1")
alaki_l = Label(master=win,
                        text="Hello Hamintori!🗿",
                        font=("Product Sans Medium",20),
                        bg="mediumorchid1",
                        fg="plum1",
                        relief="ridge",
                        border=30)
alaki_b = Button(master=win,
                        text="Hello Hamintori!🗿",
                        font=("Product Sans Medium",20),
                        bg="mediumorchid1",
                        fg="plum1",
                        relief="ridge",
                        border=30,
                        command=lambda: print("Hello Everybody!"))
alaki_e = Entry(master=win,
                        font=("Product Sans Medium",20),
                        bg="mediumorchid1",
                        fg="plum1",
                        relief="ridge",
                        border=30)
alaki_l.grid()
alaki_b.grid()
alaki_e.grid()
win.mainloop()


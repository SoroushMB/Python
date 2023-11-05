from tkinter import Tk,Label,Button,Entry

window = Tk()
# window.geometry("400x300+0+0")
window.title("Hi!🗿")
# window.state("zoomed")
# window.iconify()
window.resizable(True,False)
window.config(bg="#10002b")

alaki_l = Label(master=window,
                text="Hello, NPCs!",
                font=("Product Sans Medium",20),
                bg="#e0aaff",
                fg="#f0e6ef",
                relief="raised",
                border=40,
                padx=20,
                pady=20)
alaki_b = Button(master=window,
                text="Hello, NPCs!",
                font=("Product Sans Medium",20),
                bg="#e0aaff",
                fg="#f0e6ef",
                relief="raised",
                border=40,
                padx=20,
                pady=20,
                command=lambda:print("Didi mano zadi!"))
alaki_e = Entry(master=window,
                font=("Product Sans Medium",20),
                bg="#e0aaff",
                fg="#f0e6ef",
                relief="raised",
                border=40
                )
name = alaki_e.get()
alaki_l.pack()
alaki_b.pack()
alaki_e.pack()
window.mainloop()
from tkinter import Tk,Label

window = Tk()
window.geometry("400x300+0+0")
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
                )
alaki_l.pack()
window.mainloop()
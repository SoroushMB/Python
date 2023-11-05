from tkinter import *
from PIL import Image,ImageTk

win = Tk()

hamintori = Canvas(master=win,width=400,height=600)

moch = ImageTk.PhotoImage(file="Nissan.jpg")

hamintori.create_image(100,200,image=moch,anchor="center")

hamintori.pack()

win.mainloop()
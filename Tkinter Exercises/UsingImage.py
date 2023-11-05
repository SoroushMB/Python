from tkinter import Tk,Frame,Label
from PIL import ImageTk, Image

win = Tk()
win.geometry("300x300")

frame = Frame(win, width=200, height=200)
frame.pack()
frame.place(anchor='center',relx=0.5,rely=0.5)

example_img = ImageTk.PhotoImage(Image.open("C:\Users\DELL\Documents\Codes\Python\Tkinter Exercises\images.jpg"))
placing = Label(frame, image=example_img)
placing.pack()

win.mainloop()
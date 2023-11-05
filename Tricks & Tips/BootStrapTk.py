from ttkbootstrap import Button,Label
from tkinter import Tk
root = Tk()

l1 = Label(master=root,text="Hello,World!")
b1 = Button(master=root,text="Click Me!")
l1.pack()
b1.pack()
root.mainloop()
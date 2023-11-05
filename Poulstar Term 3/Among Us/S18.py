from tkinter import Label,Tk,PhotoImage

root = Tk()

image1 = PhotoImage(file="image.jpg")
l1 = Label(root,image=image1)

l1.pack()
root.mainloop()
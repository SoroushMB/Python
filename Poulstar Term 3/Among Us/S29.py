from PIL import Image, ImageTk
from tkinter import Frame,Label,Tk

window = Tk()
# window.geometry("700x500")
zrame = Frame(master=window,width=600,height=400,relief="raised",border=30,bg="gray50")
zrame.pack()

photo = ImageTk.PhotoImage(Image.open("Android.jpg"))
real_photo1 = Label(master=zrame,image=photo,relief="raised",border=30)
real_photo2 = Label(master=zrame,image=photo,relief="raised",border=30)

real_photo1.grid(row=0,column=0)
real_photo2.grid(row=0,column=1)
window.mainloop()
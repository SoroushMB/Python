from tkinter import Tk,Label
root=Tk()
root.geometry("800x300")
root.config(bg="black")
root.resizable(0,0)
lbl=Label(master=root,text="salam",bg="purple",fg="white"
)
lbl.grid(row=0,column=0)
root.mainloop()

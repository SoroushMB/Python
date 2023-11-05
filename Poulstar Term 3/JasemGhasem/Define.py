from tkinter import Tk,Button

def alaki():
    root.iconify()
    new_root = Tk()
    new_root.mainloop()
    
root = Tk()

hamintori = Button(master=root,text="Click to show!",command=lambda:alaki())

hamintori.pack()

root.mainloop()
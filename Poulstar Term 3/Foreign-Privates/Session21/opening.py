from tkinter import Tk,Toplevel,Label,Button

def new_window():
    second_page = Toplevel()
    l1 = Label(master=second_page,text="Just for test!",fg="white",bg="black",font=("JetBrains Mono",16),relief="ridge",border=20)
    l1.pack()
    second_page.mainloop()
    
root = Tk()

l1 = Label(master=root,text="Just for test!",fg="white",bg="black",font=("JetBrains Mono",16),relief="ridge",border=20)
b1 = Button(master=root,text="Just for test!",fg="white",bg="black",font=("JetBrains Mono",16),relief="raised",border=20,command=new_window)

l1.pack()
b1.pack()

root.mainloop()
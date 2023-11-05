# Bind
# JavaScript Object Notation (JSON)
from tkinter import Tk,Label,Button,Entry
from tkinter.messagebox import showerror

def main():
    try:
        phonenumber = int(e1.get())
        phonenumber = str(e1.get())
        print(phonenumber)
    except ValueError:
        showerror(message="You have entered a wrong format of phone number!")

root = Tk()

l1 = Label(master=root,text="Phonenumber: ",bg="sky blue",fg="black",font=("JetBrains Mono",16))
b1 = Button(master=root,text="Press to show!",bg="navy",fg="white",font=("JetBrains Mono",16),command=main)
e1 = Entry(master=root,bg="sky blue",fg="black",font=("JetBrains Mono",16))


l1.grid(row=0,column=0,sticky="nsew")
e1.grid(row=0,column=1,sticky="nsew")
b1.grid(row=1,column=0,columnspan=2,sticky="nsew")

root.mainloop()
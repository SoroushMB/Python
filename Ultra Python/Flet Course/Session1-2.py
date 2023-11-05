from tkinter import Label,Button,Tk
from random import choice

counter = 0
colors = ["Red","Green","Blue"]
def main():
    global counter
    counter += 1
    l1.config(text=counter,bg=choice(colors))
    
root = Tk()

l1 = Label(master=root,text=0,bg="black",fg="white",font=("JetBrains Mono",18))
b1 = Button(master=root,text="Press to show!",bg="black",fg="white",font=("JetBrains Mono",18),command=main)
l1.pack()
b1.pack()

root.mainloop()
from tkinter import Label,Tk
from datetime import date
root = Tk()
root.title("Artin's Project")

l1 = Label(master=root,
           text=f"Today's date is {date.today()}",
           font=("JetBrains Mono",20),
           bg="black",
           fg="skyblue",
           relief="raised",
           border=40,
           padx=20,
           pady=20)

l1.pack()
root.mainloop()
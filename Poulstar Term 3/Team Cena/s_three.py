"""
Something alaki
"""
from tkinter import Tk, Label

config = {
    "font": ("JetBrains Mono", 20),
    "bg": "black",
    "fg": "#eae0d5",
    "border": 20,
    "relief": "raised"
}
root = Tk()
root.title("--Member ID--")

name = Label(master=root, text="Name : Soroush", cnf=config)
age = Label(master=root, text="Age : 21", cnf=config)
phone_number = Label(
    master=root, text="Phone number : 09039851230\nHome number : 013-34911", cnf=config)

name.grid(row=0, column=0, sticky="ew")
age.grid(row=1, column=0, sticky="ew")
phone_number.grid(row=2, column=0, sticky="ew")

root.mainloop()

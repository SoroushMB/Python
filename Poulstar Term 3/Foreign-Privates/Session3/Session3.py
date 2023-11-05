# Name - Phonenumber - Age
from tkinter import Tk,Label

age = input("How old are you: ")
phone_number = input("What is your number: ")
name = input("What is your name: ")

root = Tk()

agel = Label(root, text=f"Age: {age}")
phone_numberl = Label(root, text=f"Phonenumber: {phone_number}")
namel = Label(root, text=f"Name: {name}")

namel.pack()
phone_numberl.pack()
agel.pack()

root.mainloop()
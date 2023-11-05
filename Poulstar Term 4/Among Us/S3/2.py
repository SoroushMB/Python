from ralph import Car_Maker
from tkinter import Tk, Label

user_input = input("What do you want do?(If you want help, just type 'help'!) ").lower()

if "help" in user_input:
    print(Car_Maker.__doc__)
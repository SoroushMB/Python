from USA import *
from tkinter import Tk,Label
from random import choice

main_win = Tk()
cities = choice((California.capital(),New_York.capital(),Florida.capital()))
city_p1 = Label(master=main_win,
                text="City : ",
                relief="raised",
                bg="darkblue",
                fg="white",
                border=20,
                font=("Product Sans Medium",20))
city_p2 = Label(master=main_win,
                text=f"{cities}",
                relief="raised",
                bg="darkred",
                fg="white",
                border=20,
                font=("Product Sans Medium",20))
city_p1.grid(row=0 ,column=0)
city_p2.grid(row=0 ,column=1)
main_win.mainloop()
# Movies 
from tkinter import Tk,Label,Entry,Button,Toplevel

def another_page():
    secondary_page = Toplevel()
    intro_label = Label(master=secondary_page,
                        text=f"Hi, {first_name_entry.get()} {last_name_entry.get()}!",
                        font=("Product Sans Medium",16),
                        bg="#f8ad9d",
                        fg="gray10",
                        width=32,
                        relief="raised",
                        border=20)
    movie_name_label = Label(master=secondary_page,
                        text="Name : ",
                        font=("Product Sans Medium",16),
                        bg="#f8ad9d",
                        fg="gray10",
                        width=14,
                        relief="raised",
                        border=20)
    movie_year_label = Label(master=secondary_page,
                        text="Year : ",
                        font=("Product Sans Medium",16),
                        bg="#f8ad9d",
                        fg="gray10",
                        width=14,
                        relief="raised",
                        border=20)
    movie_producer_label = Label(master=secondary_page,
                        text="Producer : ",
                        font=("Product Sans Medium",16),
                        bg="#f8ad9d",
                        fg="gray10",
                        width=14,
                        relief="raised",
                        border=20)
    movie_cast_label = Label(master=secondary_page,
                        text="Cast : ",
                        font=("Product Sans Medium",16),
                        bg="#f8ad9d",
                        fg="gray10",
                        width=14,
                        relief="raised",
                        border=20)
    movie_score_label = Label(master=secondary_page,
                        text="Score : ",
                        font=("Product Sans Medium",16),
                        bg="#f8ad9d",
                        fg="gray10",
                        width=14,
                        relief="raised",
                        border=20)
    intro_label.grid(row=0,column=0,columnspan=2,sticky="nsew")
    movie_name_label.grid(row=1,column=0,sticky="nsew")
    movie_year_label.grid(row=2,column=0,sticky="nsew")
    movie_producer_label.grid(row=3,column=0,sticky="nsew")
    movie_cast_label.grid(row=4,column=0,sticky="nsew")
    movie_score_label.grid(row=5,column=0,sticky="nsew")
    secondary_page.mainloop()
    
main_page = Tk()
main_page.title("Movies")

first_name_label = Label(master=main_page,
                        text="First name : ",
                        font=("Product Sans Medium",16),
                        bg="#f8ad9d",
                        fg="gray10",
                        width=14,
                        relief="raised",
                        border=20)
last_name_label = Label(master=main_page,
                        text="Last name : ",
                        font=("Product Sans Medium",16),
                        bg="#f8ad9d",
                        fg="gray10",
                        width=14,
                        relief="raised",
                        border=20)
first_name_entry = Entry(master=main_page,
                        font=("Product Sans Medium",16),
                        bg="#ffe6a7",
                        fg="gray10",
                        relief="raised",
                        width=18,
                        border=20)
last_name_entry = Entry(master=main_page,
                        font=("Product Sans Medium",16),
                        bg="#ffe6a7",
                        fg="gray10",
                        relief="raised",
                        width=18,
                        border=20)
open_button = Button(master=main_page,
                    text="Tap to open!",
                    font=("Product Sans Medium",16),
                    bg="#ffe6a7",
                    fg="gray10",
                    relief="raised",
                    width=18,
                    border=20,
                    command=lambda:another_page())

first_name_label.grid(row=0 ,column=0 ,sticky="nsew")
last_name_label.grid(row=1 ,column=0 ,sticky="nsew")
first_name_entry.grid(row=0 ,column=1 ,sticky="nsew")
last_name_entry.grid(row=1 ,column=1 ,sticky="nsew")
open_button.grid(row=2,column=0,columnspan=2,sticky="nsew")
main_page.mainloop()
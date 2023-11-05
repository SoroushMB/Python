from tkinter import Tk,Label,Button,Entry,Frame
from tkinter.ttk import Combobox
from json import load

lbl_configs = {
    "bg" : "#7cfcb5",
    "fg" : "black",
    "font" : ("Product Sans Medium",16),
    "relief" : "groove",
    "border" : 20,
    "compound" : "left"
}

root = Tk()
root.title("Spotify Khodemuni!")

parent1 = Frame(master=root)
parent2 = Frame(master=root)

artist_lbl = Label(master=parent1,text="Artist: ",cnf=lbl_configs)
songs_lbl = Label(master=parent1,text="Songs: ",cnf=lbl_configs)
year_lbl = Label(master=parent1,text="Year: ",cnf=lbl_configs)

parent1.grid(row=0 ,column=0 ,sticky="nsew")
parent2.grid(row=0 ,column=1 ,sticky="nsew")
artist_lbl.grid(row=0 ,column=0 ,sticky="nsew")
songs_lbl.grid(row=1 ,column=0 ,sticky="nsew")
year_lbl.grid(row=2 ,column=0 ,sticky="nsew")

root.mainloop()
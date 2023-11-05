from tkinter import Label,Tk,Entry,Button
from tkinter.ttk import Combobox
import json

def selected_singer(event):
    singer = singers_cbx.get()
    if singer == "Sia":
        songs_cbx.config(values=singers_and_songs["Sia"],state="readonly")
        platforms_cbx.config(state="readonly",values=platforms)
    elif singer == "Modern Talking":
        songs_cbx.config(values=singers_and_songs["Modern Talking"],state="readonly")
        platforms_cbx.config(state="readonly",values=platforms)
    elif singer == "Ice Cube":
        songs_cbx.config(values=singers_and_songs["Ice Cube"],state="readonly")
        platforms_cbx.config(state="readonly",values=platforms)

with open("SingersInfo.json","r") as file:
    singers_and_songs = json.load(file)

lbl_configs = {
    "width": 11,
    "font":("Gotham-Medium",16),
    "relief":"raised",
    "border":20,
    "bg":"#1db954",
    "fg":"#ffffff"
}
platforms = ["SoundCloud","Apple Music","Spotify","YouTube Music","Tidal"]
main_win = Tk()

singer_lbl = Label(master=main_win,text="Singer : ",cnf=lbl_configs)
song_lbl = Label(master=main_win,text="Song : ",cnf=lbl_configs)
platform_lbl = Label(master=main_win,text="Platform : ",cnf=lbl_configs)
type_lbl = Label(master=main_win,text="Type : ",cnf=lbl_configs)

singers_cbx = Combobox(master=main_win,values=tuple(singers_and_songs.keys()),font=("Gotham-Medium",16))
songs_cbx = Combobox(master=main_win,state="disabled",font=("Gotham-Medium",16))
platforms_cbx = Combobox(master=main_win,values=platforms,state="disabled",font=("Gotham-Medium",16))
type_ent = Entry(master=main_win,font=("Gotham-Medium",16),background="#1db954",foreground="#ffffff")

singers_cbx.bind("<<ComboboxSelected>>",selected_singer)

singer_lbl.grid(row=0,column=0,sticky="nsew")
song_lbl.grid(row=1,column=0,sticky="nsew")
platform_lbl.grid(row=2,column=0,sticky="nsew")
type_lbl.grid(row=3,column=0,sticky="nsew")
singers_cbx.grid(row=0,column=1,sticky="nsew")
songs_cbx.grid(row=1,column=1,sticky="nsew")
platforms_cbx.grid(row=2,column=1,sticky="nsew")
type_ent.grid(row=3,column=1,sticky="nsew")

main_win.mainloop()
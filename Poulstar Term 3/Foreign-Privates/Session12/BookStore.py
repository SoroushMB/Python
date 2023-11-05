from tkinter import Entry,Tk,Label,Button,Toplevel
from tkinter.ttk import Combobox


def saving():
    books_info = open("Books_info.txt","a")
    books_info.write(f"\nBook:{book_ent.get()}\nAuthor:{author_cbx.get()}\nPublisher:{publisher_ent.get()}\nGenre:{genre_ent.get()}")
    books_info.close()

def next_level():
    global book_ent,author_cbx,publisher_ent,genre_ent
    
    authors = ["Leo Tolstoy","J.K.Rowling","George Orwell"]
    root.iconify()
    next_window = Toplevel()
    
    book_lbl = Label(master=next_window,text="Book : ",fg="gray95",bg="#404565",relief="raised",border=20,font=("Gotham-Medium",18))
    author_lbl = Label(master=next_window,text="Author : ",fg="gray95",bg="#404565",relief="raised",border=20,font=("Gotham-Medium",18))
    publisher_lbl = Label(master=next_window,text="Publisher : ",fg="gray95",bg="#404565",relief="raised",border=20,font=("Gotham-Medium",18))
    genre_lbl = Label(master=next_window,text="Genre : ",fg="gray95",bg="#404565",relief="raised",border=20,font=("Gotham-Medium",18))
    
    book_ent = Entry(master=next_window,fg="gray5",bg="#8590c0",relief="ridge",border=28,font=("Gotham-Medium",18))
    author_cbx = Combobox(master=next_window,font=("Gotham-Medium",18),values=authors)
    publisher_ent = Entry(master=next_window,fg="gray5",bg="#8590c0",relief="ridge",border=28,font=("Gotham-Medium",18))
    genre_ent = Entry(master=next_window,fg="gray5",bg="#8590c0",relief="ridge",border=28,font=("Gotham-Medium",18))
    final_btn = Button(master=next_window,text="Save!",fg="gray5",bg="#8590c0",relief="ridge",border=28,font=("Gotham-Medium",18),command=saving)
    
    book_lbl.grid(row=0,column=0,sticky="nsew")
    author_lbl.grid(row=1,column=0,sticky="nsew")
    publisher_lbl.grid(row=2,column=0,sticky="nsew")
    genre_lbl.grid(row=3,column=0,sticky="nsew")
    final_btn.grid(row=4,column=0,columnspan=2,sticky="nsew")
    
    book_ent.grid(row=0,column=1,sticky="nsew")
    author_cbx.grid(row=1,column=1,sticky="nsew")
    publisher_ent.grid(row=2,column=1,sticky="nsew")
    genre_ent.grid(row=3,column=1,sticky="nsew")
    
    next_window.mainloop()
# raised - sunken - ridge - groove - solid - flat
root = Tk()

greeting = Label(master=root,text="Hello, What's your name?",fg="gray95",bg="#404565",relief="raised",border=30,font=("Gotham-Medium",18))
name = Entry(master=root,fg="gray5",bg="#8590c0",relief="ridge",border=28,font=("Gotham-Medium",18))
next_page = Button(master=root,text="----->",fg="gray95",bg="#404565",relief="raised",border=20,font=("Gotham-Medium",18),command=next_level)

greeting.grid(row=0,column=0,sticky="nsew")
name.grid(row=1,column=0,sticky="nsew")
next_page.grid(row=2,column=0,sticky="nsew")

root.mainloop()
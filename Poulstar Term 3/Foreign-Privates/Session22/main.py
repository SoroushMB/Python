from tkinter import Tk,Frame,Label,Entry,Button
from tkinter.ttk import Notebook

def inserting():
    name = name_entry.get()
    writer = writer_entry.get()
    pages = pages_entry.get()
    with open("Books_Info.txt","a") as file:
        file.write(f"\n\nName: {name}\nWriter: {writer}\nPages: {pages}")
    
    
configurations = {
    "bg" : "black",
    "fg" : "white",
    "relief" : "raised",
    "border" : 20,
    "font" : ("JetBrains Mono",16),
    "anchor" : "w"
}

root = Tk()

tabs = Notebook(master=root)

searching_tab = Frame(master=tabs,bg="gray40")
adding_tab = Frame(master=tabs,bg="gray80")

name_label = Label(master=adding_tab,text="Name: ",cnf=configurations)
writer_label = Label(master=adding_tab,text="Writer: ",cnf=configurations)
pages_label = Label(master=adding_tab,text="Pages count : ",cnf=configurations)

name_entry = Entry(master=adding_tab,font=("Consolas",18))
writer_entry = Entry(master=adding_tab,font=("Consolas",18))
pages_entry = Entry(master=adding_tab,font=("Consolas",18))

show_button = Button(master=adding_tab,text="Show",bg="gray15",fg="white",font=("JetBrains Mono",16),command=inserting)

tabs.add(searching_tab,text="Search")
tabs.add(adding_tab,text="Adding")

name_label.grid(row=0,column=0,sticky="nsew")
writer_label.grid(row=1,column=0,sticky="nsew")
pages_label.grid(row=2,column=0,sticky="nsew")
name_entry.grid(row=0,column=1,sticky="nsew")
writer_entry.grid(row=1,column=1,sticky="nsew")
pages_entry.grid(row=2,column=1,sticky="nsew")
show_button.grid(row=3,column=0,columnspan=2,sticky="nsew")

tabs.pack()
root.mainloop()
from tkinter import Button,Checkbutton,Entry,Label,Tk,Toplevel,BooleanVar
from tkinter.ttk import Combobox,Spinbox

def secondary_page():
    second_page = Toplevel()
    second_page.title("Restuarent")
    
    name = intro_entry.get()
    intro_to_label = Label(second_page,text=f"Hi, {name}",cnf=main_page_config)
    
    flour_label = Label(second_page,text="Flour : ")
    flour1 = BooleanVar()
    flour1_ckb = Checkbutton(second_page,onvalue=True,offvalue=False,variable=flour1,text="Sangak",cnf=main_page_config)
    flour2 = BooleanVar()
    flour2_ckb = Checkbutton(second_page,onvalue=True,offvalue=False,variable=flour2,text="Barbari",cnf=main_page_config)
    
    yeast_label = Label(second_page,text="Yeast : ")
    yeast1 = BooleanVar()
    yeast1_ckb = Checkbutton(second_page,onvalue=True,offvalue=False,variable=yeast1,text="American",cnf=main_page_config)
    yeast2 = BooleanVar()
    yeast2_ckb = Checkbutton(second_page,onvalue=True,offvalue=False,variable=yeast2,text="Italian",cnf=main_page_config)
    
    cheese_label = Label(second_page,text="Cheese : ",cnf=main_page_config)
    cheeses = ["Mozzarella","Cheddar","Goat cheese"]
    cheeses_snb = Spinbox(second_page,values=cheeses,textvariable="Cheeses",font=("Consolas",16),state="readonly",bg="black",fg="white")
    
    sausage_label = Label(second_page,text="Sausage : ",cnf=main_page_config)
    sausages = ["HotDog","Bolgarian","Cocktale","Smokey","Frankforter","Chicken Sausage","Peperoni"]    
    sausage_cob = Combobox(second_page,values=sausages,font=("Consolas",16),state="readonly",bg="black",fg="white")
    
    
main_page_config = {
    "font" : ("Consolas",16),
    "bg" : "black",
    "fg" : "white"
}

# PEP8
main_page = Tk()
main_page.title("Login")
# 1 Label , 1 Entry
intro_label = Label(main_page,text="Hi,What is your name?",cnf=main_page_config)
intro_entry = Entry(main_page,cnf=main_page_config)
intro_button = Button(main_page,text="Next Page",cnf=main_page_config,command=lambda:secondary_page())

intro_label.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
intro_entry.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
intro_button.grid(row=2,column=0,padx=10,pady=10,sticky="nsew")

main_page.mainloop()
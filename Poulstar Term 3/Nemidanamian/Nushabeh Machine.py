from tkinter import Tk,Label,Button,LabelFrame

soft_drinks_widgets = {
    "Fanta" : {
        "bg": "orange",
        "fg": "white",
        "border":20,
        "relief":"ridge",
        "font":("Gotham-Medium",16)
    },
    
    "Pepsi" : {
        "bg": "red",
        "fg": "blue",
        "border":20,
        "relief":"ridge",
        "font":("Gotham-Medium",16)
    },
    
    "Sprite" : {
        "bg": "green",
        "fg": "yellow",
        "border":20,
        "relief":"ridge",
        "font":("Gotham-Medium",16)
    },
    
    "Canada" : {
        "bg": "red",
        "fg": "white",
        "border":20,
        "relief":"ridge",
        "font":("Gotham-Medium",16)
    },
    
    "AbAli" : {
        "bg": "white",
        "fg": "blue",
        "border":20,
        "relief":"ridge",
        "font":("Gotham-Medium",16)
    }
}

main_page = Tk()
main_page.title("Soft Drinks Machine")


Fanta_lf = LabelFrame(master=main_page)
Fanta_label = Label(master=Fanta_lf,cnf=soft_drinks_widgets["Fanta"])
Fanta_upb = Button(master=Fanta_lf,cnf=soft_drinks_widgets["Fanta"])
Fanta_downb = Button(master=Fanta_lf,cnf=soft_drinks_widgets["Fanta"])

Pepsi_lf = LabelFrame(master=main_page)
Pepsi_label = Label(master=Pepsi_lf,cnf=soft_drinks_widgets["Pepsi"])
Pepsi_upb = Button(master=Pepsi_lf,cnf=soft_drinks_widgets["Pepsi"])
Pepsi_downb = Button(master=Pepsi_lf,cnf=soft_drinks_widgets["Pepsi"])

Sprite_lf = LabelFrame(master=main_page)
Sprite_label = Label(master=Sprite_lf,cnf=soft_drinks_widgets["Sprite"])
Sprite_upb = Button(master=Sprite_lf,cnf=soft_drinks_widgets["Sprite"])
Sprite_downb = Button(master=Sprite_lf,cnf=soft_drinks_widgets["Sprite"])

Canada_lf = LabelFrame(master=main_page)
Canada_label = Label(master=Canada_lf,cnf=soft_drinks_widgets["Canada"])
Canada_upb = Button(master=Canada_lf,cnf=soft_drinks_widgets["Canada"])
Canada_downb = Button(master=Canada_lf,cnf=soft_drinks_widgets["Canada"])

AbAli_lf = LabelFrame(master=main_page)
AbAli_label = Label(master=AbAli_lf,cnf=soft_drinks_widgets["AbAli"])
AbAli_upb = Button(master=AbAli_lf,cnf=soft_drinks_widgets["AbAli"])
AbAli_downb = Button(master=AbAli_lf,cnf=soft_drinks_widgets["AbAli"])

Fanta_lf.grid(row=0,column=0)
Fanta_label.grid(row)
Fanta_upb.grid(row)
Fanta_downb.grid(row)

Pepsi_lf.grid(row=0,column=1)
Pepsi_label.grid(row)
Pepsi_upb.grid(row)
Pepsi_downb.grid(row)

Sprite_lf.grid(row=0,column=2)
Sprite_label.grid(row)
Sprite_upb.grid(row)
Sprite_downb.grid(row)

Canada_lf.grid(row=0,column=)
Canada_label.grid(row)
Canada_upb.grid(row)
Canada_downb.grid(row)

AbAli_lf.grid(row=0,column=)
AbAli_label.grid(row)
AbAli_upb.grid(row)
AbAli_downb.grid(row)




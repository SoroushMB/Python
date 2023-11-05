from tkinter import Label,Button,Tk,Entry,Toplevel
from tkinter.ttk import Combobox
from RCTurtle import Shapes

def shape_drawer():
    global geometries
    shape = shapes_cbx.get()
    
    first_dis = int(first_district_ent.get())
    second_dis = int(second_district_ent.get())
    
    geometries = Shapes(first_district=first_dis,second_district=second_dis)
    
    if shape == "Triangle" :
        geometries.triangle()

    elif shape == "Square" :
        geometries.square()

    elif shape == "Rectangle" :
        geometries.rectangle()

    elif shape == "Pentagon" :
        geometries.pentagon()

    elif shape == "Hexagon" :
        geometries.hexagon()

def page_settings():
    global geometries
    second_page = Toplevel()
    second_page.title("Settings")
    second_page.resizable(0,0)
    
    pensize_lbl = Label(master=second_page,bg="#e76f51",fg="#fefae0",relief="raised",font=("JetBrains Mono",16),border=20,justify="center")
    pencolor_lbl = Label(master=second_page,bg="#e76f51",fg="#fefae0",relief="raised",font=("JetBrains Mono",16),border=20,justify="center")
    bgcolor_lbl = Label(master=second_page,bg="#e76f51",fg="#fefae0",relief="raised",font=("JetBrains Mono",16),border=20,justify="center")

    pensize_ent = Entry(master=second_page,bg="#e76f51",fg="#fefae0",relief="sunken",font=("JetBrains Mono",16),border=20,justify="center")
    pencolor_ent = Entry(master=second_page,bg="#e76f51",fg="#fefae0",relief="sunken",font=("JetBrains Mono",16),border=20,justify="center")
    bgcolor_ent = Entry(master=second_page,bg="#e76f51",fg="#fefae0",relief="sunken",font=("JetBrains Mono",16),border=20,justify="center")
    
    pensize_lbl.grid(row=0,column=0,sticky="nsew",padx=20,pady=20)
    pencolor_lbl.grid(row=1,column=0,sticky="nsew",padx=20,pady=20)
    bgcolor_lbl.grid(row=2,column=0,sticky="nsew",padx=20,pady=20)
    
    pensize_ent.grid(row=0,column=1,sticky="nsew",padx=20,pady=20)
    pencolor_ent.grid(row=1,column=1,sticky="nsew",padx=20,pady=20)
    bgcolor_ent.grid(row=2,column=1,sticky="nsew",padx=20,pady=20)
    
    second_page.mainloop()

shapes = ["Triangle","Square","Rectangle","Pentagon","Hexagon"]

main_page = Tk()
main_page.title("Shape Maker")
main_page.resizable(0,0)

shapes_lbl = Label(master=main_page,text="Select the shape: ",font=("JetBrains Mono",16),relief="raised",border=20,bg="#264653",fg="white")
shapes_cbx = Combobox(master=main_page,background="#1d3557",values=shapes,foreground="#a8dadc",font=("JetBrains Mono",16))
first_district_ent = Entry(master=main_page,bg="#e76f51",fg="#fefae0",relief="sunken",font=("JetBrains Mono",16),border=20,justify="center")
second_district_ent = Entry(master=main_page,bg="#e76f51",fg="#fefae0",relief="sunken",font=("JetBrains Mono",16),border=20,justify="center")
drawer_button = Button(master=main_page,text="Click to draw!",bg="#e76f51",fg="#fefae0",relief="sunken",font=("JetBrains Mono",16),border=20,command=shape_drawer)
settings_button = Button(master=main_page,text="Settings",bg="#e76f51",fg="#fefae0",relief="sunken",font=("JetBrains Mono",16),border=20,command=page_settings)

shapes_lbl.grid(row=0,column=0,sticky="nsew",padx=20,pady=20)
shapes_cbx.grid(row=0,column=1,sticky="nsew",padx=20,pady=20)
first_district_ent.grid(row=1,column=0,sticky="nsew",padx=20,pady=20)
second_district_ent.grid(row=1,column=1,sticky="nsew",padx=20,pady=20)
drawer_button.grid(row=2,column=0,columnspan=2,sticky="nsew",padx=20,pady=20)
settings_button.grid(row=3,column=0,columnspan=2,sticky="nsew",padx=20,pady=20)

main_page.mainloop()
from tkinter import Tk,Entry,Label,Button,Spinbox
from turtle import pencolor,speed,forward,right,left,done,reset,clear
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo

def draw_button():
    size_string = combo_size.get()
    color = combo_color.get()
    dig = combo_diagram.get()

    if size_string== "" or color== "" or dig == "" :
        showinfo(title="Warning!",message="insert all parameters!")
        return
    

    size = int(combo_size.get())

    pencolor(color)
    speed(7)
    if dig == "Square":
        for x in range(4):
            forward(size)
            right(90)
            
    elif dig == "Circle":
        from turtle import circle
        circle(size)
                
    elif dig == "Rectangle":
        for x in range(2):
            forward(size)
            right(90)
            forward(size//2)
            right(90)
            
    elif dig == "Triangle":
        for x in range(3):
            forward(size)
            left(120)

    elif dig == "Hexagon":
        for x in range(6):
            forward(size)
            right(60)
    done()
    # forward(size)

def new_button():
    clear()
    reset()



Controlturtle =Tk()
Controlturtle.title("Control turtle")
Controlturtle.config(bg='#8B7D6B')
Label1=Label(Controlturtle,fg='white',bg='#8B8378',text="Size :",relief="ridge",border='6')
Label2=Label(Controlturtle,fg='white',bg='#8B8378',text="Pen color :",relief="ridge",border='6')
Label3=Label(Controlturtle,fg='white',bg='#8B8378',text="Diagram :",relief="ridge",border='6')

combo_size=Spinbox(master=Controlturtle,from_=10,to=100,increment=10,wrap=True)
combo_color=Combobox(master=Controlturtle,values=['Red','Green','Yellow','Blue'])
combo_diagram=Combobox(master=Controlturtle,values=['Triangle','Rectangle','Square','Circle','Hexagon'])

button_draw=Button(master=Controlturtle,text="Draw",relief="raised",border=5,fg="white",bg="#8B7355",command=draw_button)
button_new=Button(master=Controlturtle,text="New",relief="raised",border=5,fg="white",bg="#696969",command=new_button)

Label1.grid(row=1,column=0,sticky="news")
Label2.grid(row=2,column=0,sticky="news")
Label3.grid(row=3,column=0,sticky="news")
combo_size.grid(row=1,column=1,sticky="news",padx=5,pady=5)
combo_color.grid(row=2,column=1,sticky="news",padx=5,pady=5)
combo_diagram.grid(row=3,column=1,sticky="news",padx=5,pady=5)
button_draw.grid(row=4,column=1,sticky="news")
button_new.grid(row=4,column=0,sticky="news")

Controlturtle.mainloop()
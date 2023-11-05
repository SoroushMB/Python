from tkinter import Tk,Label,Entry,Button,LabelFrame
tak=Tk()
tak.title("salam")

label_shape=Label(tak,text="shape:",border=10,padx=10,pady=10)
entry_shape=Entry(tak,border=10,relief="ridge")
label_district=Label(tak,text="district:",border=10,padx=10,pady=10)
entry_district=Entry(tak,border=10,relief="ridge")
btn_draw=Button(tak,text="click to draw!",border=10,padx=10,pady=10,relief="ridge")
label_shape.grid(row=1,column=1)
entry_shape.grid(row=1,column=2,columnspan=2)
label_district.grid(row=2,column=1)
entry_district.grid(row=2,column=2,columnspan=2)
btn_draw.grid(row=3,column=1,columnspan=3,sticky="news")

def draw():
   c=str[entry_district.get()]
   if c="morabae":
      
   elif c="mostatil":
      
   elif c="shish zelei":
      
   elif c="dayere":
      
   elif c="mosalas":
      
tak.mainloop()
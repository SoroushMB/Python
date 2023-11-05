from tkinter import Label,Toplevel,Entry,Button,Tk
from datetime import date

def new_window():
    second_page = Toplevel()
    l1 = Label(master=second_page,text="Write your name down below in the box!",fg="white",bg="orange",font=("jetbrains mono",15),relief="ridge",border=23)
    e1 = Entry(master=second_page,font=("Magneto Bold",16))
    l1.pack()
    e1.pack()
    second_page.mainloop()

today = date.today()
print("Today's date:", today)
def register():  
    artin_calandar=artin_calandar.get()
    username=user_ent.get()
    info_file=open("Info.txt",mode="w")
    info_file.write(f"username:{username}\n")
    info_file.close()
    
jungle_lib = Tk()

user_lbl = Label(master=jungle_lib,text="Username:")
user_ent = Entry(master=jungle_lib)
continue_btn = Button(master=jungle_lib,text="continue",command=new_window)
user_lbl.grid(row=3,column=0,padx=30,pady=30,sticky="nsew")
user_ent.grid(row=3,column=1,padx=30,pady=30,sticky="nsew")
continue_btn.grid(row=4,column=1,padx=20,pady=50,sticky="nsew")
jungle_lib.mainloop()


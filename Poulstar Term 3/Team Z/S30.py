from tkinter import Tk,Label,Entry,Button,Spinbox,Toplevel
from tkinter.ttk import Combobox

def delition(event):
    username.delete(first=0,last="end")
    username.unbind('<Button-1>',undelition)
def insertion(event):
    showing.config(text=f"I like {videogames.get()}")
    # videogames.unbind('<Button-1>',uninsertion)
    
videogames_list = ["NeedForSpeed Unbound","NeedForSpeed2015","Injustice2","CallOfDutyModernWarfare2","MortalCombat11","StrongholdSeries"]

root = Tk()
root.title("Example")

showing = Label(master=root,
                text="You will see the result here!",
                relief="raised",
                border=20,    
                font=("JetBrains Mono",16),
                bg="#1db964",
                fg="#ffffff")
username = Entry(master=root,
                bg="#003566",
                fg="gray92",
                relief="raised",
                border=20,
                font=("Gotham-Medium",16))

videogames = Spinbox(master=root,
                     values=videogames_list,
                     font=("JetBrains Mono",16),
                     bg="#1db964",
                     fg="#ffffff"
                     )

username.insert(index=0,string="Please enter your username!")

username.grid(row=0,column=0,sticky="nsew")
showing.grid(row=1,column=0)
videogames.grid(row=2,column=0)
undelition = username.bind('<Button-1>',delition)
uninsertion = videogames.bind('<Button-1>',insertion)
root.mainloop()
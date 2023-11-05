from tkinter import Tk,Label,Button,Entry

def showing():
    name = name_e.get()
    food =  food_e.get()
    print(f"{name} likes {food}")
    
root = Tk()

name_l = Label(master=root,text="Name:",bg="darkred",fg="white",font=("JetBrains Mono",16))
food_l = Label(master=root,text="Food:",bg="darkred",fg="white",font=("JetBrains Mono",16))

name_e = Entry(master=root,bg="darkred",fg="white",font=("JetBrains Mono",16))
food_e = Entry(master=root,bg="darkred",fg="white",font=("JetBrains Mono",16))

alaki_b = Button(master=root,text="Press to see!",bg="darkred",fg="white",font=("JetBrains Mono",16),command=lambda:showing())

name_l.grid(row=0 ,column=0 ,sticky="nsew")
food_l.grid(row=1 ,column=0 ,sticky="nsew")
name_e.grid(row=0 ,column=1 ,sticky="nsew")
food_e.grid(row=1 ,column=1 ,sticky="nsew")
alaki_b.grid(row=2 ,column=0 ,sticky="nsew",columnspan=2)

root.mainloop()
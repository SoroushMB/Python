from tkinter import Button,Entry,Label,Tk,Toplevel
from datetime import date
from tkinter.messagebox import showinfo

def new_window():
    if len(user_ent.get()) == 0:
        showinfo(title="Alert!",message="You haven't entered your name!")
    else:
        root.iconify()
        global username_ent,password_ent
        window = Toplevel()
        window.title("Main Page😁")
        
        username = user_ent.get()
        intro_lbl = Label(master=window,text=f"Hello, {username}!",font=("JetBrains Mono",18),bg="#344e41",fg="white",relief="solid",border=8)
        username_lbl = Label(master=window,text="Username : ",font=("JetBrains Mono",18),bg="#344e41",fg="white",relief="solid",border=8)
        password_lbl = Label(master=window,text="Password : ",font=("JetBrains Mono",18),bg="#344e41",fg="white",relief="solid",border=8)
        username_ent = Entry(master=window,font=("JetBrains Mono",18),relief="solid",border=8)
        password_ent = Entry(master=window,font=("JetBrains Mono",18),relief="solid",border=8)
        saving_btn = Button(master=window,text="Saving content!",font=("JetBrains Mono",18),relief="solid",border=8,command=saving)
        
        intro_lbl.grid(row=0,column=0,columnspan=2,sticky="nsew")
        username_lbl.grid(row=1,column=0,sticky="nsew")
        password_lbl.grid(row=2,column=0,sticky="nsew")
        username_ent.grid(row=1,column=1,sticky="nsew")
        password_ent.grid(row=2,column=1,sticky="nsew")
        saving_btn.grid(row=3,column=0,columnspan=2,sticky="nsew")
        window.mainloop()

def saving():
    global username_ent,password_ent
    username = username_ent.get()
    password = password_ent.get()
    file = open("UserInfo.txt","a")
    file.write(f"\nUsername: {username}\nPassword: {password}\nDate: {date.today()}")
    file.close()
    showinfo(title="Success!",message="Your info has been saved successfully!")

root = Tk()
root.title("Artin's Pass Manager")

user_lbl = Label(master=root,text=" Username :  ",font=("JetBrains Mono",18),bg="#344e41",fg="white",relief="solid",border=8)
user_ent = Entry(master=root,font=("JetBrains Mono",18),relief="solid",border=8)
user_btn = Button(master=root,text="Enter to start!",font=("JetBrains Mono",18),bg="#22333b",fg="white",relief="solid",border=8,command=new_window)

user_lbl.grid(row=0,column=0,padx=30,pady=30,sticky="nsew")
user_ent.grid(row=0,column=1,padx=30,pady=30,sticky="nsew")
user_btn.grid(row=1,column=0,padx=30,pady=30,columnspan=2,sticky="nsew")

root.mainloop()
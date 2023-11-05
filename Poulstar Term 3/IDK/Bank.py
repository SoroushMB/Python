# Bank : Profile , Loan , Withdraw , Create , Exchange , Deposit
# Login
from tkinter import Frame , Label , Button , Entry , Tk , Toplevel
from tkinter.ttk import Notebook , Checkbutton , Combobox

login_page = Tk()
login_page.config(background="#ffb5a7")
# Login-Page Requirements : 2 Button - 2 Entry - 2 Label

login_username_label = Label(master=login_page,text="Username :",relief="raised",width=6,border=20,font=("Product Sans Medium",16),bg="#fcd5ce",fg="gray8")
login_password_label = Label(master=login_page,text="Password :",relief="raised",width=6,border=20,font=("Product Sans Medium",16),bg="#fcd5ce",fg="gray8")
login_username_entry = Entry(master=login_page,width=10,relief="sunken",border=20,font=("Product Sans Medium",16),bg="#f8edeb",fg="gray8")
login_password_entry = Entry(master=login_page,show="🗿",width=10,relief="sunken",border=20,font=("Product Sans Medium",16),bg="#f8edeb",fg="gray8")
register_button = Button(master=login_page,text="Register",width=8,relief="ridge",border=20,font=("Product Sans Medium",15),bg="#d8e2dc",fg="gray8")
login_button = Button(master=login_page,text="Login",width=8,relief="ridge",border=20,font=("Product Sans Medium",15),bg="#e8e8e4",fg="gray8")

login_username_label.grid(row=0 ,column=0 ,sticky="nsew")
login_password_label.grid(row=1 ,column=0 ,sticky="nsew")
login_username_entry.grid(row=0 ,column=1 ,sticky="nsew")
login_password_entry.grid(row=1 ,column=1 ,sticky="nsew")
login_button.grid(row=2 ,column=0 ,sticky="nsew")
register_button.grid(row=2 ,column=1 ,sticky="nsew")

login_page.mainloop()
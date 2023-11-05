from tkinter.messagebox import showerror,showinfo
from database import Database

first_db = Database(host="127.0.0.1",dbname="carS1",pswd="root",user="root")
try:
    first_db.connectToDB()
except RuntimeError:
    showerror(title="Alarm!",message="The Username or The Password isn't correct!")
else:
    showinfo(title="Success!",message="Everything is copacetic!")
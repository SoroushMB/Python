from tkinter import Button,Entry,Label,Tk
from pymysql import connect as cnt


root = Tk()


def nmd():

    Host = ht.get()
    User = user.get()
    Passwd = passwd.get()
    dbname = dbName.get()

    nmd1 = cnt(host=Host,user=User,password=Passwd,db=dbname)

    return nmd1

config = {
    "labels" : {
                "font":("Product Sans Medium",16),
                "fg" : "black",
                "bg" : "green",
                "relief" : "raised",
                "border" : 20,
                "width" : 15,
                },
    "btn" : {
                "font":("Product Sans Medium",16),
                "fg" : "black",
                "bg" : "red",
                "relief" : "raised",
                "border" : 20,
                "width" : 15,
                }
        }


lht = int(Label(text="Host :",cnf=config["labels"],master = root))
luser = str(Label(text="User :",cnf=config["labels"],master = root))
lpasswd = str(Label(text="Password :",cnf=config["labels"],master = root))
ldbName = str(Label(text="db :",cnf=config["labels"],master= root))


ht = Entry(cnf=config["labels"],master = root)
user = Entry(cnf=config["labels"],master = root)
passwd = Entry(cnf=config["labels"],master = root)
dbName = Entry(cnf=config["labels"],master= root)

bEnd = Button(master=root,cnf=config["btn"],text="Click to show  your informations!",command=lambda:nmd())


lht.grid(row=0,column=0)
luser.grid(row=1,column=0)
lpasswd.grid(row=2,column=0)
ldbName.grid(row=3,column=0)

ht.grid(row=0,column=1)
user.grid(row=1,column=1)
passwd.grid(row=2,column=1)
dbName.grid(row=3,column=1)

bEnd.grid(row=5,column=1,columnspan=2)

root.mainloop()
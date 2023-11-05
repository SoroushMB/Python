from tkinter import Tk,Label,Button,Entry

settings = {"font":("Bodoni MT",22),
            "bg":"#b8c0ff", 
            "fg":"#3d348b",
            "border":10
            }

root = Tk()
root.geometry("600x500+960+540")
root.title(string="Team Cena")
root["bg"] = "skyblue"

greeting1 = Label(master=root, text="Hello, World!", cnf=settings,  relief="ridge")
greeting2 = Label(master=root, text="Hello, World!", cnf=settings,  relief="raised")
greeting3 = Label(master=root, text="Hello, World!", cnf=settings,  relief="groove")
greeting4 = Label(master=root, text="Hello, World!", cnf=settings,  relief="solid")
greeting5 = Label(master=root, text="Hello, World!", cnf=settings,  relief="flat")
greeting6 = Label(master=root, text="Hello, World!", cnf=settings,  relief="sunken")
greeting1.pack()
greeting2.pack()
greeting3.pack()
greeting4.pack()
greeting5.pack()
greeting6.pack()
root.mainloop()
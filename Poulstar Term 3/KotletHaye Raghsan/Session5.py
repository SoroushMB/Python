from tkinter import Tk,Label,Button,Entry

configurations = {"font":("JetBrains Mono",20),"relief":"ridge","border":50}
# ---Window---
root = Tk()
root["bg"] = "#000000"
root.title("🤍-For test-🗿")
# root.geometry("500x400+00+00")
# root.resizable(1,1)
# ---Widgets---
l1 = Label(master=root,text="Name: ",bg="#277da1",fg="#f94144",cnf=configurations)
l2 = Label(master=root,text="Age: ",bg="#577590",fg="#f3722c",cnf=configurations)
l3 = Label(master=root,text="Phone number: ",bg="#4d908e",fg="#f8961e",cnf=configurations)

e1 = Entry(master=root,bg="#277da1",fg="#f94144",cnf=configurations)
e2 = Entry(master=root,bg="#577590",fg="#f3722c",cnf=configurations)
e3 = Entry(master=root,bg="#4d908e",fg="#f8961e",cnf=configurations)

# ---Layouts---
l1.grid(row=0,column=0,sticky="nsew")
l2.grid(row=1,column=0,sticky="nsew")
l3.grid(row=2,column=0,sticky="nsew")

e1.grid(row=0,column=1,sticky="nsew")
e2.grid(row=1,column=1,sticky="nsew")
e3.grid(row=2,column=1,sticky="nsew")

root.mainloop() 

from tkinter import Tk,Label,Button,Entry

def opreations(btn):
    portal1_number = int(portal1.get())
    portal2_number = int(portal2.get())
    if btn == "Plus":
        neshundahande.config(text=f"Natijeh : {portal1_number + portal2_number}")
    elif btn == "Minus":
        neshundahande.config(text=f"Natijeh : {portal1_number - portal2_number}")
    elif btn == "Multiply":
        neshundahande.config(text=f"Natijeh : {portal1_number * portal2_number}")
    elif btn == "Division":
        neshundahande.config(text=f"Natijeh : {portal1_number / portal2_number}")

root = Tk()
root.title("Simple Calculator")

neshundahande = Label(master=root,text="Ta alan hichi ro nazadi!",width=28,relief="sunken",border=25,font=("Product Sans Medium",18),bg="salmon",fg="red4")

portal1 = Entry(master=root,width=14,relief="sunken",border=25,font=("Product Sans Medium",18),bg="salmon",fg="red4")
portal2 = Entry(master=root,width=14,relief="sunken",border=25,font=("Product Sans Medium",18),bg="salmon",fg="red4")

uno_nazan1 = Button(master=root,text="Plus",width=7,relief="sunken",border=25,font=("Product Sans Medium",18),bg="maroon",fg="sea green",command=lambda:opreations("Plus"))
uno_nazan2 = Button(master=root,text="Minus",width=7,relief="sunken",border=25,font=("Product Sans Medium",18),bg="maroon",fg="sea green",command=lambda:opreations("Minus"))
uno_nazan3 = Button(master=root,text="Multiply",width=7,relief="sunken",border=25,font=("Product Sans Medium",18),bg="maroon",fg="sea green",command=lambda:opreations("Multiply"))
uno_nazan4 = Button(master=root,text="Division",width=7,relief="sunken",border=25,font=("Product Sans Medium",18),bg="maroon",fg="sea green",command=lambda:opreations("Division"))

neshundahande.grid(row=0 ,column=0 ,columnspan=4 ,sticky="nsew")
portal1.grid(row=1 ,column=0,columnspan=2 ,sticky="nsew")
portal2.grid(row=1 ,column=2,columnspan=2 ,sticky="nsew")
uno_nazan1.grid(row=2 ,column=0 ,sticky="nsew")
uno_nazan2.grid(row=2 ,column=1 ,sticky="nsew")
uno_nazan3.grid(row=2 ,column=2 ,sticky="nsew")
uno_nazan4.grid(row=2 ,column=3 ,sticky="nsew")
root.mainloop()
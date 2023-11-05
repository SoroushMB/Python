from tkinter import Tk,Label,Button,Entry
# 2 Label - 2 Entry - 1 Button
username = input("Your name: ")

root = Tk()

username_lbl = Label(master=root,
                    text=f"Salam, {username}!",
                    font=("JetBrains Mono",16),
                    bg="#0a9396",
                    fg="White",
                    relief="raised",
                    border=20)
result_lbl = Label(master=root,
                    text="Result : ",
                    font=("JetBrains Mono",16),
                    bg="#0a9396",
                    fg="White",
                    relief="raised",
                    border=20)
number1_ent = Entry(master=root,
                    relief="ridge",
                    border=20,
                    font=("Gotham-Medium",16),
                    fg="#94d2bd",
                    bg="Black") 
number2_ent = Entry(master=root,
                    relief="ridge",
                    border=20,
                    font=("Gotham-Medium",16),
                    fg="#94d2bd",
                    bg="Black")
showing_btn = Button(master=root,
                    text=f"Age jorat dari bezan!",
                    font=("JetBrains Mono",16),
                    bg="#005f73",
                    fg="White",
                    relief="groove",
                    border=20)
username_lbl.grid(row=0,column=0,sticky="nsew")
result_lbl.grid(row=0,column=1,sticky="nsew")
number1_ent.grid(row=1,column=0,sticky="nsew")
number2_ent.grid(row=2,column=0,sticky="nsew")
showing_btn.grid(row=1,column=1,rowspan=2,sticky="nsew")
root.mainloop()

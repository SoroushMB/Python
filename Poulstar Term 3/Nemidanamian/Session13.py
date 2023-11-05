# Button - Entry
# Label : master , text , fg , bg , relief , border , width = padx , height = pady
# Button : master , text , fg , bg , relief , border , width = padx , height = pady , command
# Entry : master , text , fg , bg , relief , border , width = padx , pady , state

from tkinter import Tk,Label,Button,Entry
def feshar():
    user_name.config(state="readonly")
main_page = Tk()

name = Label(master=main_page,
             text="Hello, World!",
             font=("JetBrains Mono",16),
             bg="#2ec4b6",
             fg="gray96",
             relief="ridge",
             border=20,
             width=20,
             height=10)
show = Button(master=main_page,
             text="Feshar bede ta bebini!",
             font=("JetBrains Mono",16),
             bg="#2ec4b6",
             fg="gray96",
             relief="raised",
             border=20,
             width=20,
             height=10,
             command=lambda:feshar())
user_name = Entry(master=main_page,
             font=("JetBrains Mono",16),
             bg="#b5e2fa",
             fg="gray4",
             relief="groove",
             border=20,
             width=20,
             state="normal")
name.grid(row=0,column=0)
show.grid(row=1,column=0)
user_name.grid(row=2,column=0)
main_page.mainloop()

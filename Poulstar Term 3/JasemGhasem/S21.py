from tkinter import Tk,Label,Button,Entry

def calc():
    number1_get = int(number1.get())
    number2_get = int(number2.get())
    result.config(text=f"Result : {number1_get + number2_get}")
    
main_page = Tk()
main_page.config(background="#5fed85")

result = Label(master=main_page,text="Result : ",border=10,relief="raised",bg="darkblue",fg="lightblue",font=("Product Sans Medium",16))
showing = Button(master=main_page,text="Press to show!",border=10,relief="raised",bg="darkblue",fg="lightblue",font=("Product Sans Medium",16),command=lambda: calc())
number1 = Entry(master=main_page,border=10,relief="raised",bg="darkblue",fg="lightblue",font=("Product Sans Medium",16))
number2 = Entry(master=main_page,border=10,relief="raised",bg="darkblue",fg="lightblue",font=("Product Sans Medium",16))

result.grid(row=1,column=1,sticky="nsew")
showing.grid(row=1,column=0,sticky="nsew")
number1.grid(row=0,column=0,sticky="nsew")
number2.grid(row=0,column=1,sticky="nsew")
main_page.mainloop()
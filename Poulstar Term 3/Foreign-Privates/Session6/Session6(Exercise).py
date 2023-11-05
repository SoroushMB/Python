from tkinter import Tk,Label,Entry,Button

username = input("What is your name: ") # username = "Maya"
def calculator_sum():
    got_number1 = int(number1.get())
    got_number2 = int(number2.get())
    final = got_number1 + got_number2
    showing.config(text=f"Result: {final}")

page = Tk()
# MacOS : Arial , Spot Mono
# Windows : Arial , Consolas
# Widgets : Label , Entry , Button , RadioButton , etc
# Length = طول ، Width = عرض ، Height = ارتفاع 
greeting = Label(master=page,text=f"Hi, {username}!",font=("Product Sans",18))
number1 = Entry(master=page,font=("Product Sans",18),width=10)
number2 = Entry(master=page,font=("Product Sans",18),width=10)
showing = Label(master=page,text = "Result: ",font=("Product Sans",18))
getting_result = Button(master=page,text="Press to show!",font=("Product Sans",18),command=lambda:calculator_sum())

greeting.grid(row=0 ,column=0 ,padx=10 ,pady=10)
number1.grid(row=1 ,column=0 ,padx=10 ,pady=10)
number2.grid(row=2 ,column=0 ,padx=10 ,pady=10)
showing.grid(row=0 ,column=1 ,rowspan=2  ,padx=10 ,pady=10)
getting_result.grid(row=2 ,column=1 ,padx=10 ,pady=10)
page.mainloop()
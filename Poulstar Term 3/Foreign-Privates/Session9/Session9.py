from tkinter import Label,Button,Entry,Toplevel,Tk

def result():
    exact_equation = equation.get()
    final_result = eval(f"{exact_equation}")
    second_win = Toplevel()
    main_result = Label(master=second_win,text=f"Result : {final_result}",bg="#0b132b",fg="#6fffe9",width=20,height=5,relief="raised",border=25,font=("Product Sans Medium",16))
    main_result.grid(row=0,column=0,sticky="nsew")
    second_win.mainloop()

main_win = Tk()

equation = Entry(master=main_win,bg="#0b132b",fg="#6fffe9",width=20,relief="groove",border=25,font=("Product Sans Medium",16))
showman = Button(master=main_win,text="Press to show!",bg="#0b132b",fg="#6fffe9",width=20,height=5,relief="raised",border=25,font=("Product Sans Medium",16),command=lambda:result())

equation.grid(row=0,column=0,sticky="nsew")
showman.grid(row=1,column=0,sticky="nsew")

main_win.mainloop()
from tkinter import Tk,Label,Entry,Button,Toplevel

def show():
    money = float((money_entry.get()).replace("$",""))
    percentage = (float((percentage_entry.get()).replace("%","")))/100
    final_result = money * percentage
    main_page.iconify()
    second_page = Toplevel()
    result_label = Label(master=second_page,
                        text=f"Leave ${final_result:.2f}",
                        font=("Product Sans Medium",18),
                        bg="#f4a261",
                        fg="gray10",
                        relief="raised",
                        border=25)
    result_label.pack()
    second_page.mainloop()

main_page = Tk()
main_page.title("Tip Calculator")

money_label = Label(master=main_page,
                    text="The receipt : ",
                    font=("Product Sans Medium",18),
                    bg="#f4a261",
                    fg="gray10",
                    relief="raised",
                    border=25)
money_entry = Entry(master=main_page,
                    font=("Product Sans Medium",18),
                    bg="#e9c46a",
                    fg="gray10",
                    relief="raised",
                    border=25)

percentage_label = Label(master=main_page,
                    text="The tip : ",
                    font=("Product Sans Medium",18),
                    bg="#f4a261",
                    fg="gray10",
                    relief="raised",
                    border=25)
percentage_entry = Entry(master=main_page,
                    font=("Product Sans Medium",18),
                    bg="#e9c46a",
                    fg="gray10",
                    relief="raised",
                    border=25)

result_button = Button(master=main_page,
                    text="Result",
                    font=("Product Sans Medium",18),
                    bg="#e9c46a",
                    fg="gray10",
                    relief="raised",
                    border=25,
                    command=lambda:show())

money_label.grid(row=0 ,column=0 ,sticky="nsew")
money_entry.grid(row=0 ,column=1 ,sticky="nsew")
percentage_label.grid(row=1 ,column=0,sticky="nsew")
percentage_entry.grid(row=1 ,column=1,sticky="nsew")
result_button.grid(row=2 ,column=0 ,columnspan=2 ,sticky="nsew")

main_page.mainloop()
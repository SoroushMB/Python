from tkinter import Tk,StringVar,Label,Radiobutton,Frame

main_page = Tk()
main_page.config(background="#192a51")
def checking():
    getting_wrong_answer = wrong_answer.get()
    getting_right_answer = right_answer.get()
    if getting_right_answer == "1":
        print("You have selected right answer")
    else:
        print("You have selected wrong answer")

secondary_page = Frame(master=main_page,relief="ridge",width=600,height=600,bg="#192a51")
first_question = Label(master=secondary_page,
                                            text="If we eat 3 Apples from 4 Apples available, how many will remain? ",S
                                            font=("Product Sans Medium",12),
                                            bg="#967aa1",
                                            fg="gray6",
                                            relief="groove",
                                            border=15)

wrong_answer = StringVar()
right_answer = StringVar()
answer_one  = Radiobutton(master=secondary_page,text="1 - 1",font=("Product Sans Medium",12),relief="raised",border=20,value="1",state="normal",variable=right_answer,command=checking())
answer_two  = Radiobutton(master=secondary_page,text="2 - 2",font=("Product Sans Medium",12),relief="raised",border=20,value="0",state="normal",variable=wrong_answer,command=checking())
answer_three  = Radiobutton(master=secondary_page,text="3 - 3",font=("Product Sans Medium",12),relief="raised",border=20,value="0",state="normal",variable=wrong_answer,command=checking())
answer_fourth  = Radiobutton(master=secondary_page,text="4 - 4",font=("Product Sans Medium",12),relief="raised",border=20,value="0",state="normal",variable=wrong_answer,command=checking())

secondary_page.grid(row=0,column=0,sticky="nsew")
first_question.grid(row=0,column=0,sticky="nsew")
answer_one.grid(row=1,column=0,sticky="nsew")
answer_two.grid(row=2,column=0,sticky="nsew")
answer_three.grid(row=3,column=0,sticky="nsew")
answer_fourth.grid(row=4,column=0,sticky="nsew")
main_page.mainloop()
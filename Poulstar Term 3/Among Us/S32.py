from tkinter import Tk,Label,Text,Button,END
main_page = Tk()
hamintori = answer.get("1.0","end-1c")
main_page.title("Q&A")
question = Label(master=main_page,
            text="How much will be the answer of 2 + 2 ?",
            font=("JetBrains Mono",18),
            bg="#123456",
            fg="#6998f0",
            relief="raised",
            border=20
            )
answer = Text(master=main_page,
              font=("JetBrains Mono",18),
              bg="#0a162e",
              fg="#576c91",
              relief="sunken",
              border=20,
              height=10
              )
cars = "Nissan GTR Skyline R34"
answer.insert(END, cars)
question.grid(row=0,column=0,sticky="nsew")
answer.grid(row=1,column=0,sticky="nsew")
main_page.mainloop()
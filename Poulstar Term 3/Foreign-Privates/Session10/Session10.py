from tkinter import Text,Entry,Tk

main_win = Tk()
main_win.title("Intro to Text!")

main_entry = Entry(master=main_win,bg="#7bf1a8",fg="gray3",font=("JetBrains Mono",16),border=20,relief="ridge",width=15)
main_text = Text(master=main_win,bg="#ffef9f",fg="gray3",font=("JetBrains Mono",16),border=20,relief="ridge",width=15,height=5)

main_entry.grid(row=0,column=0,sticky="nsew")
main_text.grid(row=1,column=0,sticky="nsew")

main_win.mainloop()
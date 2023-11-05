from tkinter import Tk,Label,Button,Entry

root = Tk()
# root.geometry("800x300+100+100")
# root.state("zoom")
root.title("Hamintori")
root.config(bg="white")
root.resizable(0,0)
name = Label(master=root,
            text="Hello, World!",
            bg="#fc03c2",
            fg="white",
            font=("JetBrains Mono",32),
            relief="sunken",
            border=20,
            width=20,
            height=10,
            padx=20,
            pady=20)
show = Button(master=root,
            text="Press to show!",
            bg="#fc03c2",
            fg="white",
            font=("JetBrains Mono",32),
            relief="raised",
            border=20,
            width=20,
            height=10,
            padx=20,
            pady=20,
            command=lambda:print("Hello from here!"))
sabteahval = Entry(master=root,
            bg="#fc03c2",
            fg="white",
            font=("JetBrains Mono",32),
            relief="sunken",
            border=20,
            width=20)
name.grid(row=0,column=0)
show.grid(row=0,column=1)
sabteahval.grid(row=0,column=2)
root.mainloop()
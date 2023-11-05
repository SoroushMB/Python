from tkinter import StringVar,Tk,Checkbutton,Radiobutton


root = Tk()
language1_str = StringVar()
language2_str = StringVar()
car1_str = StringVar()

language1 = Checkbutton(master=root,
                        text="English",
                        relief="raised",
                        font=("Gotham-Medium",16),
                        fg="gray95",
                        bg="green",
                        variable=language1_str,
                        offvalue="Nothing",
                        onvalue="English",
                        command=lambda:print(f"{language1_str.get()}"))
language2 = Checkbutton(master=root,
                        text="Spanish",
                        relief="raised",
                        font=("Gotham-Medium",16),
                        fg="gray95",
                        bg="green",
                        variable=language2_str,
                        offvalue="Nothing",
                        onvalue="Spanish",
                        command=lambda:print(f"{language2_str.get()}"))
car1 = Radiobutton(master=root,
                    text="Nissan GTR",
                    relief="raised",
                    font=("Gotham-Medium",16),
                    fg="gray95",
                    bg="green",
                    variable=car1_str,
                    value="Nissan GTR",
                    command=lambda:print(f"{car1_str.get()}"))
language1.grid(row=0,column=0,sticky="nsew")
language2.grid(row=1,column=0,sticky="nsew")
car1.grid(row=2,column=0,sticky="nsew")

root.mainloop()
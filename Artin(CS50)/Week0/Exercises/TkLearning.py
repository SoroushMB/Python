import tkinter as tk
# Windows : Tk , Toplevel
# Widgets : Label , Button , Entry , Checkbutton , Radiobutton , ...
UserInput = "Cookie!"
root = tk.Tk()
root.geometry("600x200")
root.config(bg="black")
file = tk.PhotoImage(file="squidward.png")
root.iconphoto(False,file)
root.title(string="Squidward")
name = tk.Label(master=root,text=UserInput,fg="white",bg="black",font=("Consolas",16))
name.pack()
root.mainloop()
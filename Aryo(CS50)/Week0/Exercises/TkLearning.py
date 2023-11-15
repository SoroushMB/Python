import tkinter as tk
# Windows : Tk , Toplevel
# Widgets : Label , Button , Entry , Combobox , etc
root = tk.Tk()
File = tk.PhotoImage(file="FH4.png")
root.iconphoto(False,File)
root.config(bg="DarkSeaGreen4")
root.title(string="Example")
root.geometry("300x250")
root.mainloop()
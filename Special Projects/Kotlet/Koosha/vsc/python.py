import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Spinbox Demo')
c=["kos","lor"]
# Spinbox
current_value = tk.StringVar(value=0)
spin_box = ttk.Spinbox(
    root,
    values=c,
    textvariable=current_value,
    wrap=True)

spin_box.pack()

root.mainloop()
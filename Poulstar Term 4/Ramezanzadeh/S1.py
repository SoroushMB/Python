import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Intro Of Treeview")

columns = ("first_name","last_name","phonenumber")

tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("first_name",text="First Name")
tree.heading("last_name",text="Last Name")
tree.heading("phonenumber",text="Phone Number")

contacts = [
    ["Soroush","MasoumBabaei","09039851230"],
    ["Arad","Abdolmanaf","09903178388"],
    ["Ilya","Dayi","09909570170"]
]
for contact in contacts:
    tree.insert('',"end",values=contact)

def items(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item["values"]

tree.bind("<<TreeviewSelect>>", items)
tree.grid(row=0,column=0,sticky="nsew")
root.mainloop()
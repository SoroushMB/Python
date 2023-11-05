from tkinter import *
from tkinter import ttk
#Create an instance of tkinter frame
win = Tk()
win.geometry("750x250")
#Create a Notebook widget
my_notebook= ttk.Notebook(win)
#Create Tabs
tab1= ttk.Frame(my_notebook)
tab2= ttk.Frame(my_notebook)
#Create a Label in Tabs
Label(tab1, text= "Hello, Howdy?", font= ('Helvetica 20 bold')).pack()
Label(tab2, text= "This is a New Tab Context", font=('Helvetica 20 bold')).pack()

my_notebook.add(child=tab1, text= "Tab 1")
my_notebook.add(tab2, text= "Tab 2")
my_notebook.pack(expand=1,fill=BOTH)
win.mainloop()
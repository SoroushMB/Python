# RadioButton - CheckButton
from tkinter import Label,Tk,Button,Radiobutton,StringVar,IntVar
from tkinter.ttk import Checkbutton

def showing_language():
    python_language = python.get()
    js_language = javascript.get()
    cplusplus_language = cplusplus.get()
    if python_language == "Python Off":
        python_label.config(text="Python is Off!")
    elif python_language == "Python On":
        python_label.config(text="Python is On!")

main_page = Tk()

python = StringVar()
javascript = StringVar()
cplusplus = StringVar()

python_label = Label(master=main_page,text="",font=("Product Sans Medium",16))
python_show = Checkbutton(master=main_page,text="Python",offvalue="Python Off",onvalue="Python On",variable=python,command=showing_language())
javascript_show = Checkbutton(master=main_page,text="JavaScript",offvalue="JS Off",onvalue="JS On",variable=javascript)
cplusplus_show = Checkbutton(master=main_page,text="C++",offvalue="C++ Off",onvalue="C++ On",variable=cplusplus)

python_label.pack()
python_show.pack()
javascript_show.pack()
cplusplus_show.pack()
main_page.mainloop()
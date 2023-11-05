from tkinter import Tk

root = Tk()

root_w = 800
root_h = 600

window_w = root.winfo_screenwidth()
window_h = root.winfo_screenheight()

converted_w = (window_w/2) - (root_w/2)
converted_h = (window_h/2) - (root_h/2)

root.geometry("{}x{}+{}+{}".format(root_w,root_h,converted_h))
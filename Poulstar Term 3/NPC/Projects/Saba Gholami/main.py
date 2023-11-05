from tkinter import Tk,Button,Entry,Frame,END,LEFT,BOTH,TRUE,GROOVE,RIGHT
import tkinter.messagebox
import math


root = Tk()
root.geometry("550x500+0+0")
root.title("Calculator")


def btn1():
    if ent.get() == "0":
        ent.delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, "1")


def btn2():
    if ent.get() == "0":
        ent. delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, "2")


def btn3():
    if ent.get() == "0":
        ent.delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, "3")


def btn4():
    if ent.get() == "0":
        ent.delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, "4")


def btn5():
    if ent.get() == "0":
        ent.delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, "5")


def btn6():
    if ent.get() == "0":
        ent.delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, "6")


def btn7():
    if ent.get() == "0":
        ent.delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, "7")


def btn8():
    if ent.get() == "0":
        ent. delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, "8")


def btn9():
    if ent.get() == "0":
        ent. delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, "9")


def btn0():
    if ent.get() == "0":
        ent. delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, "0")


def btn_mosbat():
    pos = len(ent.get())
    ent.insert(pos, "+")


def btn_manfi():
    pos = len(ent.get())
    ent.insert(pos, "-")


def btn_zarb():
    pos = len(ent.get())
    ent.insert(pos, "*")


def btn_taghsim():
    pos = len(ent.get())
    ent.insert(pos, "/")


def btnc(*args):
    ent.delete(0, END)
    ent.insert(0, "0")


def btn_xy():
    pos = len(ent.get())
    ent.insert(pos, "**")


def btn_pi():
    pos = len(ent.get())
    ent.insert(pos, "3.14")


def btn_x2():
    pos = len(ent.get())
    ent.insert(pos, "**2")


def btn_mosavi(*args):
    try:
        ans = ent.get()
        ans = eval(ans)
        ent.delete(0, END)
        ent.insert(0, ans)
    except:
        tkinter.messagebox.showerror("Eror", "Check ")


def btn_darsad():
    pos = len(ent.get())
    ent.insert(pos, '%')


def btn_e():
    if ent.get() == "0":
        ent.delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, str(math.e))


def btn_sin():
    if ent.get() == "0":
        ent.delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, str(math.sin(pos)))


def btn_log():
    if ent.get() == "0":
        ent.delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, str(math.cos()))


def btn_tan():
    if ent.get() == "0":
        ent.delete(0, END)
    pos = len(ent.get())
    ent.insert(pos, str(math.tan))


ent = Entry(root, font="Vazir 20", fg="black",
            bg="#6699ff", bd=20, justify=RIGHT)
ent.pack(expand=TRUE, fill=BOTH)


btnrow1 = Frame(root)
btnrow1.pack(expand=TRUE, fill=BOTH)

pi = Button(btnrow1, text="pi", font="Vazir 18", relief=GROOVE,
            bd=10, command=btn_pi, fg="white", bg="#80aaff")
pi.pack(side=LEFT, expand=TRUE, fill=BOTH)

xy_btn = Button(btnrow1, text="x^y", font="Segoe 17", relief=GROOVE, bd=10,
                command=btn_xy, fg="white", bg="#80aaff")
xy_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

x2_btn = Button(btnrow1, text="x^2", font="Segoe 17", relief=GROOVE, bd=10,
                command=btn_x2, fg="white", bg="#80aaff")
x2_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

b_darsad = Button(btnrow1, text=" % ", font="Segoe 16", relief=GROOVE,
                  bd=10, command=btn_darsad, fg="white", bg="#80aaff")
b_darsad.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)

b_e = Button(btnrow2, text=" e", font="Segoe 20", relief=GROOVE, bd=10,
             command=btn_e, fg="white", bg="#80aaff")
b_e.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn7 = Button(btnrow2, text="7", font="Segoe 23", relief=GROOVE, bd=0,
              command=btn7, fg="white", bg="#99bbff")
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow2, text="8", font="Segoe 23", relief=GROOVE, bd=0,
              command=btn8, fg="white", bg="#99bbff")
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(btnrow2, text="9", font="Segoe 23", relief=GROOVE, bd=0,
              command=btn9, fg="white", bg="#99bbff")
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

b_taghsim = Button(btnrow2, text=" / ", font="Segoe 23", relief=GROOVE, bd=10,
                   command=btn_taghsim, fg="white", bg="#80aaff")
b_taghsim.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

b_sin = Button(btnrow3, text="sin", font="Segoe 16", relief=GROOVE, bd=10,
               command=btn_sin, fg="white", bg="#80aaff")
b_sin.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn4 = Button(btnrow3, text="4", font="Segoe 23", relief=GROOVE,
              bd=0, command=btn4, fg="white", bg="#99bbff")
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(btnrow3, text="5", font="Segoe 23", relief=GROOVE, bd=0,
              command=btn5, fg="white", bg="#99bbff")
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(btnrow3, text="6", font="Segoe 23", relief=GROOVE, bd=0,
              command=btn6, fg="white", bg="#99bbff")
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

b_zarb = Button(btnrow3, text=" * ", font="Segoe 22", relief=GROOVE, bd=10,
                command=btn_zarb, fg="white", bg="#80aaff")
b_zarb.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

b_log = Button(btnrow4, text="log", font="Segoe 16", relief=GROOVE, bd=10,
               command=btn_log, fg="white", bg="#80aaff")
b_log.pack(side=LEFT, expand=TRUE, fill=BOTH)


btn1 = Button(btnrow4, text="1", font="Vazir 23", relief=GROOVE, bd=0,
              command=btn1, fg="white", bg="#99bbff")
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow4, text="2", font="Segoe 23", relief=GROOVE, bd=0,
              command=btn2, fg="white", bg="#99bbff")
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow4, text="3", font="Segoe 23", relief=GROOVE, bd=0,
              command=btn3, fg="white", bg="#99bbff")
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

b_mosbat = Button(btnrow4, text="+ ", font="Segoe 23", relief=GROOVE, bd=10,
                  command=btn_mosbat, fg="white", bg="#80aaff")
b_mosbat.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnrow5 = Frame(root)
btnrow5.pack(expand=TRUE, fill=BOTH)

b_tan = Button(btnrow5, text="tan", font="Segoe 16", relief=GROOVE, bd=10,
               command=btn_tan, fg="white", bg="#80aaff")
b_tan.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow5, text="0", font="Segoe 23", relief=GROOVE, bd=0,
              command=btn0, fg="white", bg="#99bbff")
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnc = Button(btnrow5, text="C", font="Segoe 23", relief=GROOVE, bd=0,
              command=btnc, fg="red", bg="#99bbff")
btnc.pack(side=LEFT, expand=TRUE, fill=BOTH)

b_mosavi = Button(btnrow5, text="=", font="Segoe 23", relief=GROOVE, bd=0,
                  command=btn_mosavi, fg="green", bg="#99bbff")
b_mosavi.pack(side=LEFT, expand=TRUE, fill=BOTH)

b_manfi = Button(btnrow5, text="-  ", font="Segoe 23", relief=GROOVE, bd=10,
                 command=btn_manfi, fg="white", bg="#80aaff")
b_manfi.pack(side=LEFT, expand=TRUE, fill=BOTH)

root.mainloop()

from tkinter import *
import time


global a



def update(a):
    txt = 'Sample Text'
    mylabel.configure(text=txt[0:a])
    
def timer():
    global a
    a = 0
    lenth = len('Sample Text')
    start = time.time()
    while True:
        # Do other stuff, it won't be blocked
        time.sleep(0.1)

        # When 1 sec or more has elapsed...
        if time.time() - start > 1:
            start = time.time()
            a = a + 1

            # This will be updated once per second
            print("{} counter".format(a))
            update(a)
            # Count up to the lenth of text, ending loop
            if a > lenth:
                break

root = Tk()
root.geometry('300x300')

mylabel = Label(root, text="S", font=('Bell', 36, 'bold'))
mylabel.pack(pady=5)

root.after(3000, timer)
root.mainloop()
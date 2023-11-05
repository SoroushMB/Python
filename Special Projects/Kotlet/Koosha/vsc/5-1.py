from tkinter import Tk,Button,Label,Entry
import os
os.system("cls")
root=Tk()
root.geometry('400x300')
root.title("jam.exe")
root['bg']="white"

entry1=Entry(root,width=20)
entry2=Entry(root,width=20)
entry3=Entry(root,width=25)
def calc():
   operator=entry3.get()
   if operator=="jam":
    adad1=entry1.get()
    adad2=entry2.get()
    jvb=int(adad1)+int(adad2)
    eera= Label (root,text=jvb,font=("Arial",10))
    eera.pack()
   elif operator=="menha":
    adad1=entry1.get()
    adad2=entry2.get()
    jvb=int(adad1)-int(adad2)
    eera= Label (root,text=jvb,font=("Arial",10))
    eera.pack()
   elif operator=="zarb":
    adad1=entry1.get()
    adad2=entry2.get()
    jvb=int(adad1)*int(adad2)
    eera= Label (root,text=jvb,font=("Arial",10))
    eera.pack()
   elif operator=="taghsim":
    adad1=entry1.get()
    adad2=entry2.get()
    jvb=int(adad1)/int(adad2)
    eera= Label (root,text=jvb,font=("Arial",10))
    eera.pack()

button1=Button(root,text="submit",width=15,height=1,font="Arial",command=lambda:calc())
labelone=Label(root,text="first number",fg="red")
labeltwo=Label(root,text="second number",fg="red")
op=Label(root,text="Operator",fg="red")

labelone.
labelone.pack()
entry1.pack()
labeltwo.pack()
entry2.pack()
op.pack()
entry3.pack()
button1.pack()

root.mainloop()
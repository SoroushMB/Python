from tkinter import Tk,Entry,Label,Button,LabelFrame
from time import sleep
root=Tk()
root.title("nomarat")
frame=LabelFrame(root,fg="Red")
frame.pack()
nlst=[]
slst=[]
def next():
   n=nent.get()
   nlst.append(n)
   s=float(sent.get())
   f=str(round(s))
   j=int(f)
   slst.append(j)
   a=n+" ba nomre "+f+" has been added."
   pabel.config(text=a,fg="red")
def sub():
   g=0
   c=0
   for i in slst:
      if i<51:
         nlst.pop(c)
         slst.pop(c)
      c+=1
   for i in range(0,c):
      k=str(nlst[i])
      K=str(slst[i])
      pabel.config(text=f"{k} ba nomre {K}:::::")
      g+=1
pabel=Label(frame)
nlbl=Label(frame,text="enter nam:",fg="Red")
slbl=Label(frame,text="enter your nomre:",fg="Red")
nent=Entry(frame)
sent=Entry(frame)
sbt=Button(frame,text="submit",command=lambda:sub())
nbt=Button(frame,text="next",command=lambda:next())
nlbl.grid(row=0,column=1)
slbl.grid(row=2,column=1)
nent.grid(row=1,column=1,sticky="news",columnspan=2)
sent.grid(row=3,column=1,sticky="news",columnspan=2)
sbt.grid(row=4,column=2,sticky="news")
nbt.grid(row=4,column=1,sticky="news")
pabel.grid(row=5,column=1,columnspan=2,sticky="news")


root.mainloop()
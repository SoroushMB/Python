from tkinter import Tk,Label,Entry,Button,LabelFrame,messagebox
from tkinter.ttk import Combobox,Spinbox
from time import sleep

tak=Tk()
tak.title("on taklife ke 20% ta 50% prozhe payan term mahsob mishod")
tak.config
product=LabelFrame(tak,bg="#FFEECC",relief="ridge",border=3)
product.grid(row=1,column=1,padx=15,pady=15)

product1=Button(product,text=
"""diet coke
2$""",bg="#CD6688",width=7,height=2,bd=10,relief="ridge",command=lambda:p1())
product1.grid(row=1,column=1,padx=4,pady=5)

p1up=Button(product,text="🔼",bg="#EA1179",bd=3,height=2,width=4,command=lambda:udietcoke())
p1down=Button(product,text="🔽",bg="#EA1179",bd=3,height=2,width=4,command=lambda:ddietcoke())
p1lbl=Label(product,text="0",bg="#FEBBCC",bd=6,height=1,width=3,relief="sunken")
p1up.grid(row=2,column=1,pady=3)
p1down.grid(row=4,column=1,pady=3)
p1lbl.grid(row=3,column=1)

def p1():
 p1up.flash()
 p1down.flash()

def udietcoke():
 d=int(p1lbl['text'])
 f=d+1
 p1lbl.config(text=f)
def ddietcoke():
 d=int(p1lbl['text'])
 if d==0:
  messagebox.showerror("Error","Error!")  
 else:              
  f=d-1
  p1lbl.config(text=f)


product2=Button(product,text=
"""pringles
3.5$""",bg="#CD6688",width=7,height=2,bd=10,relief="ridge",command=lambda:p2())
product2.grid(row=1,column=2,padx=4,pady=5)

p2up=Button(product,text="🔼",bg="#EA1179",bd=3,height=2,width=4,command=lambda:upringles())
p2down=Button(product,text="🔽",bg="#EA1179",bd=3,height=2,width=4,command=lambda:dpringles())
p2lbl=Label(product,text="0",bg="#FEBBCC",bd=6,height=1,width=3,relief="sunken")
p2up.grid(row=2,column=2,pady=3)
p2down.grid(row=4,column=2,pady=3)
p2lbl.grid(row=3,column=2)

def p2():
 p2up.flash()
 p2down.flash()

def upringles():
 d=int(p2lbl['text'])
 f=d+1
 p2lbl.config(text=f)
def dpringles():
 d=int(p2lbl['text'])
 if d==0:
  messagebox.showerror("Error","Error!")  
 else:              
  f=d-1
  p2lbl.config(text=f)

product3=Button(product,text=
"""snickers
1.5$""",bg="#CD6688",width=7,height=2,bd=10,relief="ridge",command=lambda:p3())
product3.grid(row=1,column=3,padx=4,pady=5)

p3up=Button(product,text="🔼",bg="#EA1179",bd=3,height=2,width=4,command=lambda:usnickers())
p3down=Button(product,text="🔽",bg="#EA1179",bd=3,height=2,width=4,command=lambda:dsnickers())
p3lbl=Label(product,text="0",bg="#FEBBCC",bd=6,height=1,width=3,relief="sunken")
p3up.grid(row=2,column=3,pady=3)
p3down.grid(row=4,column=3,pady=3)
p3lbl.grid(row=3,column=3)

def p3():
 p3up.flash()
 p3down.flash()

def usnickers():
 d=int(p3lbl['text'])
 f=d+1
 p3lbl.config(text=f)
def dsnickers():
 d=int(p3lbl['text'])
 if d==0:
  messagebox.showerror("Error","Error!")  
 else:              
  f=d-1
  p3lbl.config(text=f)


submit=Button(product,text="Submit",bg="#D7BBF5",command=lambda:submit())
submit.grid(row=5,column=1,columnspan=3,sticky="news",padx=4,pady=4)

def submit():
  c=int(p1lbl['text'])
  e=int(p2lbl['text'])
  f=int(p3lbl['text'])
  if c==0 and e==0 and f==0:
    messagebox.showerror("Error","Your basket is empty.")  
  else:
    o=(c*2)+(e*3.5)+(f*1.5)
    prlbl.config(text=f"{o}$")


price=LabelFrame(tak,bg="#FFD9C0",relief="ridge",border=2)
price.grid(row=2,column=1,pady=5)


price2=LabelFrame(price,bg="#FFEECC",relief="ridge",border=6)
price2.grid(row=1,rowspan=2,column=1,columnspan=3,padx=3,pady=3)

txtlbl=Label(price2,text="           Price: ",height=2,width=8,bg="#FFEECC")
txtlbl.grid(row=1,column=1,columnspan=2,sticky="news",rowspan=2)
prlbl=Label(price2,text="",bg="#FFEECC",width=12)
prlbl.grid(row=1,column=3,sticky="news",rowspan=2)

a=("1¢","5¢","10¢","25¢","50¢","1$","5$","10$")

bill=Spinbox(price,state="readonly",values=a,width=9)
bill.grid(row=1,column=4,columnspan=3,sticky="news")
billbt=Button(price,text="Bill",bg="#85A389",command=lambda:bil())
billbt.grid(row=2,column=4,columnspan=3,sticky="news")

def bil():
  a=bill.get()
  s=prlbl['text']
  x=s.replace("$","")
  k=float(x. replace('.', '.'))
  P=k*100
  if a=="1¢":
    if P>1:
      g=P-1 
      j=g/100
      prlbl.config(text=f"{j}$")
    elif P==1:
      g=P-1 
      messagebox.showinfo("Your done","Thank you for choosing us!")  
      tak.destroy()
    elif P<1:
      messagebox.showerror("Error","It's a lot")  
  elif a=="5¢":
    if P>5:
      g=P-5 
      j=g/100
      prlbl.config(text=f"{j}$")
    elif P==5:
      g=P-5 
      messagebox.showinfo("Your done","Thank you for choosing us!")  
      tak.destroy()
    elif P<5:
      messagebox.showerror("Error","It's a lot")  
  elif a=="10¢":
    if P>10:
      g=P-10 
      j=g/100
      prlbl.config(text=f"{j}$")
    elif P==10:
      g=P-10 
      messagebox.showinfo("Your done","Thank you for choosing us!")  
      tak.destroy()
    elif P<10:
      messagebox.showerror("Error","It's a lot")  
  elif a=="25¢":
    if P>25:
      g=P-25 
      j=g/100
      prlbl.config(text=f"{j}$")
    elif P==25:
      g=P-25 
      messagebox.showinfo("Your done","Thank you for choosing us!")  
      tak.destroy()
    elif P<25:
      messagebox.showerror("Error","It's a lot")  
  elif a=="50¢":
    if P>50:
      g=P-50 
      j=g/100
      prlbl.config(text=f"{j}$")
    elif P==50:
      g=P-50 
      messagebox.showinfo("Your done","Thank you for choosing us!")  
      tak.destroy()
    elif P<50:
      messagebox.showerror("Error","It's a lot")  
  elif a=="1$":
    if P>100:
      g=P-100
      j=g/100
      prlbl.config(text=f"{j}$")
    elif P==100:
      g=P-100 
      messagebox.showinfo("Your done","Thank you for choosing us!")  
      tak.destroy()
    elif P<100:
      messagebox.showerror("Error","It's a lot")  
  elif a=="5$":
    if P>500:
      g=P-500 
      j=g/100
      prlbl.config(text=f"{j}$")
    elif P==500:
      g=P-500 
      messagebox.showinfo("Your done","Thank you for choosing us!")  
      tak.destroy()
    elif P<500:
      messagebox.showerror("Error","It's a lot")  
  elif a=="10$":
    if P>1000:
      g=P-1000 
      j=g/100
      prlbl.config(text=f"{j}$")
    elif P==1000:
      g=P-1000 
      messagebox.showinfo("Your done","Thank you for choosing us!")  
      tak.destroy()
    elif P<1000:
      messagebox.showerror("Error","It's a lot")  
      
tak.mainloop()
from tkinter import Tk,Label,Button,LabelFrame,Frame,Entry,Spinbox,Toplevel,StringVar,Checkbutton,Radiobutton,IntVar,Text
from tkinter.ttk import Combobox
from random import choice,randint
from tkinter.messagebox import showinfo,showerror
c1=randint(1000,9999)
def Hesab():
    global f2,f3,cb,f12,ep
    a=f2.get()
    b=f3.get()
    c=cb.get()
    if len(a)==0 or len(b)==0 or len(c)==0:
        showerror(title="ALERT",message="Complete The List")
    else:
      page=Toplevel()
      lp=Label(page,text="ID cart:",font=("Arial",20))
      ep=Entry(page,font=("Arial",20))
      bp=Button(page,text="Send",font=("Arial",20),command=lambda:Ersal())
      lp.grid(row=0,column=0,columnspan=1,sticky="nsew")
      ep.grid(row=0,column=1,columnspan=2,sticky="nsew")
      bp.grid(row=2,column=2,columnspan=3,sticky="nsew")
      page.mainloop()
def Faktor():
    global cb2,cb3,f5,f12,e1,f2,f3,cb,rp,Code
    a=cb.get()
    b=cb2.get()
    c=cb3.get()
    d=e1.get()
    e=f2.get()
    f=f3.get()
    g=f5.get()
    h=f12.get()
    n=rp.get()
    if n==Code:
        
        page3=Toplevel()

        t=Label(page3,text=
                f"""Your Name: {d} 
        Your Phone Number: {e}
        you live in : {f}
        Food : {h}
        Tedad pors : {a}
        Sid dishes : {b}
        beverages : {c}

        """)
        t.grid(row=0,column=0,columnspan=1,sticky="nsew")
    else :
       showerror(title="Alert",message="code Not correct!")

def Ersal():
    global rp,Code,ip,ep
    Code=randint(1000,9999)
    a=ep.get()
    if len(a)==16:
      ramz_poya=open("ramz_poya.txt","a")
      ramz_poya.write("_"*30)
      ramz_poya.write(f"\n ramz poya baray tapsi food {Code}")
      ramz_poya.close()
      page2=Toplevel()
      ip=Label(page2,text="Enter code",font=("Arial",20))
      rp=Entry(page2,font=("Arial",20))
      dp=Button(page2,text="Finish",font=("Arial",20),command=lambda:Faktor())
      ip.grid(row=0,column=0,columnspan=1,sticky="nsew")
      rp.grid(row=0,column=1,columnspan=2,sticky="nsew")
      dp.grid(row=2,column=2,columnspan=3,sticky="nsew")
      page2.mainloop()
    else:
      showerror(title="ALERT",message="id cart not correct")


def Refresh():
    global cb2,cb3,e5,e12
    a=f5.get()
    b=f12.get()

    if a=="fast_food":
      f12.config(values=fast_food)
    elif a=="stew":
      f12.config(values=stew)
    elif a=="barbecue":
      f12.config(values=barbecue)
    elif a=="fish":
      f12.config(values=fish)
    elif a=="":
      f12.config(values=food_all) 
    if b in fish:
      f5.config(values="fish")
    elif b in barbecue:
      f5.config(values="barbecue")
    elif b in stew:
      f5.config(values="stew")
    elif b in fast_food:
      f5.config(values="fast_food")
    elif b=="":
      f5.config(values=food)
    
    
kobideh=110000
chenjeh=100000
jojeh=120000
kabab_torshe=90000
qhezel_ala=200000
capor=180000
khavyar=300000
meigo=500000
pitzza=80000
hut_dog=70000
hamberger=75000
sandewich=78000
olive=2000
jelly=10000
yogurs=7000
ashpal=8000
fesenjun=89000
qheime=95000
alo_qheisi=92000
qhormeh=91000
orange_soda=5000
beer=7000
dough=9000
black_soda=1000000

side_dishes="olive","jelly","yogurs","ashpal"
fast_food="pitzza","hut_dog","hamberger","sandevich"
beverages="black_soda","orange_soda","beer","dough"
fish="qhezel_ala","capor","khavyar","meigo"
barbecue="jojeh","chenjeh","kobideh","kabab_torsh"
food_all="pitzza","hut_dog","hamberger","sandevich","kotlet","fesenjun","qheime","alo_qheisi","qhormeh","qhezel_ala","capor","khavyar","meigo","jojeh","chenjeh","kobideh","kabab_torsh"
food=["stew","barbecue","fast_food","fish"]
stew="fesenjun","qheime","alo_qheisi","qhormeh","kotlet"
def code_sending():
    global c1
    showinfo(title="CODE",message=f"Your Code Is {c1}")

def Check_Vorood():
    global e2,e3,e4,e5,c1
    a=e2.get()
    b=e3.get()
    c=e4.get()
    d=e5.get()
    if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0:
        showerror(title="ALERT",message="Complete The List")
    elif b!=c:
        showerror(title="ALERT",message="Passwords Are Not The Same")
    elif d!=f"{c1}":
        showerror(title="ALERT",message="Enter The Correct Code")
    else:
        root.destroy()
root=Tk()
root.title("Taxi food")
lf1=LabelFrame(root,font=("Arial",50))
l1=Label(root,text=" Taxi Food ",font=("Arial",15))
l2=Label(lf1,text="Name :",font=("Arial",15))
l3=Label(lf1,text="Enter The Password :",font=("Arial",15))
l4=Label(lf1,text="Enter The Confirm Password :",font=("Arial",15))
l5=Label(lf1,text="Enter The Code :",font=("Arial",15))
e2=Entry(lf1,font=("Arial",15))
e3=Entry(lf1,font=("Arial",15))
e4=Entry(lf1,font=("Arial",15))
e5=Entry(lf1,font=("Arial",15))
b1=Button(lf1,text="Code",font=("Arial",15),command=lambda:code_sending())
b2=Button(lf1,text="Save",font=("Arial",15),command=lambda:Check_Vorood())
lf1.grid(row=1,column=0,columnspan=1,sticky="nsew")
l1.grid(row=0,column=0,columnspan=2,sticky="nsew")
l2.grid(row=0,column=0,columnspan=1,sticky="nsew")
l3.grid(row=1,column=0,columnspan=1,sticky="nsew")
l4.grid(row=2,column=0,columnspan=1,sticky="nsew")
l5.grid(row=3,column=0,columnspan=1,sticky="nsew")
e2.grid(row=0,column=1,columnspan=2,sticky="nsew")
e3.grid(row=1,column=1,columnspan=2,sticky="nsew")
e4.grid(row=2,column=1,columnspan=2,sticky="nsew")
e5.grid(row=3,column=1,columnspan=2,sticky="nsew")
b1.grid(row=4,column=0,columnspan=3,sticky="nsew")
b2.grid(row=5,column=0,columnspan=3,sticky="nsew")
root.mainloop()
root2=Tk()
root2.title("taxi food")
lb1=LabelFrame(root2,font=("Arial",70))
lb2=LabelFrame(root2,font=("Arial",70))
l2=Label(lb1,text="Name :",font=("Arial",20))
l3=Label(lb1,text="Phone Number :",font=("Arial",20))
l4=Label(lb1,text="Where Do You Live :",font=("Arial",20))
l7=Label(lb1,text="resturan",font=("Arial",20))
e1=Entry(lb1,font=("Arial",20))
f2=Entry(lb1,font=("Arial",20))
f3=Entry(lb1,font=("Arial",20))
lb1.grid(row=0,column=0,columnspan=1,sticky="nsew")
l2.grid(row=0,column=0,columnspan=1,sticky="nsew")
l3.grid(row=1,column=0,columnspan=1,sticky="nsew")
l4.grid(row=2,column=0,columnspan=1,sticky="nsew")
e1.grid(row=0,column=1,columnspan=2,sticky="nsew")
f2.grid(row=1,column=1,columnspan=2,sticky="nsew")
f3.grid(row=2,column=1,columnspan=2,sticky="nsew")
l5=Label(lb2,text="Food",font=("Arial",20))
l6=Label(lb2,text="Menu",font=("Arial",20))
l7=Label(lb2,text="tedad pors",font=("Arial",20))
l9=Label(lb2,text="sid dishes",font=("Arial",20))
l10=Label(lb2,text="beverages" ,font=("Arial",20))
b1=Button(lb2,text="Refresh",font=("Arial,20"),command=lambda:Refresh())
b2=Button(lb1,text="Save",font=("Arial,20"),command=lambda:Hesab())
b2.grid(row=3,column=1,columnspan=1,sticky="nsew")
cb=Entry(lb2,font=("Arial",20))
cb2=Combobox(lb2,values=side_dishes,font=("Arial",20))
cb3=Combobox(lb2,values=beverages,font=("Arial",20))
f12=Combobox(lb2,values=food_all,font=("Arial",20))
f5=Combobox(lb2,values=food,font=("Arial",20))
lb2.grid(row=0,column=1,columnspan=2,sticky="nsew")
l5.grid(row=0,column=0,columnspan=1,sticky="nsew")
l6.grid(row=1,column=0,columnspan=1,sticky="nsew")
l7.grid(row=2,column=0,columnspan=1,sticky="nsew")
l9.grid(row=4,column=0,columnspan=1,sticky="nsew")
l10.grid(row=5,column=0,columnspan=1,sticky="nsew")
b1.grid(row=6,column=0,columnspan=1,sticky="nsew")
f5.grid(row=0,column=1,columnspan=2,sticky="nsew")
f12.grid(row=1,column=1,columnspan=2,sticky="nsew")
cb.grid(row=2,column=1,columnspan=2,sticky="nsew")
cb2.grid(row=4,column=1,columnspan=2,sticky="nsew")
cb3.grid(row=5,column=1,columnspan=2,sticky="nsew")
root2.mainloop()
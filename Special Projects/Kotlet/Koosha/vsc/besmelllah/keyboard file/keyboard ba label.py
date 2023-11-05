from tkinter import Tk,Label,Entry,Button,LabelFrame,messagebox,Text,Toplevel
from tkinter.ttk import Combobox,Spinbox
root=Tk()
root.title("Keyboard")
rang="red"
temcode=1
#Keyboard has 61 buttons
#khat aval

esc=Button(root,text="Esc",height=2,width=4,relief="raised",border=5,bg="#F1F0E8",command=lambda:escape())
esc.grid(row=1,column=1,columnspan=2,sticky="news")

manfiyek=Button(root,text="`",height=2,width=4,relief="raised",border=5,command=lambda:manfiyak())
manfiyek.grid(row=1,column=3,columnspan=2,sticky="news")

yek=Button(root,text="1",height=2,width=4,relief="raised",border=5,command=lambda:yak())
yek.grid(row=1,column=5,columnspan=2,sticky="news")

do=Button(root,text="2",height=2,width=4,relief="raised",border=5,command=lambda:du())
do.grid(row=1,column=7,columnspan=2,sticky="news")

se=Button(root,text="3",height=2,width=4,relief="raised",border=5,command=lambda:si())
se.grid(row=1,column=9,columnspan=2,sticky="news")

char=Button(root,text="4",height=2,width=4,relief="raised",border=5,command=lambda:chaar())
char.grid(row=1,column=11,columnspan=2,sticky="news")

panj=Button(root,text="5",height=2,width=4,relief="raised",border=5,command=lambda:pang())
panj.grid(row=1,column=13,columnspan=2,sticky="news")

shish=Button(root,text="6",height=2,width=4,relief="raised",border=5,command=lambda:shesh())
shish.grid(row=1,column=15,columnspan=2,sticky="news")

haft=Button(root,text="7",height=2,width=4,relief="raised",border=5,command=lambda:hafte())
haft.grid(row=1,column=17,columnspan=2,sticky="news")

hasht=Button(root,text="8",height=2,width=4,relief="raised",border=5,command=lambda:hashte())
hasht.grid(row=1,column=19,columnspan=2,sticky="news")

noh=Button(root,text="9",height=2,width=4,relief="raised",border=5,command=lambda:nah())
noh.grid(row=1,column=21,columnspan=2,sticky="news")

sefr=Button(root,text="0",height=2,width=4,relief="raised",border=5,command=lambda:sofre())
sefr.grid(row=1,column=23,columnspan=2,sticky="news")

khat=Button(root,text="-",height=2,width=4,relief="raised",border=5,command=lambda:khatefasele())
khat.grid(row=1,column=25,columnspan=2,sticky="news")

mosavi=Button(root,text="=",height=2,width=4,relief="raised",border=5,command=lambda:movasi())
mosavi.grid(row=1,column=27,columnspan=2,sticky="news")

backespace=Button(root,text="⌫",height=2,width=4,relief="raised",border=5,bg="#F1F0E8",command=lambda:backspace())
backespace.grid(row=1,column=29,columnspan=2,sticky="news")

#khat dovom

tab=Button(root,text="Tab",height=2,width=8,relief="raised",border=5,bg="#F1F0E8")
tab.grid(row=2,column=1,columnspan=3,sticky="news")

q=Button(root,text="q",height=2,width=4,relief="raised",border=5,command=lambda:qq())
q.grid(row=2,column=4,columnspan=2,sticky="news")

w=Button(root,text="w",height=2,width=4,relief="raised",border=5,command=lambda:ww())
w.grid(row=2,column=6,columnspan=2,sticky="news")

e=Button(root,text="e",height=2,width=4,relief="raised",border=5,command=lambda:ee())
e.grid(row=2,column=8,columnspan=2,sticky="news")

r=Button(root,text="r",height=2,width=4,relief="raised",border=5,command=lambda:rr())
r.grid(row=2,column=10,columnspan=2,sticky="news")

t=Button(root,text="t",height=2,width=4,relief="raised",border=5,command=lambda:tt())
t.grid(row=2,column=12,columnspan=2,sticky="news")

y=Button(root,text="y",height=2,width=4,relief="raised",border=5,command=lambda:yy())
y.grid(row=2,column=14,columnspan=2,sticky="news")

u=Button(root,text="u",height=2,width=4,relief="raised",border=5,command=lambda:uu())
u.grid(row=2,column=16,columnspan=2,sticky="news")

i=Button(root,text="i",height=2,width=4,relief="raised",border=5,command=lambda:ii())
i.grid(row=2,column=18,columnspan=2,sticky="news")

o=Button(root,text="o",height=2,width=4,relief="raised",border=5,command=lambda:oo())
o.grid(row=2,column=20,columnspan=2,sticky="news")

p=Button(root,text="p",height=2,width=4,relief="raised",border=5,command=lambda:pp())
p.grid(row=2,column=22,columnspan=2,sticky="news")

korushe=Button(root,text="[",height=2,width=4,relief="raised",border=5,command=lambda:koroshe())
korushe.grid(row=2,column=24,columnspan=2,sticky="news")

bkorushe=Button(root,text="]",height=2,width=4,relief="raised",border=5,command=lambda:bkoroshe())
bkorushe.grid(row=2,column=26,columnspan=2,sticky="news")

enter=Button(root,text="Enter",height=2,width=4,relief="raised",border=5,bg="#F1F0E8")
enter.grid(row=2,column=28,columnspan=3,sticky="news")
#khat sevom


caps1=Button(root,text="Caps",height=2,width=4,relief="raised",border=5,bg="#F1F0E8",command=lambda:caps(),fg="black")
caps1.grid(row=3,column=1,columnspan=4,sticky="news")

a=Button(root,text="a",height=2,width=4,relief="raised",border=5,command=lambda:aa())
a.grid(row=3,column=5,columnspan=2,sticky="news")

s=Button(root,text="s",height=2,width=4,relief="raised",border=5,command=lambda:ss())
s.grid(row=3,column=7,columnspan=2,sticky="news")

d=Button(root,text="d",height=2,width=4,relief="raised",border=5,command=lambda:dd())
d.grid(row=3,column=9,columnspan=2,sticky="news")

f=Button(root,text="f",height=2,width=4,relief="raised",border=5,command=lambda:ff())
f.grid(row=3,column=11,columnspan=2,sticky="news")

g=Button(root,text="g",height=2,width=4,relief="raised",border=5,command=lambda:gg())
g.grid(row=3,column=13,columnspan=2,sticky="news")

h=Button(root,text="h",height=2,width=4,relief="raised",border=5,command=lambda:hh())
h.grid(row=3,column=15,columnspan=2,sticky="news")

j=Button(root,text="j",height=2,width=4,relief="raised",border=5,command=lambda:jj())
j.grid(row=3,column=17,columnspan=2,sticky="news")

k=Button(root,text="k",height=2,width=4,relief="raised",border=5,command=lambda:kk())
k.grid(row=3,column=19,columnspan=2,sticky="news")

l=Button(root,text="l",height=2,width=4,relief="raised",border=5,command=lambda:ll())
l.grid(row=3,column=21,columnspan=2,sticky="news")

donoghte=Button(root,text=":",height=2,width=4,relief="raised",border=5,command=lambda:dodot())
donoghte.grid(row=3,column=23,columnspan=2,sticky="news")

potation=Button(root,text='"',height=2,width=4,relief="raised",border=5,command=lambda:potaishen())
potation.grid(row=3,column=25,columnspan=2,sticky="news")

enter2=Button(root,text="↵",height=2,width=4,relief="raised",border=5,bg="#F1F0E8")
enter2.grid(row=3,column=27,columnspan=4,sticky="news")

#khat charom

shift1=Button(root,text="⇧ Shift",height=2,width=4,relief="raised",border=5,command=lambda:shift(),bg="#F1F0E8",fg="black") 
shift1.grid(row=4,column=1,columnspan=5,sticky="news")

z=Button(root,text="z",height=2,width=4,relief="raised",border=5,command=lambda:zz())
z.grid(row=4,column=6,columnspan=2,sticky="news")

x=Button(root,text="x",height=2,width=4,relief="raised",border=5,command=lambda:xx())
x.grid(row=4,column=8,columnspan=2,sticky="news")

c=Button(root,text="c",height=2,width=4,relief="raised",border=5,command=lambda:cc())
c.grid(row=4,column=10,columnspan=2,sticky="news")

v=Button(root,text="v",height=2,width=4,relief="raised",border=5,command=lambda:vv())
v.grid(row=4,column=12,columnspan=2,sticky="news")

b=Button(root,text="b",height=2,width=4,relief="raised",border=5,command=lambda:bb())
b.grid(row=4,column=14,columnspan=2,sticky="news")

n=Button(root,text="n",height=2,width=4,relief="raised",border=5,command=lambda:nn())
n.grid(row=4,column=16,columnspan=2,sticky="news")

m=Button(root,text="m",height=2,width=4,relief="raised",border=5,command=lambda:mm())
m.grid(row=4,column=18,columnspan=2,sticky="news")

virgol=Button(root,text=",",height=2,width=4,relief="raised",border=5,command=lambda:virjol())
virgol.grid(row=4,column=20,columnspan=2,sticky="news")

noghte=Button(root,text=".",height=2,width=4,relief="raised",border=5,command=lambda:dot())
noghte.grid(row=4,column=22,columnspan=2,sticky="news")

slash=Button(root,text="/",height=2,width=4,relief="raised",border=5,command=lambda:eslash())
slash.grid(row=4,column=24,columnspan=2,sticky="news")

shift2=Button(root,text="⇧ Shift",height=2,width=4,relief="raised",border=5,command=lambda:shift(),bg="#F1F0E8",fg="black")
shift2.grid(row=4,column=26,columnspan=5,sticky="news")

#kaht akhar

ctrl1=Button(root,text="Ctrl",height=2,width=4,relief="raised",border=5,bg="#F1F0E8")
ctrl1.grid(row=5,column=1,columnspan=3,sticky="news")

windows1=Button(root,text="Win",height=2,width=4,relief="raised",border=5,bg="#F1F0E8")
windows1.grid(row=5,column=4,columnspan=2,sticky="news")

alt1=Button(root,text="Alt",height=2,width=4,relief="raised",border=5,command=lambda:shiftalt(),bg="#F1F0E8")
alt1.grid(row=5,column=6,columnspan=3,sticky="news")

space=Button(root,text="Space",height=2,width=4,fg="dark grey",relief="raised",border=5,bg="#F1F0E8",command=lambda:espace())
space.grid(row=5,column=9,columnspan=12,sticky="news")

alt2=Button(root,text="Alt",height=2,width=4,relief="raised",border=5,command=lambda:shiftalt(),bg="#F1F0E8")
alt2.grid(row=5,column=21,columnspan=3,sticky="news")

windows2=Button(root,text="Win",height=2,width=4,relief="raised",border=5,bg="#F1F0E8")
windows2.grid(row=5,column=24,columnspan=2,sticky="news")

fn=Button(root,text="""Made by
 Koosha""",height=2,width=4,fg="red",relief="raised",border=5,bg="#F1F0E8")
fn.grid(row=5,column=26,columnspan=2,sticky="news")

ctrl2=Button(root,text="Ctrl",height=2,width=4,relief="raised",border=5,activebackground="red",bg="#F1F0E8")
ctrl2.grid(row=5,column=28,columnspan=3,sticky="news")

komak=Label(root,height=1,relief="sunken",border=5,state="normal",anchor="center",width=38,font=("",22))
komak.grid(row=0,column=0,columnspan=32)




##############################    DEFS   ############################





def caps():
   global temcode
   ge=q["text"]
   dy=caps1['fg']
   if temcode==1:
    if dy=="black":
     caps1.config(fg=rang)
    else:
     caps1.config(fg="black")
    if ge=="q":
     z.config(text="Z") 
     x.config(text="X")
     c.config(text="C") 
     v.config(text="V") 
     b.config(text="B") 
     n.config(text="N") 
     m.config(text="M") 
     q.config(text="Q") 
     w.config(text="W") 
     e.config(text="E") 
     r.config(text="R") 
     t.config(text="T") 
     y.config(text="Y") 
     u.config(text="U") 
     i.config(text="I") 
     o.config(text="O") 
     p.config(text="P")
     a.config(text="A") 
     s.config(text="S")
     d.config(text="D") 
     f.config(text="F") 
     g.config(text="G") 
     h.config(text="H") 
     j.config(text="J") 
     k.config(text="K") 
     l.config(text="L") 
    elif ge=="Q":
     q.config(text="q") 
     w.config(text="w") 
     e.config(text="e") 
     r.config(text="r") 
     t.config(text="t") 
     y.config(text="y") 
     u.config(text="u") 
     i.config(text="i") 
     o.config(text="o") 
     p.config(text="p") 
     a.config(text="a")  
     s.config(text="s")  
     d.config(text="d") 
     f.config(text="f") 
     g.config(text="g") 
     h.config(text="h") 
     j.config(text="j") 
     k.config(text="k") 
     l.config(text="l") 
     z.config(text="z") 
     x.config(text="x")
     c.config(text="c") 
     v.config(text="v")  
     b.config(text="b")  
     n.config(text="n")  
     m.config(text="m")
   elif temcode==2:
    if dy=="white":
     caps1.config(fg=rang)
    else:
     caps1.config(fg="white")
    if ge=="q":
     z.config(text="Z") 
     x.config(text="X")
     c.config(text="C") 
     v.config(text="V") 
     b.config(text="B") 
     n.config(text="N") 
     m.config(text="M") 
     q.config(text="Q") 
     w.config(text="W") 
     e.config(text="E") 
     r.config(text="R") 
     t.config(text="T") 
     y.config(text="Y") 
     u.config(text="U") 
     i.config(text="I") 
     o.config(text="O") 
     p.config(text="P")
     a.config(text="A") 
     s.config(text="S")
     d.config(text="D") 
     f.config(text="F") 
     g.config(text="G") 
     h.config(text="H") 
     j.config(text="J") 
     k.config(text="K") 
     l.config(text="L") 
    elif ge=="Q":
     q.config(text="q") 
     w.config(text="w") 
     e.config(text="e") 
     r.config(text="r") 
     t.config(text="t") 
     y.config(text="y") 
     u.config(text="u") 
     i.config(text="i") 
     o.config(text="o") 
     p.config(text="p") 
     a.config(text="a")  
     s.config(text="s")  
     d.config(text="d") 
     f.config(text="f") 
     g.config(text="g") 
     h.config(text="h") 
     j.config(text="j") 
     k.config(text="k") 
     l.config(text="l") 
     z.config(text="z") 
     x.config(text="x")
     c.config(text="c") 
     v.config(text="v")  
     b.config(text="b")  
     n.config(text="n")  
     m.config(text="m")  
def shift():
   global temcode
   es=q['text']
   dy=shift1['fg']
   if temcode==1:
    if dy=="black":
     shift1.config(fg=rang)
     shift2.config(fg=rang)
     alt1.config(bg="#FFDBC3")
     alt2.config(bg="#FFDBC3")
    else:
      shift1.config(fg="black")
      shift2.config(fg="black")
      alt1.config(bg="#F1F0E8")
      alt2.config(bg="#F1F0E8")
    if es=="q":
     manfiyek.config(text="~") 
     yek.config(text="!") 
     do.config(text="@") 
     se.config(text="#") 
     char.config(text="$") 
     panj.config(text="%") 
     shish.config(text="^") 
     haft.config(text="&") 
     hasht.config(text="*") 
     noh.config(text="(") 
     sefr.config(text=")") 
     mosavi.config(text="+") 
     khat.config(text="_") 
     q.config(text="Q") 
     w.config(text="W") 
     e.config(text="E") 
     r.config(text="R") 
     t.config(text="T") 
     y.config(text="Y") 
     u.config(text="U") 
     i.config(text="I") 
     o.config(text="O") 
     p.config(text="P") 
     korushe.config(text="{") 
     bkorushe.config(text="}") 
     a.config(text="A") 
     s.config(text="S")
     d.config(text="D") 
     f.config(text="F") 
     g.config(text="G") 
     h.config(text="H") 
     j.config(text="J") 
     k.config(text="K") 
     l.config(text="L") 
     donoghte.config(text=":") 
     potation.config(text='"') 
     z.config(text="Z") 
     x.config(text="X")
     c.config(text="C") 
     v.config(text="V") 
     b.config(text="B") 
     n.config(text="N") 
     m.config(text="M") 
     virgol.config(text="<") 
     noghte.config(text=">") 
     slash.config(text="?")     
    elif es=="Q":
     manfiyek.config(text="`") 
     yek.config(text="1") 
     do.config(text="2") 
     se.config(text="3") 
     char.config(text="4") 
     panj.config(text="5") 
     shish.config(text="6") 
     haft.config(text="7") 
     hasht.config(text="8") 
     noh.config(text="9") 
     sefr.config(text="0") 
     mosavi.config(text="=") 
     khat.config(text="-")    
     q.config(text="q") 
     w.config(text="w") 
     e.config(text="e") 
     r.config(text="r") 
     t.config(text="t") 
     y.config(text="y") 
     u.config(text="u") 
     i.config(text="i") 
     o.config(text="o") 
     p.config(text="p") 
     korushe.config(text="[") 
     bkorushe.config(text="]") 
     a.config(text="a") 
     s.config(text="s")
     d.config(text="d") 
     f.config(text="f") 
     g.config(text="g") 
     h.config(text="h") 
     j.config(text="j") 
     k.config(text="k") 
     l.config(text="l") 
     donoghte.config(text=";") 
     potation.config(text="'") 
     z.config(text="z") 
     x.config(text="x")
     c.config(text="c") 
     v.config(text="v") 
     b.config(text="b") 
     n.config(text="n") 
     m.config(text="m") 
     virgol.config(text=",") 
     noghte.config(text=".") 
     slash.config(text="/")
    elif es=="ض":
        manfiyek.config(text="×") 
        yek.config(text="!") 
        do.config(text="@") 
        se.config(text="#") 
        char.config(text="$") 
        panj.config(text="%") 
        shish.config(text="^")
        haft.config(text="&") 
        hasht.config(text="*") 
        noh.config(text=")") 
        sefr.config(text="(") 
        mosavi.config(text="+") 
        khat.config(text="_")
        q.config(text="ً") 
        w.config(text="ٌ") 
        e.config(text="ٍ") 
        r.config(text="ريال") 
        t.config(text="،") 
        y.config(text="؛") 
        u.config(text=",") 
        i.config(text="]") 
        o.config(text="[") 
        p.config(text="شششششششششششششششششششششش") 
        korushe.config(text="}") 
        bkorushe.config(text="{") 
        a.config(text="َ") 
        s.config(text="ُ")
        d.config(text="ِ") 
        f.config(text="ّ") 
        g.config(text="ۀ") 
        h.config(text="آ") 
        j.config(text="ـ") 
        k.config(text="«") 
        l.config(text="»") 
        donoghte.config(text=":") 
        potation.config(text='"') 
        z.config(text="ة") 
        x.config(text="ي")
        c.config(text="ژ") 
        v.config(text="ؤ") 
        b.config(text="إ") 
        n.config(text="أ") 
        m.config(text="ء") 
        virgol.config(text="<") 
        noghte.config(text=">") 
        slash.config(text="؟")       
    elif es=="ً":
        manfiyek.config(text="÷") 
        yek.config(text="1") 
        do.config(text="2") 
        se.config(text="3") 
        char.config(text="4") 
        panj.config(text="5") 
        shish.config(text="6")
        haft.config(text="7") 
        hasht.config(text="8") 
        noh.config(text="9") 
        sefr.config(text="0") 
        mosavi.config(text="=") 
        khat.config(text="-") 
        q.config(text="ض") 
        w.config(text="ص") 
        e.config(text="ث") 
        r.config(text="ق") 
        t.config(text="ف") 
        y.config(text="غ") 
        u.config(text="ع") 
        i.config(text="ه") 
        o.config(text="خ") 
        p.config(text="ح") 
        korushe.config(text="ج") 
        bkorushe.config(text="چ") 
        a.config(text="ش") 
        s.config(text="س")
        d.config(text="ی") 
        f.config(text="ب") 
        g.config(text="ل") 
        h.config(text="ا") 
        j.config(text="ت") 
        k.config(text="ن") 
        l.config(text="م") 
        donoghte.config(text="ک") 
        potation.config(text='گ') 
        z.config(text="ظ") 
        x.config(text="ط")
        c.config(text="ز") 
        v.config(text="ر") 
        b.config(text="ذ") 
        n.config(text="د") 
        m.config(text="ئ") 
        virgol.config(text="و") 
        noghte.config(text=".") 
        slash.config(text="/") 
   if temcode==2:
    if dy=="white":
     shift1.config(fg=rang)
     shift2.config(fg=rang)
     alt1.config(bg="#FFDBC3")
     alt2.config(bg="#FFDBC3")
    else:
      shift1.config(fg="white")
      shift2.config(fg="white")
      alt1.config(bg="grey")
      alt2.config(bg="grey")
    if es=="q":
     manfiyek.config(text="~") 
     yek.config(text="!") 
     do.config(text="@") 
     se.config(text="#") 
     char.config(text="$") 
     panj.config(text="%") 
     shish.config(text="^") 
     haft.config(text="&") 
     hasht.config(text="*") 
     noh.config(text="(") 
     sefr.config(text=")") 
     mosavi.config(text="+") 
     khat.config(text="_") 
     q.config(text="Q") 
     w.config(text="W") 
     e.config(text="E") 
     r.config(text="R") 
     t.config(text="T") 
     y.config(text="Y") 
     u.config(text="U") 
     i.config(text="I") 
     o.config(text="O") 
     p.config(text="P") 
     korushe.config(text="{") 
     bkorushe.config(text="}") 
     a.config(text="A") 
     s.config(text="S")
     d.config(text="D") 
     f.config(text="F") 
     g.config(text="G") 
     h.config(text="H") 
     j.config(text="J") 
     k.config(text="K") 
     l.config(text="L") 
     donoghte.config(text=":") 
     potation.config(text='"') 
     z.config(text="Z") 
     x.config(text="X")
     c.config(text="C") 
     v.config(text="V") 
     b.config(text="B") 
     n.config(text="N") 
     m.config(text="M") 
     virgol.config(text="<") 
     noghte.config(text=">") 
     slash.config(text="?")     
    elif es=="Q":
     manfiyek.config(text="`") 
     yek.config(text="1") 
     do.config(text="2") 
     se.config(text="3") 
     char.config(text="4") 
     panj.config(text="5") 
     shish.config(text="6") 
     haft.config(text="7") 
     hasht.config(text="8") 
     noh.config(text="9") 
     sefr.config(text="0") 
     mosavi.config(text="=") 
     khat.config(text="-")    
     q.config(text="q") 
     w.config(text="w") 
     e.config(text="e") 
     r.config(text="r") 
     t.config(text="t") 
     y.config(text="y") 
     u.config(text="u") 
     i.config(text="i") 
     o.config(text="o") 
     p.config(text="p") 
     korushe.config(text="[") 
     bkorushe.config(text="]") 
     a.config(text="a") 
     s.config(text="s")
     d.config(text="d") 
     f.config(text="f") 
     g.config(text="g") 
     h.config(text="h") 
     j.config(text="j") 
     k.config(text="k") 
     l.config(text="l") 
     donoghte.config(text=";") 
     potation.config(text="'") 
     z.config(text="z") 
     x.config(text="x")
     c.config(text="c") 
     v.config(text="v") 
     b.config(text="b") 
     n.config(text="n") 
     m.config(text="m") 
     virgol.config(text=",") 
     noghte.config(text=".") 
     slash.config(text="/")
    elif es=="ض":
        manfiyek.config(text="×") 
        yek.config(text="!") 
        do.config(text="@") 
        se.config(text="#") 
        char.config(text="$") 
        panj.config(text="%") 
        shish.config(text="^")
        haft.config(text="&") 
        hasht.config(text="*") 
        noh.config(text=")") 
        sefr.config(text="(") 
        mosavi.config(text="+") 
        khat.config(text="_")
        q.config(text="ً") 
        w.config(text="ٌ") 
        e.config(text="ٍ") 
        r.config(text="ريال") 
        t.config(text="،") 
        y.config(text="؛") 
        u.config(text=",") 
        i.config(text="]") 
        o.config(text="[") 
        p.config(text="شششششششششششششششششششششش") 
        korushe.config(text="}") 
        bkorushe.config(text="{") 
        a.config(text="َ") 
        s.config(text="ُ")
        d.config(text="ِ") 
        f.config(text="ّ") 
        g.config(text="ۀ") 
        h.config(text="آ") 
        j.config(text="ـ") 
        k.config(text="«") 
        l.config(text="»") 
        donoghte.config(text=":") 
        potation.config(text='"') 
        z.config(text="ة") 
        x.config(text="ي")
        c.config(text="ژ") 
        v.config(text="ؤ") 
        b.config(text="إ") 
        n.config(text="أ") 
        m.config(text="ء") 
        virgol.config(text="<") 
        noghte.config(text=">") 
        slash.config(text="؟")       
    elif es=="ً":
        manfiyek.config(text="÷") 
        yek.config(text="1") 
        do.config(text="2") 
        se.config(text="3") 
        char.config(text="4") 
        panj.config(text="5") 
        shish.config(text="6")
        haft.config(text="7") 
        hasht.config(text="8") 
        noh.config(text="9") 
        sefr.config(text="0") 
        mosavi.config(text="=") 
        khat.config(text="-") 
        q.config(text="ض") 
        w.config(text="ص") 
        e.config(text="ث") 
        r.config(text="ق") 
        t.config(text="ف") 
        y.config(text="غ") 
        u.config(text="ع") 
        i.config(text="ه") 
        o.config(text="خ") 
        p.config(text="ح") 
        korushe.config(text="ج") 
        bkorushe.config(text="چ") 
        a.config(text="ش") 
        s.config(text="س")
        d.config(text="ی") 
        f.config(text="ب") 
        g.config(text="ل") 
        h.config(text="ا") 
        j.config(text="ت") 
        k.config(text="ن") 
        l.config(text="م") 
        donoghte.config(text="ک") 
        potation.config(text='گ') 
        z.config(text="ظ") 
        x.config(text="ط")
        c.config(text="ز") 
        v.config(text="ر") 
        b.config(text="ذ") 
        n.config(text="د") 
        m.config(text="ئ") 
        virgol.config(text="و") 
        noghte.config(text=".") 
        slash.config(text="/") 
def shiftalt():
   global temcode
   dy=shift1['fg']
   if dy==rang :
    ed=q['text']
    dena=caps1['fg']
    if temcode==1:
     if ed== "ً" :
          if dena=="black":
            alt1.config(bg="#F1F0E8")
            alt2.config(bg="#F1F0E8")
            shift1.config(fg="black")
            shift2.config(fg="black")
            manfiyek.config(text="`") 
            yek.config(text="1") 
            do.config(text="2") 
            se.config(text="3") 
            char.config(text="4") 
            panj.config(text="5") 
            shish.config(text="6") 
            haft.config(text="7") 
            hasht.config(text="8") 
            noh.config(text="9") 
            sefr.config(text="0") 
            mosavi.config(text="=") 
            khat.config(text="-")    
            q.config(text="q") 
            w.config(text="w") 
            e.config(text="e") 
            r.config(text="r") 
            t.config(text="t") 
            y.config(text="y") 
            u.config(text="u") 
            i.config(text="i") 
            o.config(text="o") 
            p.config(text="p") 
            korushe.config(text="[") 
            bkorushe.config(text="]") 
            a.config(text="a") 
            s.config(text="s")
            d.config(text="d") 
            f.config(text="f") 
            g.config(text="g") 
            h.config(text="h") 
            j.config(text="j") 
            k.config(text="k") 
            l.config(text="l") 
            donoghte.config(text=";") 
            potation.config(text="'") 
            z.config(text="z") 
            x.config(text="x")
            c.config(text="c") 
            v.config(text="v") 
            b.config(text="b") 
            n.config(text="n") 
            m.config(text="m") 
            virgol.config(text=",") 
            noghte.config(text=".") 
            slash.config(text="/") 
          elif dena==rang:
            alt1.config(bg="#F1F0E8")
            alt2.config(bg="#F1F0E8")
            shift1.config(fg="black")
            shift2.config(fg="black")
            manfiyek.config(text="~") 
            yek.config(text="!") 
            do.config(text="@") 
            se.config(text="#") 
            char.config(text="$") 
            panj.config(text="%") 
            shish.config(text="^") 
            haft.config(text="&") 
            hasht.config(text="*") 
            noh.config(text="(") 
            sefr.config(text=")") 
            mosavi.config(text="+") 
            khat.config(text="_") 
            q.config(text="Q") 
            w.config(text="W") 
            e.config(text="E") 
            r.config(text="R") 
            t.config(text="T") 
            y.config(text="Y") 
            u.config(text="U") 
            i.config(text="I") 
            o.config(text="O") 
            p.config(text="P") 
            korushe.config(text="{") 
            bkorushe.config(text="}") 
            a.config(text="A") 
            s.config(text="S")
            d.config(text="D") 
            f.config(text="F") 
            g.config(text="G") 
            h.config(text="H") 
            j.config(text="J") 
            k.config(text="K") 
            l.config(text="L") 
            donoghte.config(text=":") 
            potation.config(text='"') 
            z.config(text="Z") 
            x.config(text="X")
            c.config(text="C") 
            v.config(text="V") 
            b.config(text="B") 
            n.config(text="N") 
            m.config(text="M") 
            virgol.config(text="<") 
            noghte.config(text=">") 
            slash.config(text="?") 
     elif ed=="q" or "Q":
            alt1.config(bg="#F1F0E8")
            alt2.config(bg="#F1F0E8")
            shift1.config(fg="black",relief="raised")
            shift2.config(fg="black",relief="raised")
            manfiyek.config(text="÷") 
            yek.config(text="1") 
            do.config(text="2") 
            se.config(text="3") 
            char.config(text="4") 
            panj.config(text="5") 
            shish.config(text="6")
            haft.config(text="7") 
            hasht.config(text="8") 
            noh.config(text="9") 
            sefr.config(text="0") 
            mosavi.config(text="=") 
            khat.config(text="-") 
            q.config(text="ض") 
            w.config(text="ص") 
            e.config(text="ث") 
            r.config(text="ق") 
            t.config(text="ف") 
            y.config(text="غ") 
            u.config(text="ع") 
            i.config(text="ه") 
            o.config(text="خ") 
            p.config(text="ح") 
            korushe.config(text="ج") 
            bkorushe.config(text="چ") 
            a.config(text="ش") 
            s.config(text="س")
            d.config(text="ی") 
            f.config(text="ب") 
            g.config(text="ل") 
            h.config(text="ا") 
            j.config(text="ت") 
            k.config(text="ن") 
            l.config(text="م") 
            donoghte.config(text="ک") 
            potation.config(text='گ') 
            z.config(text="ظ") 
            x.config(text="ط")
            c.config(text="ز") 
            v.config(text="ر") 
            b.config(text="ذ") 
            n.config(text="د") 
            m.config(text="ئ") 
            virgol.config(text="و") 
            noghte.config(text=".") 
            slash.config(text="/")
    if temcode==2:
     if ed== "ً" :
          if dena=="white":
            alt1.config(bg="grey")
            alt2.config(bg="grey")
            shift1.config(fg="white")
            shift2.config(fg="white")
            manfiyek.config(text="`") 
            yek.config(text="1") 
            do.config(text="2") 
            se.config(text="3") 
            char.config(text="4") 
            panj.config(text="5") 
            shish.config(text="6") 
            haft.config(text="7") 
            hasht.config(text="8") 
            noh.config(text="9") 
            sefr.config(text="0") 
            mosavi.config(text="=") 
            khat.config(text="-")    
            q.config(text="q") 
            w.config(text="w") 
            e.config(text="e") 
            r.config(text="r") 
            t.config(text="t") 
            y.config(text="y") 
            u.config(text="u") 
            i.config(text="i") 
            o.config(text="o") 
            p.config(text="p") 
            korushe.config(text="[") 
            bkorushe.config(text="]") 
            a.config(text="a") 
            s.config(text="s")
            d.config(text="d") 
            f.config(text="f") 
            g.config(text="g") 
            h.config(text="h") 
            j.config(text="j") 
            k.config(text="k") 
            l.config(text="l") 
            donoghte.config(text=";") 
            potation.config(text="'") 
            z.config(text="z") 
            x.config(text="x")
            c.config(text="c") 
            v.config(text="v") 
            b.config(text="b") 
            n.config(text="n") 
            m.config(text="m") 
            virgol.config(text=",") 
            noghte.config(text=".") 
            slash.config(text="/") 
          elif dena==rang:
            alt1.config(bg="grey")
            alt2.config(bg="grey")
            shift1.config(fg="white")
            shift2.config(fg="white")
            manfiyek.config(text="~") 
            yek.config(text="!") 
            do.config(text="@") 
            se.config(text="#") 
            char.config(text="$") 
            panj.config(text="%") 
            shish.config(text="^") 
            haft.config(text="&") 
            hasht.config(text="*") 
            noh.config(text="(") 
            sefr.config(text=")") 
            mosavi.config(text="+") 
            khat.config(text="_") 
            q.config(text="Q") 
            w.config(text="W") 
            e.config(text="E") 
            r.config(text="R") 
            t.config(text="T") 
            y.config(text="Y") 
            u.config(text="U") 
            i.config(text="I") 
            o.config(text="O") 
            p.config(text="P") 
            korushe.config(text="{") 
            bkorushe.config(text="}") 
            a.config(text="A") 
            s.config(text="S")
            d.config(text="D") 
            f.config(text="F") 
            g.config(text="G") 
            h.config(text="H") 
            j.config(text="J") 
            k.config(text="K") 
            l.config(text="L") 
            donoghte.config(text=":") 
            potation.config(text='"') 
            z.config(text="Z") 
            x.config(text="X")
            c.config(text="C") 
            v.config(text="V") 
            b.config(text="B") 
            n.config(text="N") 
            m.config(text="M") 
            virgol.config(text="<") 
            noghte.config(text=">") 
            slash.config(text="?") 
     elif ed=="q" or "Q":
            alt1.config(bg="grey")
            alt2.config(bg="grey")
            shift1.config(fg="white")
            shift2.config(fg="white")
            manfiyek.config(text="÷") 
            yek.config(text="1") 
            do.config(text="2") 
            se.config(text="3") 
            char.config(text="4") 
            panj.config(text="5") 
            shish.config(text="6")
            haft.config(text="7") 
            hasht.config(text="8") 
            noh.config(text="9") 
            sefr.config(text="0") 
            mosavi.config(text="=") 
            khat.config(text="-") 
            q.config(text="ض") 
            w.config(text="ص") 
            e.config(text="ث") 
            r.config(text="ق") 
            t.config(text="ف") 
            y.config(text="غ") 
            u.config(text="ع") 
            i.config(text="ه") 
            o.config(text="خ") 
            p.config(text="ح") 
            korushe.config(text="ج") 
            bkorushe.config(text="چ") 
            a.config(text="ش") 
            s.config(text="س")
            d.config(text="ی") 
            f.config(text="ب") 
            g.config(text="ل") 
            h.config(text="ا") 
            j.config(text="ت") 
            k.config(text="ن") 
            l.config(text="م") 
            donoghte.config(text="ک") 
            potation.config(text='گ') 
            z.config(text="ظ") 
            x.config(text="ط")
            c.config(text="ز") 
            v.config(text="ر") 
            b.config(text="ذ") 
            n.config(text="د") 
            m.config(text="ئ") 
            virgol.config(text="و") 
            noghte.config(text=".") 
            slash.config(text="/") 
       
def backspace():
   dis=komak['text']
   Str = dis[:-1]
   komak.config(text=Str)
def espace():
   dis=komak['text']
   komak.config(text=dis+" ")         
def qq():
   es=q['text']
   dis=komak['text']
   komak.config(text=dis+es)
def ww():
   es=w['text']
   dis=komak['text']
   komak.config(text=dis+es)
def ee():
   es=e['text']
   dis=komak['text']
   komak.config(text=dis+es)
def rr():
   es=r['text']
   dis=komak['text']
   komak.config(text=dis+es)
def tt():
   es=t['text']
   dis=komak['text']
   komak.config(text=dis+es)
def yy():
   es=y['text']
   dis=komak['text']
   komak.config(text=dis+es)
def uu():
   es=u['text']
   dis=komak['text']
   komak.config(text=dis+es)
def ii():
   es=i['text']
   dis=komak['text']
   komak.config(text=dis+es)
def oo():
   es=o['text']
   dis=komak['text']
   komak.config(text=dis+es)
def pp():
   es=p['text']
   dis=komak['text']
   komak.config(text=dis+es)
def koroshe():
   es=korushe['text']
   dis=komak['text']
   komak.config(text=dis+es)
def bkoroshe():
   es=bkorushe['text']
   dis=komak['text']
   komak.config(text=dis+es)
def aa():
   es=a['text']
   dis=komak['text']
   komak.config(text=dis+es)
def ss():
   es=s['text']
   dis=komak['text']
   komak.config(text=dis+es)
def dd():
   es=d['text']
   dis=komak['text']
   komak.config(text=dis+es)
def ff():
   es=f['text']
   dis=komak['text']
   komak.config(text=dis+es)
def gg():
   es=g['text']
   dis=komak['text']
   komak.config(text=dis+es)
def hh():
   es=h['text']
   dis=komak['text']
   komak.config(text=dis+es)
def jj():
   es=j['text']
   dis=komak['text']
   komak.config(text=dis+es)
def kk():
   es=k['text']
   dis=komak['text']
   komak.config(text=dis+es)
def ll():
   es=l['text']
   dis=komak['text']
   komak.config(text=dis+es)
def dodot():
   es=donoghte['text']
   dis=komak['text']
   komak.config(text=dis+es)
def potaishen():
   es=potation['text']
   dis=komak['text']
   komak.config(text=dis+es)
def zz():
   es=z['text']
   dis=komak['text']
   komak.config(text=dis+es)
def xx():
   es=x['text']
   dis=komak['text']
   komak.config(text=dis+es)
def cc():
   es=c['text']
   dis=komak['text']
   komak.config(text=dis+es)
def vv():
   es=v['text']
   dis=komak['text']
   komak.config(text=dis+es)
def bb():
   es=b['text']
   dis=komak['text']
   komak.config(text=dis+es)
def nn():
   es=n['text']
   dis=komak['text']
   komak.config(text=dis+es)
def mm():
   es=m['text']
   dis=komak['text']
   komak.config(text=dis+es)
def virjol():
   es=virgol['text']
   dis=komak['text']
   komak.config(text=dis+es)
def dot():
   es=noghte['text']
   dis=komak['text']
   komak.config(text=dis+es)
def eslash():
   es=slash['text']
   dis=komak['text']
   komak.config(text=dis+es)
def yak():
   es=yek['text']
   dis=komak['text']
   komak.config(text=dis+es)
def du():
   es=do['text']
   dis=komak['text']
   komak.config(text=dis+es)
def si():
   es=se['text']
   dis=komak['text']
   komak.config(text=dis+es)
def chaar():
   es=char['text']
   dis=komak['text']
   komak.config(text=dis+es)
def pang():
   es=panj['text']
   dis=komak['text']
   komak.config(text=dis+es)
def shesh():
   es=shish['text']
   dis=komak['text']
   komak.config(text=dis+es)
def hafte():
   es=haft['text']
   dis=komak['text']
   komak.config(text=dis+es)
def hashte():
   es=hasht['text']
   dis=komak['text']
   komak.config(text=dis+es)
def nah():
   es=noh['text']
   dis=komak['text']
   komak.config(text=dis+es)
def sofre():
   es=sefr['text']
   dis=komak['text']
   komak.config(text=dis+es)
def khatefasele():
   es=khat['text']
   dis=komak['text']
   komak.config(text=dis+es)
def movasi():
   es=mosavi['text']
   dis=komak['text']
   komak.config(text=dis+es)
def manfiyak():
   es=manfiyek['text']
   dis=komak['text']
   komak.config(text=dis+es)



###################################### TOP LEVEL ######################################



def escape():
   global codeclr
   ak=Toplevel()
   ak.title("Setting")
   clr=Label(ak,text="Colors:")
   clr.grid(row=1,column=1,pady=5)
   exit=Button(ak,text="Exit",bg="grey",border=4,relief="raised",command=lambda:ext(),width=5)
   exit.grid(row=8,column=5,padx=5,pady=5)
   save=Button(ak,text="Save",bg="dark grey",border=4,relief="raised",command=lambda:saive(),width=5)
   save.grid(row=8,column=4,padx=5,pady=5)
   if rang=="dark red":
    zereshki=Button(ak,text="Dark red",height=1,width=7,border=3,relief="raised",fg="black",command=lambda:dred(),bg="dark red")
    zereshki.grid(row=2,column=1)
    ghermez=Button(ak,text="Red",height=1,width=7,border=3,relief="raised",fg="black",command=lambda:red(),bg="#f0f0f0")
    ghermez.grid(row=2,column=2)
    narenji=Button(ak,text="Orange",height=1,width=7,border=3,relief="raised",fg="orange",command=lambda:orange(),bg="#f0f0f0")
    narenji.grid(row=2,column=3)
    zard=Button(ak,text="Yellow",height=1,width=7,border=3,relief="raised",fg="yellow",command=lambda:yellow(),bg="#f0f0f0")
    zard.grid(row=2,column=4)
    sabz=Button(ak,text="Green",height=1,width=7,border=3,relief="raised",fg="green",command=lambda:green(),bg="#f0f0f0")
    sabz.grid(row=2,column=5)
    sabztire=Button(ak,text="Dark green",height=1,width=7,border=3,relief="raised",fg="dark green",command=lambda:dgreen(),bg="#f0f0f0")
    sabztire.grid(row=3,column=5)
    abiroshan=Button(ak,text="Cyan",height=1,width=7,border=3,relief="raised",fg="cyan",command=lambda:cyan(),bg="#f0f0f0")
    abiroshan.grid(row=3,column=4)
    abi=Button(ak,text="Blue",height=1,width=7,border=3,relief="raised",fg="blue",command=lambda:blue(),bg="#f0f0f0")
    abi.grid(row=3,column=3)
    banafsh=Button(ak,text="Purple",height=1,width=7,border=3,relief="raised",fg="purple",command=lambda:purple(),bg="#f0f0f0")
    banafsh.grid(row=3,column=2)
    sorati=Button(ak,text="Pink",height=1,width=7,border=3,relief="raised",fg="pink",command=lambda:pink(),bg="#f0f0f0")
    sorati.grid(row=3,column=1)
   elif rang=="red":
    zereshki=Button(ak,text="Dark red",height=1,width=7,border=3,relief="raised",fg="dark red",command=lambda:dred(),bg="#f0f0f0")
    zereshki.grid(row=2,column=1)
    ghermez=Button(ak,text="Red",height=1,width=7,border=3,relief="raised",bg="red",fg="black",command=lambda:red())
    ghermez.grid(row=2,column=2)
    narenji=Button(ak,text="Orange",height=1,width=7,border=3,relief="raised",fg="orange",command=lambda:orange(),bg="#f0f0f0")
    narenji.grid(row=2,column=3)
    zard=Button(ak,text="Yellow",height=1,width=7,border=3,relief="raised",fg="yellow",command=lambda:yellow(),bg="#f0f0f0")
    zard.grid(row=2,column=4)
    sabz=Button(ak,text="Green",height=1,width=7,border=3,relief="raised",fg="green",command=lambda:green(),bg="#f0f0f0")
    sabz.grid(row=2,column=5)
    sabztire=Button(ak,text="Dark green",height=1,width=7,border=3,relief="raised",fg="dark green",command=lambda:dgreen(),bg="#f0f0f0")
    sabztire.grid(row=3,column=5)
    abiroshan=Button(ak,text="Cyan",height=1,width=7,border=3,relief="raised",fg="cyan",command=lambda:cyan(),bg="#f0f0f0")
    abiroshan.grid(row=3,column=4)
    abi=Button(ak,text="Blue",height=1,width=7,border=3,relief="raised",fg="blue",command=lambda:blue(),bg="#f0f0f0")
    abi.grid(row=3,column=3)
    banafsh=Button(ak,text="Purple",height=1,width=7,border=3,relief="raised",fg="purple",command=lambda:purple(),bg="#f0f0f0")
    banafsh.grid(row=3,column=2)
    sorati=Button(ak,text="Pink",height=1,width=7,border=3,relief="raised",fg="pink",command=lambda:pink(),bg="#f0f0f0")
    sorati.grid(row=3,column=1)
   elif rang=="orange":
    zereshki=Button(ak,text="Dark red",height=1,width=7,border=3,relief="raised",fg="dark red",command=lambda:dred(),bg="#f0f0f0")
    zereshki.grid(row=2,column=1)
    ghermez=Button(ak,text="Red",height=1,width=7,border=3,relief="raised",fg="red",command=lambda:red(),bg="#f0f0f0")
    ghermez.grid(row=2,column=2)
    narenji=Button(ak,text="Orange",height=1,width=7,border=3,relief="raised",fg="black",command=lambda:orange(),bg="orange")
    narenji.grid(row=2,column=3)
    zard=Button(ak,text="Yellow",height=1,width=7,border=3,relief="raised",fg="yellow",command=lambda:yellow(),bg="#f0f0f0")
    zard.grid(row=2,column=4)
    sabz=Button(ak,text="Green",height=1,width=7,border=3,relief="raised",fg="green",command=lambda:green(),bg="#f0f0f0")
    sabz.grid(row=2,column=5)
    sabztire=Button(ak,text="Dark green",height=1,width=7,border=3,relief="raised",fg="dark green",command=lambda:dgreen(),bg="#f0f0f0")
    sabztire.grid(row=3,column=5)
    abiroshan=Button(ak,text="Cyan",height=1,width=7,border=3,relief="raised",fg="cyan",command=lambda:cyan(),bg="#f0f0f0")
    abiroshan.grid(row=3,column=4)
    abi=Button(ak,text="Blue",height=1,width=7,border=3,relief="raised",fg="blue",command=lambda:blue(),bg="#f0f0f0")
    abi.grid(row=3,column=3)
    banafsh=Button(ak,text="Purple",height=1,width=7,border=3,relief="raised",fg="purple",command=lambda:purple(),bg="#f0f0f0")
    banafsh.grid(row=3,column=2)
    sorati=Button(ak,text="Pink",height=1,width=7,border=3,relief="raised",fg="pink",command=lambda:pink(),bg="#f0f0f0")
    sorati.grid(row=3,column=1)
   elif rang=="yellow":
    zereshki=Button(ak,text="Dark red",height=1,width=7,border=3,relief="raised",fg="dark red",command=lambda:dred(),bg="#f0f0f0")
    zereshki.grid(row=2,column=1)
    ghermez=Button(ak,text="Red",height=1,width=7,border=3,relief="raised",fg="red",command=lambda:red(),bg="#f0f0f0")
    ghermez.grid(row=2,column=2)
    narenji=Button(ak,text="Orange",height=1,width=7,border=3,relief="raised",fg="orange",command=lambda:orange(),bg="#f0f0f0")
    narenji.grid(row=2,column=3)
    zard=Button(ak,text="Yellow",height=1,width=7,border=3,relief="raised",fg="black",command=lambda:yellow(),bg="yellow")
    zard.grid(row=2,column=4)
    sabz=Button(ak,text="Green",height=1,width=7,border=3,relief="raised",fg="green",command=lambda:green(),bg="#f0f0f0")
    sabz.grid(row=2,column=5)
    sabztire=Button(ak,text="Dark green",height=1,width=7,border=3,relief="raised",fg="dark green",command=lambda:dgreen(),bg="#f0f0f0")
    sabztire.grid(row=3,column=5)
    abiroshan=Button(ak,text="Cyan",height=1,width=7,border=3,relief="raised",fg="cyan",command=lambda:cyan(),bg="#f0f0f0")
    abiroshan.grid(row=3,column=4)
    abi=Button(ak,text="Blue",height=1,width=7,border=3,relief="raised",fg="blue",command=lambda:blue(),bg="#f0f0f0")
    abi.grid(row=3,column=3)
    banafsh=Button(ak,text="Purple",height=1,width=7,border=3,relief="raised",fg="purple",command=lambda:purple(),bg="#f0f0f0")
    banafsh.grid(row=3,column=2)
    sorati=Button(ak,text="Pink",height=1,width=7,border=3,relief="raised",fg="pink",command=lambda:pink(),bg="#f0f0f0")
    sorati.grid(row=3,column=1)
   elif rang=="green":
    zereshki=Button(ak,text="Dark red",height=1,width=7,border=3,relief="raised",fg="dark red",command=lambda:dred(),bg="#f0f0f0")
    zereshki.grid(row=2,column=1)
    ghermez=Button(ak,text="Red",height=1,width=7,border=3,relief="raised",fg="red",command=lambda:red(),bg="#f0f0f0")
    ghermez.grid(row=2,column=2)
    narenji=Button(ak,text="Orange",height=1,width=7,border=3,relief="raised",fg="orange",command=lambda:orange(),bg="#f0f0f0")
    narenji.grid(row=2,column=3)
    zard=Button(ak,text="Yellow",height=1,width=7,border=3,relief="raised",fg="yellow",command=lambda:yellow(),bg="#f0f0f0")
    zard.grid(row=2,column=4)
    sabz=Button(ak,text="Green",height=1,width=7,border=3,relief="raised",fg="black",command=lambda:green(),bg="green")
    sabz.grid(row=2,column=5)
    sabztire=Button(ak,text="Dark green",height=1,width=7,border=3,relief="raised",fg="dark green",command=lambda:dgreen(),bg="#f0f0f0")
    sabztire.grid(row=3,column=5)
    abiroshan=Button(ak,text="Cyan",height=1,width=7,border=3,relief="raised",fg="cyan",command=lambda:cyan(),bg="#f0f0f0")
    abiroshan.grid(row=3,column=4)
    abi=Button(ak,text="Blue",height=1,width=7,border=3,relief="raised",fg="blue",command=lambda:blue(),bg="#f0f0f0")
    abi.grid(row=3,column=3)
    banafsh=Button(ak,text="Purple",height=1,width=7,border=3,relief="raised",fg="purple",command=lambda:purple(),bg="#f0f0f0")
    banafsh.grid(row=3,column=2)
    sorati=Button(ak,text="Pink",height=1,width=7,border=3,relief="raised",fg="pink",command=lambda:pink(),bg="#f0f0f0")
    sorati.grid(row=3,column=1)
   elif rang=="dark green":
    zereshki=Button(ak,text="Dark red",height=1,width=7,border=3,relief="raised",fg="dark red",command=lambda:dred(),bg="#f0f0f0")
    zereshki.grid(row=2,column=1)
    ghermez=Button(ak,text="Red",height=1,width=7,border=3,relief="raised",fg="red",command=lambda:red(),bg="#f0f0f0")
    ghermez.grid(row=2,column=2)
    narenji=Button(ak,text="Orange",height=1,width=7,border=3,relief="raised",fg="orange",command=lambda:orange(),bg="#f0f0f0")
    narenji.grid(row=2,column=3)
    zard=Button(ak,text="Yellow",height=1,width=7,border=3,relief="raised",fg="yellow",command=lambda:yellow(),bg="#f0f0f0")
    zard.grid(row=2,column=4)
    sabz=Button(ak,text="Green",height=1,width=7,border=3,relief="raised",fg="green",command=lambda:green(),bg="#f0f0f0")
    sabz.grid(row=2,column=5)
    sabztire=Button(ak,text="Dark green",height=1,width=7,border=3,relief="raised",fg="black",command=lambda:dgreen(),bg="dark green")
    sabztire.grid(row=3,column=5)
    abiroshan=Button(ak,text="Cyan",height=1,width=7,border=3,relief="raised",fg="cyan",command=lambda:cyan(),bg="#f0f0f0")
    abiroshan.grid(row=3,column=4)
    abi=Button(ak,text="Blue",height=1,width=7,border=3,relief="raised",fg="blue",command=lambda:blue(),bg="#f0f0f0")
    abi.grid(row=3,column=3)
    banafsh=Button(ak,text="Purple",height=1,width=7,border=3,relief="raised",fg="purple",command=lambda:purple(),bg="#f0f0f0")
    banafsh.grid(row=3,column=2)
    sorati=Button(ak,text="Pink",height=1,width=7,border=3,relief="raised",fg="pink",command=lambda:pink(),bg="#f0f0f0")
    sorati.grid(row=3,column=1)
   elif rang=="cyan":
    zereshki=Button(ak,text="Dark red",height=1,width=7,border=3,relief="raised",fg="dark red",command=lambda:dred(),bg="#f0f0f0")
    zereshki.grid(row=2,column=1)
    ghermez=Button(ak,text="Red",height=1,width=7,border=3,relief="raised",fg="red",command=lambda:red(),bg="#f0f0f0")
    ghermez.grid(row=2,column=2)
    narenji=Button(ak,text="Orange",height=1,width=7,border=3,relief="raised",fg="orange",command=lambda:orange(),bg="#f0f0f0")
    narenji.grid(row=2,column=3)
    zard=Button(ak,text="Yellow",height=1,width=7,border=3,relief="raised",fg="yellow",command=lambda:yellow(),bg="#f0f0f0")
    zard.grid(row=2,column=4)
    sabz=Button(ak,text="Green",height=1,width=7,border=3,relief="raised",fg="green",command=lambda:green(),bg="#f0f0f0")
    sabz.grid(row=2,column=5)
    sabztire=Button(ak,text="Dark green",height=1,width=7,border=3,relief="raised",fg="dark green",command=lambda:dgreen(),bg="#f0f0f0")
    sabztire.grid(row=3,column=5)
    abiroshan=Button(ak,text="Cyan",height=1,width=7,border=3,relief="raised",fg="black",command=lambda:cyan(),bg="cyan")
    abiroshan.grid(row=3,column=4)
    abi=Button(ak,text="Blue",height=1,width=7,border=3,relief="raised",fg="blue",command=lambda:blue(),bg="#f0f0f0")
    abi.grid(row=3,column=3)
    banafsh=Button(ak,text="Purple",height=1,width=7,border=3,relief="raised",fg="purple",command=lambda:purple(),bg="#f0f0f0")
    banafsh.grid(row=3,column=2)
    sorati=Button(ak,text="Pink",height=1,width=7,border=3,relief="raised",fg="pink",command=lambda:pink(),bg="#f0f0f0")
    sorati.grid(row=3,column=1)
   elif rang=="blue":
    zereshki=Button(ak,text="Dark red",height=1,width=7,border=3,relief="raised",fg="dark red",command=lambda:dred(),bg="#f0f0f0")
    zereshki.grid(row=2,column=1)
    ghermez=Button(ak,text="Red",height=1,width=7,border=3,relief="raised",fg="red",command=lambda:red(),bg="#f0f0f0")
    ghermez.grid(row=2,column=2)
    narenji=Button(ak,text="Orange",height=1,width=7,border=3,relief="raised",fg="orange",command=lambda:orange(),bg="#f0f0f0")
    narenji.grid(row=2,column=3)
    zard=Button(ak,text="Yellow",height=1,width=7,border=3,relief="raised",fg="yellow",command=lambda:yellow(),bg="#f0f0f0")
    zard.grid(row=2,column=4)
    sabz=Button(ak,text="Green",height=1,width=7,border=3,relief="raised",fg="green",command=lambda:green(),bg="#f0f0f0")
    sabz.grid(row=2,column=5)
    sabztire=Button(ak,text="Dark green",height=1,width=7,border=3,relief="raised",fg="dark green",command=lambda:dgreen(),bg="#f0f0f0")
    sabztire.grid(row=3,column=5)
    abiroshan=Button(ak,text="Cyan",height=1,width=7,border=3,relief="raised",fg="cyan",command=lambda:cyan(),bg="#f0f0f0")
    abiroshan.grid(row=3,column=4)
    abi=Button(ak,text="Blue",height=1,width=7,border=3,relief="raised",fg="black",command=lambda:blue(),bg="blue")
    abi.grid(row=3,column=3)
    banafsh=Button(ak,text="Purple",height=1,width=7,border=3,relief="raised",fg="purple",command=lambda:purple(),bg="#f0f0f0")
    banafsh.grid(row=3,column=2)
    sorati=Button(ak,text="Pink",height=1,width=7,border=3,relief="raised",fg="pink",command=lambda:pink(),bg="#f0f0f0")
    sorati.grid(row=3,column=1)
   elif rang=="purple":
    zereshki=Button(ak,text="Dark red",height=1,width=7,border=3,relief="raised",fg="dark red",command=lambda:dred(),bg="#f0f0f0")
    zereshki.grid(row=2,column=1)
    ghermez=Button(ak,text="Red",height=1,width=7,border=3,relief="raised",fg="red",command=lambda:red(),bg="#f0f0f0")
    ghermez.grid(row=2,column=2)
    narenji=Button(ak,text="Orange",height=1,width=7,border=3,relief="raised",fg="orange",command=lambda:orange(),bg="#f0f0f0")
    narenji.grid(row=2,column=3)
    zard=Button(ak,text="Yellow",height=1,width=7,border=3,relief="raised",fg="yellow",command=lambda:yellow(),bg="#f0f0f0")
    zard.grid(row=2,column=4)
    sabz=Button(ak,text="Green",height=1,width=7,border=3,relief="raised",fg="green",command=lambda:green(),bg="#f0f0f0")
    sabz.grid(row=2,column=5)
    sabztire=Button(ak,text="Dark green",height=1,width=7,border=3,relief="raised",fg="dark green",command=lambda:dgreen(),bg="#f0f0f0")
    sabztire.grid(row=3,column=5)
    abiroshan=Button(ak,text="Cyan",height=1,width=7,border=3,relief="raised",fg="cyan",command=lambda:cyan(),bg="#f0f0f0")
    abiroshan.grid(row=3,column=4)
    abi=Button(ak,text="Blue",height=1,width=7,border=3,relief="raised",fg="blue",command=lambda:blue(),bg="#f0f0f0")
    abi.grid(row=3,column=3)
    banafsh=Button(ak,text="Purple",height=1,width=7,border=3,relief="raised",fg="black",command=lambda:purple(),bg="purple")
    banafsh.grid(row=3,column=2)
    sorati=Button(ak,text="Pink",height=1,width=7,border=3,relief="raised",fg="pink",command=lambda:pink(),bg="#f0f0f0")
    sorati.grid(row=3,column=1)
   elif rang=="pink":
    zereshki=Button(ak,text="Dark red",height=1,width=7,border=3,relief="raised",fg="dark red",command=lambda:dred(),bg="#f0f0f0")
    zereshki.grid(row=2,column=1)
    ghermez=Button(ak,text="Red",height=1,width=7,border=3,relief="raised",fg="red",command=lambda:red(),bg="#f0f0f0")
    ghermez.grid(row=2,column=2)
    narenji=Button(ak,text="Orange",height=1,width=7,border=3,relief="raised",fg="orange",command=lambda:orange(),bg="#f0f0f0")
    narenji.grid(row=2,column=3)
    zard=Button(ak,text="Yellow",height=1,width=7,border=3,relief="raised",fg="yellow",command=lambda:yellow(),bg="#f0f0f0")
    zard.grid(row=2,column=4)
    sabz=Button(ak,text="Green",height=1,width=7,border=3,relief="raised",fg="green",command=lambda:green(),bg="#f0f0f0")
    sabz.grid(row=2,column=5)
    sabztire=Button(ak,text="Dark green",height=1,width=7,border=3,relief="raised",fg="dark green",command=lambda:dgreen(),bg="#f0f0f0")
    sabztire.grid(row=3,column=5)
    abiroshan=Button(ak,text="Cyan",height=1,width=7,border=3,relief="raised",fg="cyan",command=lambda:cyan(),bg="#f0f0f0")
    abiroshan.grid(row=3,column=4)
    abi=Button(ak,text="Blue",height=1,width=7,border=3,relief="raised",fg="blue",command=lambda:blue(),bg="#f0f0f0")
    abi.grid(row=3,column=3)
    banafsh=Button(ak,text="Purple",height=1,width=7,border=3,relief="raised",fg="purple",command=lambda:purple(),bg="#f0f0f0")
    banafsh.grid(row=3,column=2)
    sorati=Button(ak,text="Pink",height=1,width=7,border=3,relief="raised",fg="black",bg="pink",command=lambda:pink())
    sorati.grid(row=3,column=1)

   hr=Label(ak,text="-------------------------------------------------------------")
   hr.grid(row=5,column=1,columnspan=5,sticky="news")
   teme=Label(ak,text="Theme:")
   teme.grid(row=6,column=1,pady=4)
   teme=Button(ak,text="light",command=lambda:light())
   teme.grid(row=7,column=1,columnspan=2,pady=4,sticky="news")
   teme=Button(ak,text="dark",bg="dark grey",command=lambda:dark())
   teme.grid(row=7,column=3,columnspan=2,pady=4,sticky="news")




   def dred():
    zereshki.config(bg="dark red",fg="black")
    ghermez.config(bg="#f0f0f0",fg="red")
    narenji.config(bg="#f0f0f0",fg="orange")
    zard.config(bg="#f0f0f0",fg="yellow")
    sabz.config(bg="#f0f0f0",fg="green")
    sabztire.config(bg="#f0f0f0",fg="dark green")
    abiroshan.config(bg="#f0f0f0",fg="cyan")
    abi.config(bg="#f0f0f0",fg="blue")
    banafsh.config(bg="#f0f0f0",fg="purple")
    sorati.config(bg="#f0f0f0",fg="pink")
   def red():
    zereshki.config(bg="#f0f0f0",fg="dark red")
    ghermez.config(bg="red",fg="black")
    narenji.config(bg="#f0f0f0",fg="orange")
    zard.config(bg="#f0f0f0",fg="yellow")
    sabz.config(bg="#f0f0f0",fg="green")
    sabztire.config(bg="#f0f0f0",fg="dark green")
    abiroshan.config(bg="#f0f0f0",fg="cyan")
    abi.config(bg="#f0f0f0",fg="blue")
    banafsh.config(bg="#f0f0f0",fg="purple")
    sorati.config(bg="#f0f0f0",fg="pink")
   def orange():
    zereshki.config(bg="#f0f0f0",fg="dark red")
    ghermez.config(bg="#f0f0f0",fg="red")
    narenji.config(bg="orange",fg="black")
    zard.config(bg="#f0f0f0",fg="yellow")
    sabz.config(bg="#f0f0f0",fg="green")
    sabztire.config(bg="#f0f0f0",fg="dark green")
    abiroshan.config(bg="#f0f0f0",fg="cyan")
    abi.config(bg="#f0f0f0",fg="blue")
    banafsh.config(bg="#f0f0f0",fg="purple")
    sorati.config(bg="#f0f0f0",fg="pink")
   def yellow():
    zereshki.config(bg="#f0f0f0",fg="dark red")
    ghermez.config(bg="#f0f0f0",fg="red")
    narenji.config(bg="#f0f0f0",fg="orange")
    zard.config(bg="yellow",fg="black")
    sabz.config(bg="#f0f0f0",fg="green")
    sabztire.config(bg="#f0f0f0",fg="dark green")
    abiroshan.config(bg="#f0f0f0",fg="cyan")
    abi.config(bg="#f0f0f0",fg="blue")
    banafsh.config(bg="#f0f0f0",fg="purple")
    sorati.config(bg="#f0f0f0",fg="pink")
   def green():
    zereshki.config(bg="#f0f0f0",fg="dark red")
    ghermez.config(bg="#f0f0f0",fg="red")
    narenji.config(bg="#f0f0f0",fg="orange")
    zard.config(bg="#f0f0f0",fg="yellow")
    sabz.config(bg="green",fg="black")
    sabztire.config(bg="#f0f0f0",fg="dark green")
    abiroshan.config(bg="#f0f0f0",fg="cyan")
    abi.config(bg="#f0f0f0",fg="blue")
    banafsh.config(bg="#f0f0f0",fg="purple")
    sorati.config(bg="#f0f0f0",fg="pink")
   def dgreen():
    zereshki.config(bg="#f0f0f0",fg="dark red")
    ghermez.config(bg="#f0f0f0",fg="red")
    narenji.config(bg="#f0f0f0",fg="orange")
    zard.config(bg="#f0f0f0",fg="yellow")
    sabz.config(bg="#f0f0f0",fg="green")
    sabztire.config(bg="dark green",fg="black")
    abiroshan.config(bg="#f0f0f0",fg="cyan")
    abi.config(bg="#f0f0f0",fg="blue")
    banafsh.config(bg="#f0f0f0",fg="purple")
    sorati.config(bg="#f0f0f0",fg="pink")
   def cyan():
    zereshki.config(bg="#f0f0f0",fg="dark red")
    ghermez.config(bg="#f0f0f0",fg="red")
    narenji.config(bg="#f0f0f0",fg="orange")
    zard.config(bg="#f0f0f0",fg="yellow")
    sabz.config(bg="#f0f0f0",fg="green")
    sabztire.config(bg="#f0f0f0",fg="dark green")
    abiroshan.config(bg="cyan",fg="black")
    abi.config(bg="#f0f0f0",fg="blue")
    banafsh.config(bg="#f0f0f0",fg="purple")
    sorati.config(bg="#f0f0f0",fg="pink")
   def blue():
    zereshki.config(bg="#f0f0f0",fg="dark red")
    ghermez.config(bg="#f0f0f0",fg="red")
    narenji.config(bg="#f0f0f0",fg="orange")
    zard.config(bg="#f0f0f0",fg="yellow")
    sabz.config(bg="#f0f0f0",fg="green")
    sabztire.config(bg="#f0f0f0",fg="dark green")
    abiroshan.config(bg="#f0f0f0",fg="cyan")
    abi.config(bg="blue",fg="#f0f0f0")
    banafsh.config(bg="#f0f0f0",fg="purple")
    sorati.config(bg="#f0f0f0",fg="pink")
   def purple():
    zereshki.config(bg="#f0f0f0",fg="dark red")
    ghermez.config(bg="#f0f0f0",fg="red")
    narenji.config(bg="#f0f0f0",fg="orange")
    zard.config(bg="#f0f0f0",fg="yellow")
    sabz.config(bg="#f0f0f0",fg="green")
    sabztire.config(bg="#f0f0f0",fg="dark green")
    abiroshan.config(bg="#f0f0f0",fg="cyan")
    abi.config(bg="#f0f0f0",fg="blue")
    banafsh.config(bg="purple",fg="black")
    sorati.config(bg="#f0f0f0",fg="pink")
   def pink():
    zereshki.config(bg="#f0f0f0",fg="dark red")
    ghermez.config(bg="#f0f0f0",fg="red")
    narenji.config(bg="#f0f0f0",fg="orange")
    zard.config(bg="#f0f0f0",fg="yellow")
    sabz.config(bg="#f0f0f0",fg="green")
    sabztire.config(bg="#f0f0f0",fg="dark green")
    abiroshan.config(bg="#f0f0f0",fg="cyan")
    abi.config(bg="#f0f0f0",fg="blue")
    banafsh.config(bg="#f0f0f0",fg="purple")
    sorati.config(bg="pink",fg="black")
   def ext():     
     ak.destroy()
   def saive():
    global rang
    clrgt=zereshki['bg']
    clrg=ghermez['bg']
    clrn=narenji['bg']
    clrz=zard['bg']
    clrs=sabz['bg']
    clrst=sabztire['bg']
    clrar=abiroshan['bg']
    clra=abi['bg']
    clrb=banafsh['bg']
    clrp=sorati ['bg']    
    if clrgt=="dark red":
     rang="dark red"    

    elif clrg=="red":
     rang="red"

    elif clrn=="orange":
     rang="orange"

    elif clrz=="yellow":
     rang="yellow"

    elif clrs=="green":
     rang="green"      

    elif clrst=="dark green":
     rang="dark green"

    elif clrar=="cyan":
     rang="cyan"

    elif clra=="blue":
     rang="blue"

    elif b=="purple":
     rang="purple"

    elif p=="pink":
     rang="pink"
    if temcode==2:
           esc.config(bg="grey",fg="white")
           tab.config(bg="grey",fg="white")
           caps1.config(bg="grey",fg="white")
           windows1.config(bg="grey",fg="white")
           windows2.config(bg="grey",fg="white")
           alt2.config(bg="grey",fg="white")
           alt1.config(bg="grey",fg="white")
           shift1.config(bg="grey",fg="white")
           shift2.config(bg="grey",fg="white")
           ctrl1.config(bg="grey",fg="white")
           ctrl2.config(bg="grey",fg="white")
           space.config(bg="grey",fg="white")
           fn.config(bg="grey")
           enter.config(bg="grey",fg="white")
           enter2.config(bg="grey",fg="white")
           backespace.config(bg="grey",fg="white")
           manfiyek.config(bg="dark grey",fg="white")
           yek.config(bg="dark grey",fg="white")
           do.config(bg="dark grey",fg="white")
           se.config(bg="dark grey",fg="white")
           char.config(bg="dark grey",fg="white")
           panj.config(bg="dark grey",fg="white")
           shish.config(bg="dark grey",fg="white")
           haft.config(bg="dark grey",fg="white")
           hasht.config(bg="dark grey",fg="white")
           noh.config(bg="dark grey",fg="white")
           sefr.config(bg="dark grey",fg="white")
           mosavi.config(bg="dark grey",fg="white")
           khat.config(bg="dark grey",fg="white")
           q.config(bg="dark grey",fg="white")
           w.config(bg="dark grey",fg="white")
           e.config(bg="dark grey",fg="white")
           r.config(bg="dark grey",fg="white")
           t.config(bg="dark grey",fg="white")
           y.config(bg="dark grey",fg="white")
           u.config(bg="dark grey",fg="white")
           i.config(bg="dark grey",fg="white")
           o.config(bg="dark grey",fg="white")
           p.config(bg="dark grey",fg="white")
           korushe.config(bg="dark grey",fg="white")
           bkorushe.config(bg="dark grey",fg="white")
           a.config(bg="dark grey",fg="white")
           s.config(bg="dark grey",fg="white")
           d.config(bg="dark grey",fg="white")
           f.config(bg="dark grey",fg="white")
           g.config(bg="dark grey",fg="white")
           h.config(bg="dark grey",fg="white")
           j.config(bg="dark grey",fg="white")
           k.config(bg="dark grey",fg="white")
           l.config(bg="dark grey",fg="white")
           donoghte.config(bg="dark grey",fg="white")
           potation.config(bg="dark grey",fg="white")
           z.config(bg="dark grey",fg="white")
           x.config(bg="dark grey",fg="white")
           c.config(bg="dark grey",fg="white")
           v.config(bg="dark grey",fg="white")
           b.config(bg="dark grey",fg="white")
           n.config(bg="dark grey",fg="white")
           m.config(bg="dark grey",fg="white")
           virgol.config(bg="dark grey",fg="white")
           noghte.config(bg="dark grey",fg="white")
           slash.config(bg="dark grey",fg="white")
    elif temcode==1:
           esc.config(bg="#F1F0E8",fg="black")
           tab.config(bg="#F1F0E8",fg="black")
           caps1.config(bg="#F1F0E8",fg="black")
           windows1.config(bg="#F1F0E8",fg="black")
           windows2.config(bg="#F1F0E8",fg="black")
           alt1.config(bg="#F1F0E8",fg="black")
           alt2.config(bg="#F1F0E8",fg="black")
           shift1.config(bg="#F1F0E8",fg="black")
           shift2.config(bg="#F1F0E8",fg="black")
           ctrl1.config(bg="#F1F0E8",fg="black")
           ctrl2.config(bg="#F1F0E8",fg="black")
           space.config(bg="#F1F0E8",fg="black")
           fn.config(bg="#F1F0E8",fg="black")
           enter.config(bg="#F1F0E8",fg="black")
           enter2.config(bg="#F1F0E8",fg="black")
           backespace.config(bg="#F1F0E8",fg="black")
           manfiyek.config(bg="#f0f0f0",fg="black")
           yek.config(bg="#f0f0f0",fg="black")
           do.config(bg="#f0f0f0",fg="black")
           se.config(bg="#f0f0f0",fg="black")
           char.config(bg="#f0f0f0",fg="black")
           panj.config(bg="#f0f0f0",fg="black")
           shish.config(bg="#f0f0f0",fg="black")
           haft.config(bg="#f0f0f0",fg="black")
           hasht.config(bg="#f0f0f0",fg="black")
           noh.config(bg="#f0f0f0",fg="black")
           sefr.config(bg="#f0f0f0",fg="black")
           mosavi.config(bg="#f0f0f0",fg="black")
           khat.config(bg="#f0f0f0",fg="black")
           q.config(bg="#f0f0f0",fg="black")
           w.config(bg="#f0f0f0",fg="black")
           e.config(bg="#f0f0f0",fg="black")
           r.config(bg="#f0f0f0",fg="black")
           t.config(bg="#f0f0f0",fg="black")
           y.config(bg="#f0f0f0",fg="black")
           u.config(bg="#f0f0f0",fg="black")
           i.config(bg="#f0f0f0",fg="black")
           o.config(bg="#f0f0f0",fg="black")
           p.config(bg="#f0f0f0",fg="black")
           korushe.config(bg="#f0f0f0",fg="black")
           bkorushe.config(bg="#f0f0f0",fg="black")
           a.config(bg="#f0f0f0",fg="black")
           s.config(bg="#f0f0f0",fg="black")
           d.config(bg="#f0f0f0",fg="black")
           f.config(bg="#f0f0f0",fg="black")
           g.config(bg="#f0f0f0",fg="black")
           h.config(bg="#f0f0f0",fg="black")
           j.config(bg="#f0f0f0",fg="black")
           k.config(bg="#f0f0f0",fg="black")
           l.config(bg="#f0f0f0",fg="black")
           donoghte.config(bg="#f0f0f0",fg="black")
           potation.config(bg="#f0f0f0",fg="black")
           z.config(bg="#f0f0f0",fg="black")
           x.config(bg="#f0f0f0",fg="black")
           c.config(bg="#f0f0f0",fg="black")
           v.config(bg="#f0f0f0",fg="black")
           b.config(bg="#f0f0f0",fg="black")
           n.config(bg="#f0f0f0",fg="black")
           m.config(bg="#f0f0f0",fg="black")
           virgol.config(bg="#f0f0f0",fg="black")
           noghte.config(bg="#f0f0f0",fg="black")
           slash.config(bg="#f0f0f0",fg="black")
   def light():
     global temcode
     temcode=1
   def dark():
     global temcode
     temcode=2




root.mainloop()
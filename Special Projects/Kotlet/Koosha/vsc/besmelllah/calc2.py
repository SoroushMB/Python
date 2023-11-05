from tkinter import Tk,Button,Label,Entry
import math
import os
os.system("cls")
root=Tk()
u='481x447'
y='381x447'
i='626x447'
root.geometry(u)
root.title("calk")
root['bg']="white"
a="dark green"
#############operators
def calc_close():
  root.geometry(u)
  

def calc_color():
  s=str(entry1.get())
  root.geometry(u)
  button_mosavi.config(bg=s)
  entry1.config(fg=s)

def get_jam():
  g=(labelmain['text'])
  ge=(g)
  labelone.config(text="+",fg="dark grey")
  labelmain.config(text="")
  label2_2.config(text=g,fg="dark grey")
  label3_4.config(text="",fg="dark grey")
  F="+"

def get_menha():
  g=labelmain['text']
  ge=int(g)
  labelone.config(text="-",fg="dark grey")
  labelmain.config(text="")
  label2_2.config(text=g,fg="dark grey")
  label3_4.config(text="",fg="dark grey")
  F="-"

def get_zarb():
  g=labelmain['text']
  ge=int(g)
  labelone.config(text="×",fg="dark grey")
  labelmain.config(text="")
  label2_2.config(text=g,fg="dark grey")
  label3_4.config(text="",fg="dark grey")
  F="×"
def get_taghsim():
  g=labelmain['text']
  ge=int(g)
  labelone.config(text="÷",fg="dark grey")
  labelmain.config(text="")
  label2_2.config(text=g,fg="dark grey")
  label3_4.config(text="",fg="dark grey")
  F="÷"

def calc_tavan():
  if entry1.get()=="":
       s="dark grey"
       a=label_dl['text']
  else:
       s=entry1.get()
       a=label_dl['text']
  g=labelmain['text']
  jvb=int(g)**2
  labelmain.config(text=jvb,fg=a)
  label3_4.config(text=g,fg=s)
  labelone.config(text="×",fg=s)
  label2_2.config(text=g,fg=s)

def calc_kasr():
    if entry1.get()=="":
       s="dark grey"
       a=label_dl['text']
    else:
       s=entry1.get()
       a=label_dl['text']
    g=labelmain['text']
    jvb=1/int(g)
    labelmain.config(text=jvb,fg=a)
    label3_4.config(text=g,fg=s)
    labelone.config(text="÷",fg=s)
    label2_2.config(text="1",fg=s)

def calc_mm():
   g=labelmain['text']
   if int(g)>0:
    jvb="-"+g
    labelmain.config(text=jvb)
   elif int(g)<0:
    j=abs(int(g))
    jvb=str(j)
    labelmain.config(text=jvb)
def calc_darsad():
    if entry1.get()=="":
       s="dark grey"
       a=label_dl['text']
    else:
       s=entry1.get()
       a=label_dl['text']
    g=labelmain['text']
    jvb=int(g)/100
    labelmain.config(text=jvb,fg=a)
    label3_4.config(text="100",fg=s)
    labelone.config(text="÷",fg=s)
    label2_2.config(text=g,fg=s)   

#############mosavi

def calc_mosavi():
     F=labelone['text']
     if F=="+":
      if entry1.get()=="":
       s="dark grey"
       a=label_dl['text']
      else:
       s=entry1.get()
       a=label_dl['text']
      g=label2_2['text']
      h=labelmain['text']
      jvb=int(g)+int(h)
      labelmain.config(text=jvb,fg=a)
      label3_4.config(text=h,fg=s)
      labelone.config(fg=s)
      label2_2.config(fg=s)

     elif F=="-":
      if entry1.get()=="":
       s="dark grey"
       a=label_dl['text']
      else:
       s=entry1.get()
       a=label_dl['text']
      g=label2_2['text']
      h=labelmain['text']
      jvb=int(g)-int(h)
      labelmain.config(text=jvb,fg=a)
      label3_4.config(text=h,fg=s)
      labelone.config(fg=s)
      label2_2.config(fg=s)

     elif F=="×":
      a="black"
      if entry1.get()=="":
       s="dark grey"
       a=label_dl['text']
      else:
       s=entry1.get()
       a=label_dl['text']
      g=label2_2['text']
      h=labelmain['text']
      jvb=int(g)*int(h)
      labelmain.config(text=jvb,fg=a)
      label3_4.config(text=h,fg=s)
      labelone.config(fg=s)
      label2_2.config(fg=s)

     elif F=="÷":
      if entry1.get()=="":
       s="dark grey"
       a=label_dl['text']
      else:
       s=entry1.get()
       a=label_dl['text']
      g=label2_2['text']
      h=labelmain['text']
      jvb=int(g)/int(h)
      labelmain.config(text=jvb,fg=a)
      label3_4.config(text=h,fg=s)
      labelone.config(fg=s)
      label2_2.config(fg=s)
def calc_c():
  label2_2.config(text="")
  label3_4.config(text="")
  labelmain.config(text="")
  labelone.config(text="")
def calc_ce():
  labelmain.config(text="")
def calc_backspace():
   g=labelmain['text']
   j=int(g)//10
   if j==0:
    labelmain.config(text="")
   else:
     p=str(j)
     labelmain.config(text=p)

#############setting
def calc_setting():
  root.geometry(i)


#############calcs

def calc_1():
 a=labelmain['text']
 labelmain.config(text=f"{a}1")
def calc_2():
 a=labelmain['text']
 labelmain.config(text=f"{a}2")
def calc_3():
 a=labelmain['text']
 labelmain.config(text=f"{a}3")
def calc_4():
 a=labelmain['text']
 labelmain.config(text=f"{a}4")
def calc_5():
 a=labelmain['text']
 labelmain.config(text=f"{a}5")
def calc_6():
 a=labelmain['text']
 labelmain.config(text=f"{a}6")
def calc_7():
 a=labelmain['text']
 labelmain.config(text=f"{a}7")
def calc_8():
 a=labelmain['text']
 labelmain.config(text=f"{a}8")
def calc_9():
 a=labelmain['text']
 labelmain.config(text=f"{a}9")
def calc_0():
 a=labelmain['text']
 labelmain.config(text=f"{a}0")
def calc_dot():
 a=labelmain['text']
 labelmain.config(text=f"{a}.")
   
#############buttons

button_jam=Button(root,text="+",width=11,height=2,font="Arial,15",command=lambda:get_jam())
button_menha=Button(root,text="-",width=11,height=2,font="Arial,15",command=lambda:get_menha())
button_zarb=Button(root,text="×",width=11,height=2,font="Arial,15",command=lambda:get_zarb())
button_taghsim=Button(root,text="÷",width=11,height=2,font="Arial,15",command=lambda:get_taghsim())
button1=Button(root,text="1",width=9,height=2,font="Arial,15",command=lambda:calc_1(),bg="white")
button2=Button(root,text="2",width=9,height=2,font="Arial,15",command=lambda:calc_2(),bg="white")
button3=Button(root,text="3",width=9,height=2,font="Arial,15",command=lambda:calc_3(),bg="white")
button4=Button(root,text="4",width=9,height=2,font="Arial,15",command=lambda:calc_4(),bg="white")
button5=Button(root,text="5",width=9,height=2,font="Arial,15",command=lambda:calc_5(),bg="white")
button6=Button(root,text="6",width=9,height=2,font="Arial,15",command=lambda:calc_6(),bg="white")
button7=Button(root,text="7",width=9,height=2,font="Arial,15",command=lambda:calc_7(),bg="white")
button8=Button(root,text="8",width=9,height=2,font="Arial,15",command=lambda:calc_8(),bg="white")
button9=Button(root,text="9",width=9,height=2,font="Arial,15",command=lambda:calc_9(),bg="white")
button0=Button(root,text="0",width=9,height=2,font="Arial,15",command=lambda:calc_0(),bg="white",)
button_mosavi=Button(root,text="=",width=11,height=2,font="Arial,15",command=lambda:calc_mosavi(),bg="darkgreen",fg="white")
button_dot=Button(root,text=".",width=9,height=2,font="Arial,15",command=lambda:calc_dot())
button_ce=Button(root,text="CE",width=9,height=2,font="Arial,15",command=lambda:calc_ce())
button_c=Button(root,text="C",width=9,height=2,font="Arial,15",command=lambda:calc_c())
button_tavan=Button(root,text="x²",width=9,height=2,font="Arial,15",command=lambda:calc_tavan())
button_kasr=Button(root,text="¹⁄ₓ",width=9,height=2,font="Arial,15",command=lambda:calc_kasr())
button_mm=Button(root,text="⁺⁄₋",width=9,height=2,font="Arial,15",command=lambda:calc_mm())
button_darsad=Button(root,text="%",width=9,height=2,font="Arial,15",command=lambda:calc_darsad())
button_bs=Button(root,text="⌫",width=11,height=2,font="Arial,15",command=lambda:calc_backspace())

button_setting=Button(root,text="setting",width=9,height=2,font="Arial,15",command=lambda:calc_setting())


#############labels

labelone=Label(root,text="",fg="red",bg="white",height=3,width=10)
labelmain=Label(root,text="",height=2,width=10,fg="black",font="Arian,15")
label2_2=Label(root,text="",height=3,width=5,fg="red",bg="white")
label3_4=Label(root,text="",height=3,width=5,fg="red",bg="white")
label_dl=Label(root,text="black")
label_alaki=Label(root,text="komak",bg="white",fg="red")
#############grids
label_alaki.grid(row=1,column=1)
label2_2.grid(row=1,column=2)
labelone.grid(row=1,column=3)
label3_4.grid(row=1,column=4)
labelmain.grid(row=2,column=1,columnspan=4,sticky="news")
button_jam.grid(row=8,column=4)
button_menha.grid(row=7,column=4)
button_zarb.grid(row=6,column=4)
button_taghsim.grid(row=5,column=4)
button1.grid(row=8,column=1)
button2.grid(row=8,column=2)
button3.grid(row=8,column=3)
button4.grid(row=7,column=1)
button5.grid(row=7,column=2)
button6.grid(row=7,column=3)
button7.grid(row=6,column=1)
button8.grid(row=6,column=2)
button9.grid(row=6,column=3)
button0.grid(row=9,column=2)
button_mosavi.grid(row=9,column=4)
button_dot.grid(row=9,column=3)
button_ce.grid(row=3,column=3)
button_c.grid(row=3,column=2)
button_tavan.grid(row=5,column=2)
button_kasr.grid(row=5,column=1)
button_mm.grid(row=9,column=1)
button_darsad.grid(row=5,column=3)
button_bs.grid(row=3,column=4)
button_setting.grid(row=3,column=1)

###########color setting

label_rang=Label(root,text="  color:   ",fg="black",bg="white",font="Arial")
entry1=Entry(root,width=8,bg="#f0f0f0")
button_submit=Button(root,text="submit",width=5,height=1,font="Arial",command=lambda:calc_color())
label_rang.grid(row=2,column=5)
entry1.grid(row=3,column=5)
button_submit.grid(row=4,column=5)

############theme setting
button_light=Button(root,text="light",width=5,height=1,font="Arial",command=lambda:calc_light())
button_dark=Button(root,text="dark",width=5,height=1,font="Arial",command=lambda:calc_dark(),bg="grey",fg="white")
label_theme=Label(root,text="theme:",fg="black",bg="white")
label_theme2=Label(root,text="light",fg="black",bg="white")
button_close=Button(root,text="close",width=5,height=1,font="Arial",command=lambda:calc_close())
label_theme.grid(row=5,column=5)
label_theme2.grid(row=5,column=6)
button_light.grid(row=6,column=5)
button_dark.grid(row=6,column=6)
button_close.grid(row=8,column=6)
############def theme
def calc_dark():
  label_dl.config(text="white")
  root.config(bg="#4f4f4f")
  f="grey"
  h="dark grey"
  button0.config(bg=h,fg="white")
  button1.config(bg=h,fg="white")
  button2.config(bg=h,fg="white")
  button3.config(bg=h,fg="white")
  button4.config(bg=h,fg="white")
  button5.config(bg=h,fg="white")
  button6.config(bg=h,fg="white")
  button7.config(bg=h,fg="white")
  button8.config(bg=h,fg="white")
  button9.config(bg=h,fg="white")
  button_close.config(bg=h,fg="white")

  button_bs.config(bg=f,fg="white")
  button_c.config(bg=f,fg="white")
  button_ce.config(bg=f,fg="white")
  button_darsad.config(bg=f,fg="white")
  button_kasr.config(bg=f,fg="white")
  button_jam.config(bg=f,fg="white")
  button_menha.config(bg=f,fg="white")
  button_zarb.config(bg=f,fg="white")
  button_taghsim.config(bg=f,fg="white")
  button_tavan.config(bg=f,fg="white")
  button_dot.config(bg=f,fg="white")
  button_mm.config(bg=f,fg="white")
  button_setting.config(bg=f,fg="white")
  button_dark.config(bg=h,fg="white")
  button_submit.config(bg=f,fg="white")
  button_mosavi.config(fg="black")
  button_cos.config(bg=h,fg="white")
  button_sin.config(bg=h,fg="white")
  button_tan.config(bg=h,fg="white")

  label_alaki.config(bg="#4f4f4f")
  label2_2.config(bg="#4f4f4f")
  label3_4.config(bg="#4f4f4f")
  label_rang.config(bg="#4f4f4f",fg="white")
  label_theme.config(bg="#4f4f4f",fg="white")
  label_theme2.config(bg="#4f4f4f",fg="white",text="dark")
  labelone.config(bg="#4f4f4f")
  labelmain.config(bg="grey",fg="white") 

  entry1.config(bg="grey")

  root.geometry(u)
def calc_light():
  label_dl.config(text="black")
  root.config(bg="white")
  f="grey"
  h="white"
  button0.config(bg=h,fg="black")
  button1.config(bg=h,fg="black")
  button2.config(bg=h,fg="black")
  button3.config(bg=h,fg="black")
  button4.config(bg=h,fg="black")
  button5.config(bg=h,fg="black")
  button6.config(bg=h,fg="black")
  button7.config(bg=h,fg="black")
  button8.config(bg=h,fg="black")
  button9.config(bg=h,fg="black")
  button_close.config(bg=h,fg="black")

  button_bs.config(bg="#f0f0f0",fg="black")
  button_c.config(bg="#f0f0f0",fg="black")
  button_ce.config(bg="#f0f0f0",fg="black")
  button_darsad.config(bg="#f0f0f0",fg="black")
  button_kasr.config(bg="#f0f0f0",fg="black")
  button_jam.config(bg="#f0f0f0",fg="black")
  button_menha.config(bg="#f0f0f0",fg="black")
  button_zarb.config(bg="#f0f0f0",fg="black")
  button_taghsim.config(bg="#f0f0f0",fg="black")
  button_tavan.config(bg="#f0f0f0",fg="black")
  button_dot.config(bg="#f0f0f0",fg="black")
  button_mm.config(bg="#f0f0f0",fg="black")
  button_setting.config(bg="#f0f0f0",fg="black")
  button_light.config(bg="#f0f0f0",fg="black")
  button_submit.config(bg="#f0f0f0",fg="black")
  button_mosavi.config(fg="white")

  label_alaki.config(bg="white")
  label2_2.config(bg="white")
  label3_4.config(bg="white")
  label_rang.config(bg="white",fg="black")
  label_theme.config(bg="white",fg="black")
  label_theme2.config(bg="white",fg="black",text="light")
  labelone.config(bg="white")
  labelmain.config(bg="white",fg="black")

  button_cos.config(bg=h,fg="black")
  button_sin.config(bg=h,fg="black")
  button_tan.config(bg=h,fg="black") 

  entry1.config(bg="#f0f0f0")

  root.geometry(u)
##########sinos ina:
button_sin=Button(root,text="Sin",width=9,height=2,font="Arial,15",command=lambda:calc_sin(),bg="white",)
button_cos=Button(root,text="Cos",width=9,height=2,font="Arial,15",command=lambda:calc_cos(),bg="white",)
button_tan=Button(root,text="Tan",width=11,height=2,font="Arial,15",command=lambda:calc_tan(),bg="white",)
button_sin.grid(row=4,column=1)
button_cos.grid(row=4,column=2,columnspan=2,sticky="news")
button_tan.grid(row=4,column=4)
def calc_sin():
  g=labelmain['text']
  ge=int(g)
  a=math.sin(math.radians(ge))
  labelmain.config(text=a)
  labelone.config(text="sin")
  label3_4.config(text=g+"°")
def calc_cos():
  g=labelmain['text']
  ge=int(g)
  a=math.cos(math.radians(ge))
  labelmain.config(text=a)
  labelone.config(text="cos")
  label3_4.config(text=g+"°")
def calc_tan():
  g=labelmain['text']
  ge=int(g)
  a=math.tan(math.radians(ge))
  labelmain.config(text=a)
  labelone.config(text="tan")
  label3_4.config(text=g+"°")
root.mainloop()
from tkinter import Tk,Label,Entry,Button,LabelFrame
tak=Tk()
tak.title("salam")
root=LabelFrame(tak,relief="ridge")
root.grid(row=0,column=0,padx=7,pady=7)
lbl1=Label(root,text="hello",height=3,width=8   )
lbl2=Label(root,text="my",height=3,width=8)
lbl3=Label(root,text="name",height=3,width=8)
lbl4=Label(root,text="is",height=3,width=8)
lbl5=Label(root,text="jeff",height=3,width=8)

btn1=Button(root,text="hello",height=3,width=8,relief="raised")
btn2=Button(root,text="i",height=3,width=8,relief="raised")
btn3=Button(root,text="am",height=3,width=8,relief="raised")
btn4=Button(root,text="under",height=3,width=8,relief="raised")
btn5=Button(root,text="water",height=3,width=8,relief="raised")

ent1=Entry(root)
ent2=Entry(root)

lbl1.grid(row=0,column=1,columnspan=2,sticky="news",padx=2,pady=2)
lbl2.grid(row=0,column=3,columnspan=2,sticky="news",padx=2,pady=2)
lbl3.grid(row=0,column=5,columnspan=2,sticky="news",padx=2,pady=2)
lbl4.grid(row=0,column=7,columnspan=2,sticky="news",padx=2,pady=2)
lbl5.grid(row=0,column=9,columnspan=2,sticky="news",padx=2,pady=2)

btn1.grid(row=1,column=1,columnspan=2,sticky="news",padx=2,pady=2)
btn2.grid(row=1,column=3,columnspan=2,sticky="news",padx=2,pady=2)
btn3.grid(row=1,column=5,columnspan=2,sticky="news",padx=2,pady=2)
btn4.grid(row=1,column=7,columnspan=2,sticky="news",padx=2,pady=2)
btn5.grid(row=1,column=9,columnspan=2,sticky="news",padx=2,pady=2)

ent1.grid(row=2,column=1,columnspan=5,sticky="news",padx=2,pady=2)
ent2.grid(row=2,column=6,columnspan=5,sticky="news",padx=2,pady=2)

tak.mainloop()
from turtle import fd,lt,rt,done,bgcolor,pencolor,pensize
bgcolor("black");pencolor("RosyBrown1");pensize(10)

def Squares(LOR,District):
    if LOR == "R":
        for i in range(4):
            fd(District)
            rt(90)
    elif LOR == "L":
        for i in range(4):
            fd(District)
            lt(90)
            
Squares(LOR="R",District=100)
Squares(LOR="R",District=120)
Squares(LOR="R",District=140)
Squares(LOR="R",District=160)
Squares(LOR="R",District=180)
Squares(LOR="L",District=100)
Squares(LOR="L",District=120)
Squares(LOR="L",District=140)
Squares(LOR="L",District=160)
Squares(LOR="L",District=180)

rt(180)

Squares(LOR="R",District=100)
Squares(LOR="R",District=120)
Squares(LOR="R",District=140)
Squares(LOR="R",District=160)
Squares(LOR="R",District=180)
Squares(LOR="L",District=100)

Squares(LOR="L",District=120)
Squares(LOR="L",District=140)
Squares(LOR="L",District=160)
Squares(LOR="L",District=180)

done()

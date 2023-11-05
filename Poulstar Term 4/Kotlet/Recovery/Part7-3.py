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

for number in range(100,181,20):
    Squares(LOR="R",District=number)
for number in range(100,181,20):
    Squares(LOR="L",District=number)
rt(180)
for number in range(100,181,20):
    Squares(LOR="R",District=number)
for number in range(100,181,20):
    Squares(LOR="L",District=number)
done()
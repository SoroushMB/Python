from turtle import fd,lt,circle,done,speed,pensize,begin_fill,end_fill,fillcolor
speed(2)
pensize(width=5)
def triangle(district):
    fillcolor("black")
    begin_fill()
    for i in range(3):
        fd(district)
        lt(120)
    end_fill()
fillcolor("yellow")
begin_fill()
circle(radius=180)
end_fill()
lt(90)
fd(180)
for i in range(3):    
    for i in range(100,181,20):
        triangle(district=i)
    lt(-120)
done()
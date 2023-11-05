from turtle import fd,lt,rt,done,speed
speed(100)

def square_l(dis):
    for i in range(4):
        fd(dis)
        lt(90)
for i in range(100,181,20):
    square_l(dis=i)

def square_r(dis):
    for i in range(4):
        fd(dis)
        rt(90)
for i in range(100,181,20):
    square_r(dis=i)
    
rt(180)
for i in range(100,181,20):
    square_l(dis=i)
for i in range(100,181,20):
    square_r(dis=i)
done()

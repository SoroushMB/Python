from turtle import fd,lt,done,speed
speed(100)
def square_l(dis):
    for i in range(4):
        fd(dis)
        lt(90)
    lt(90)
for i in range(4):
    for i in range(100,181,20):
        square_l(dis=i)
done()
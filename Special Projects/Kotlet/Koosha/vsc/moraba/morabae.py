from turtle import forward,left,back


def komak(a):
    a=100
    for i in range(5):
        a=a+10
        for f in range(4):
            forward(a)
            left(90)
        for f in range(4):
            back(a)
            left(90)
komak(100)
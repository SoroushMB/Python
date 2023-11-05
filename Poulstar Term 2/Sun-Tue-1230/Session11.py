from turtle import fd,lt,pensize,pencolor,done,bgcolor

colors = ["#f00202","#11fa05","#1f74db","#fadd05"]
pensize(width=5)
bgcolor("Black")

def square(color,district):
        pencolor(color)
        for i in range(4):
            fd(district)
            lt(90)

for i in range(len(colors)):#0-3 -> i=0 , square(color=colors[3] , district=100)
    square(color=colors[i],district=100)
done()
from turtle import fd,rt,lt,pensize,pendown,penup,color,bgcolor,begin_fill,end_fill,done,speed,circle,shape,shapesize,position
# fd =  Forward , rt = Right , lt = Left
pensize(width=10)
color("#ffffff")
bgcolor("black")
shape("classic")
shapesize( 1.5 )
penup()
fd(-200)
pendown()
for i in range( 3 ):
    fd(100)
    lt(120)
for i in range(90):
    fd( 1 )
    lt( 1 )
color("cyan")
done()
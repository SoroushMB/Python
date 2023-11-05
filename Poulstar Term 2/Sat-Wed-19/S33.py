from turtle import fd,lt,rt,done,shapesize,shape,pensize,penup,pendown,bgcolor,fillcolor,color,speed,begin_fill,end_fill,setposition

def triangle(district_size):
    for i in range( 3 ):    
        fd(district_size)
        lt(120)
        
penup()
setposition(x=-500,y=-100)
pendown()
shape("turtle")
shapesize( 1.85 )
color("cyan")
pensize( 5 )
bgcolor("#153642")
fillcolor("#a18c52")
begin_fill()
speed( 5 )
for i in range( 200,241,10 ):
    triangle(district_size=i)
end_fill()
done()
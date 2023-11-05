from turtle import fd,lt,done

def square(district):
    for i in range( 4 ):
        fd(district)
        lt(90)
for i in range(100,181,20):
    square(district=i)
done()
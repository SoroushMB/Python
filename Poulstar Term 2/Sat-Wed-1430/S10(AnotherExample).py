from turtle import fd,lt,rt,done
# Define
# Variable : name = value
# Variable in Function : Parameter = Argument
def square(district):
    for i in range(4):
        fd(district)
        lt(90)
for i in range(100,181,20):
    square(district=i)
done()
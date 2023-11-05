# (x+y)**2 = x**2 + 2xy + y**2 -> 
from turtle import fd,lt,rt,done,speed
speed(1000)
def TwoSentenceSquared(x:float=1.0,y:float=2.0) -> float:
    return (x+y)**2
some_var = TwoSentenceSquared(x=6,y=7)
print(some_var,flush=True)
            
def DoingSomeAction(LOR,Dis):
    if LOR.upper() == "R":
        for i in range(4):
            fd(Dis)
            rt(90)
    elif LOR.upper() == "L":
        for i in range(4):
            fd(Dis)
            lt(90)

for i in range(100,141,10):
    DoingSomeAction(LOR="r",Dis=i)
for i in range(100,141,10):
    DoingSomeAction(LOR="l",Dis=i)

rt(180)
for i in range(100,141,10):
    DoingSomeAction(LOR="r",Dis=i)
for i in range(100,141,10):
    DoingSomeAction(LOR="l",Dis=i)

done()
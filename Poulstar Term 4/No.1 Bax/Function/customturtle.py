from turtle import fd,lt,rt,done


class Shapes:
    def __init__(self,dis:int):
        self.dis = dis
    
    def triangle(self):
        for i in range(3):
            fd(self.dis)
            lt(120)
    
    def square(self):
        for i in range(4):
            fd(self.dis)
            lt(90)
    
    def rectangle(self):
        for i in range(2):
            fd(self.dis)
            lt(90)
            fd(self.dis*2)
            lt(90)
    
    def pentagon(self):
        for i in range(5):
            fd(self.dis)
            lt(72)

    def hexagon(self):
        for i in range(6):
            fd(self.dis)
            lt(60)
    
    def custom_shape(self,dis_count:int):
        self.dis_count = dis_count
        angle = 360/int(self.dis_count)
        for i in range(self.dis_count):
            fd(self.dis)
            lt(angle=angle)

alaki = Shapes(dis=100)

alaki.custom_shape(dis_count=15)
done()
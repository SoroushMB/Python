from turtle import fd,lt,done,pensize,pencolor,bgcolor


class Shapes:
    def __init__(self,first_district,second_district):
        self.first_district = int(first_district)
        self.second_district = int(second_district)
        
    def triangle(self):
        for i in range(3):
            fd(self.first_district)
            lt(120)
        done()
        
    def square(self):
        for i in range(4):
            fd(self.first_district)
            lt(90)
        done()
        
    def rectangle(self):
        for i in range(2):
            fd(self.first_district)
            lt(90)
            fd(self.second_district)
            lt(90)
        done()

    def pentagon(self):
        for i in range(5):
            fd(self.first_district)
            lt(72)
        done()

    def hexagon(self):
        for i in range(6):
            fd(self.first_district)
            lt(60)
        done()

    def settings(self,size,pcolor,bcolor):
        pensize(size)
        pencolor(pcolor)
        bgcolor(bcolor)


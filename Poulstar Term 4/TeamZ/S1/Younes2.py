class test:
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y
    def sum(self):
        return self.x + self.y

instance1 = test()
print('Result is', instance1.sum())
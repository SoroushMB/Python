class Test():
    def __init__ (self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
    def alaki1(self):
        print('alaki')
    def show_all(self):
        print(self.a, self.b)

class Birabt:
    def __init__(self, z, y):
        self.z = z
        self.y = y    
    def print11(self):
        print(11)

class Test2(Test):
    def __init__(self, a, b, c, d, e, f=None, g=None):
        super().__init__(a, b, c, d, e)
    # def __init__(self, a, b, c, d, e, f=None, g=None):
    #     Test.__init__(self, a, b, c, d, e)
    #     self.f = f
    #     self.g = g
    def show_all(self):
        print("salam")
    
    def print20(self):
        Birabt.print11(self)

# t1 = Test(1,2,3,4,5)
# t2 = Test2(10, 20, 30, 40, 50, 60, 70)
# # print(t2.show_all())
# t2.print20()

# def add2(a, b:str) -> str:
#     a: int = 11
# print(add2(3, 4))
# print(add2('ali', 'reza'))
# a = {'a':1, "b":2}
# b = {'a':3, 'c':4}
# c = a|b
# print(c)
from typing import Final
Test: Final = 'ok'
Test *= 2
print(Test)
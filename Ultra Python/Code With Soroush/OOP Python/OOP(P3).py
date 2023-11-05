# name = input("Your name : ")
# age = input("Your age : ")
# p1 = Person(name=name,age=age)
# print(p1)
class Person:
    def __init__(jasemghasemi, name, age):
        jasemghasemi.name = name
        jasemghasemi.age = age
    def __str__(self):
        return f"{self.name}:{self.age}"
    def greeting(olagh):
        print(f"Hello, my name is {olagh.name} and I'm {olagh.age} years old!")


amir = Person(name="AmirTaha",age=15)
amir.age = 17
# del amir.age
amir.greeting()
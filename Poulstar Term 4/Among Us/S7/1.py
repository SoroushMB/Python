# OOP -> Object Oriented Programming
# Human -> Name , Age , Race
class Human:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age

first_human = Human(name="Arash",age=20)

print(first_human.age)
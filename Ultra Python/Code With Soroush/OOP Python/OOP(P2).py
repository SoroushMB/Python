# The story behind (__init__())!!!!
# Initiate
# Variable : name = value
# Function : parameter = argument
# Class : property = value
class Person:
    # Input
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Output
    def __str__(self):
        return f"Name : {self.name}  , Age : {self.age}"
    def greeting(self):
        print(f"Hello my name is {self.name}")

person_1 = Person(age=15,name="Amir")
person_2 = Person(age=21,name="Soroush")

person_1.greeting()
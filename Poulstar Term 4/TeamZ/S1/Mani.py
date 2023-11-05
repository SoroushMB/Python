class Human:

    def __init__(self, height1, weight1 , age1):

        self.height1 = height1

        self.weight1 = weight1

        self.age1 = age1

    number_of_hands = ("2")

    number_of_legs = ("2")

    number_of_eyes = ("2")

    number_of_heart = ("1")


    def height(self):

        return self.height1

    def weight(self):

        return self.weight1
    
    def age(self):

        return self.age1
    
ye_adam = Human(198 , 67 , 24)

print(ye_adam.number_of_eyes)

print(f"this person Height is {ye_adam.height()}")

print(f"this person Weight is {ye_adam.weight()}")

print(f"this person age is {ye_adam.age()}")
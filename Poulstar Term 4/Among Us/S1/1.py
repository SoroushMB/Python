# Object Oriented Programming
# Real World : Human
# Nose , Mouth , 2 Kidneys , 2 Legs , 2 Hands
# Name , Age , Height , Weight
# Attributes : Variable(Property) , Function(Methods)
class Human_Head:
    def __init__(self,hair_color,eyes_color,skin_color):
        self.hair_color = hair_color
        self.eyes_color = eyes_color
        self.skin_color = skin_color
    def naming(self,first_name,last_name):
        return first_name + last_name
    
    first_thing = "Hair"
    second_thing = "Brain"
    third_thing = "Eyes"
    fourth_thing = "Nose"
    fifth_thing = "Ears"
    sixth_thing = "Mouth"
    seventh_thing = "Chin"
    
first_head = Human_Head(hair_color="Dark Brown🗿",eyes_color="Brown🗿",skin_color="Caucasian🗿")
print(first_head.naming(first_name="Arash",last_name="Jamali"))
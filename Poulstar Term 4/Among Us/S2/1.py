# United States of America
# 7 Kinds Of Cars
# Mixing - 
class Car_Maker:
    
    """
Kinds : 9 Cars : White , Black , Blue , Green , Red , Indigo , Violet , Yellow , Orange
Owner : The name of the owner
must : "Flour","Sugar","Milk","Chocolate"
must_not :  

    """
    def __init__(self,owner,kind):
        self.kind = kind
        self.owner = owner
    
    def mixing(self):
        must = ["Flour","Sugar","Milk","Chocolate"]
        user_ingredients = []
        while True:

            for ingredient in must:
                print(ingredient)
            user_selected = input("Which one do you want your car have?\n>> ")
        
        
        
        
print(Car_Maker.__doc__)
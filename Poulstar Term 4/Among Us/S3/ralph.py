class Car_Maker:
    """
Kinds : 9 Cars :'White','Black','Blue','Green','Red','Indigo','Violet','Yellow','Orange'
Owner : The name of the owner
must : 'Flour','Sugar','Milk','Chocolate','Eggs'
must_not : 'Fire Hydrant','Shoes','Plumber','Traffic Cones'
Decorating : 'Strawberry Oreo', 'Red Cream', 'Mentos', 'Jelly Beans'
    """

    def __init__(self, owner, kind, first_color, second_color):
        self.kind = kind
        self.owner = owner
        self.first_color = first_color
        self.second_color = second_color

    def mixing(self):
        must = ["Flour", "Sugar", "Milk", "Chocolate"]
        user_ingredients = []
        while True:
            for ingredient in must:
                print(ingredient)
            user_selected = input("Which one do you want your car have?\n>> ")
            user_ingredients.append(user_selected)
            user_choice = input("Continue?(Y/N)\n>> ").upper()
            if user_choice.startswith("Y") or user_choice.startswith("ARE") or user_choice.startswith("OUI"):
                continue
            else:
                break
        for user_ingredient in user_ingredients:
            print(user_ingredient)

    def baking(self, user_degree):
        degree_levels = range(100, 220)
        if 165 <= user_degree <= 180:
            print("Your car is baking...👍😁")
        elif user_degree > 180:
            print("Your car has been burnt!🔥")
        else:
            print("We can't bake your car!💧")

    def decorating(self):
        user_chosen = []
        ingredients = ("Strawberry Oreo", "Red Cream", "Mentos", "Jelly Beans")
        for ingredient in ingredients:
            print(f"Decorator : {ingredient}")
        while True:
            user_decorating = input("What do you want to add to your car?\n>> ").title()
            if user_decorating in ingredients:
                user_chosen.append(user_decorating)
            else:
                print("You haven't chosen the right ingredient")
            deciding = input("Do you want to continue? ")
            if deciding.startswith("y"):
                continue
            elif deciding.startswith("n"):
                break
        return user_chosen
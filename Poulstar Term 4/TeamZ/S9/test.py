from os import system
system("cls")
Protein = {
    "Medium chicken breast" : 172,
    "Medium chicken wings" : 222,
    "Medium chicken thigh" : 211,
    "Turkey meat" : 112,
    "Turkey breast" : 157,
    "Turkey thigh" : 144,
    "Ostrich thigh" : 111,
    "Ostrich fillet" : 123,
    "Quail meat" : 192,
    "Dock meat" : 404,
    "Goose meat" : 161,
    "Pheasant meat" : 181,
    "Thigh of lamb" : 201,
    "Straight lamp meat" : 134,
    "Lamp ribs" : 161,
}
Rice = {
    "Cooked white rice(100g)" : 120,
    "Raw white rice(100g)" : 130,
}
The_vegetables = {
    "An onion (1 piece)" : 44,
    "Cauliflower(100g)" : 25,
    "Broccoli(88g)" : 25,
    "Medium potatoes(1 piece)" : 164,
    "Medium sweet potato(1 piece)" : 112,
    "Medium radish(1 piece)" : 1,
    "Chopped parsley(4g)" : 1,
    "Cress(50g)" : 16,
    "Medium carrot(1 piece)" : 30,
    "Chopped ginger(24g)" : 19,
    "1 clove of garlic" : 3,
    "Chopped onion(25g)" : 10,
    "Medium cucumber(100g)" : 15,
    "tomato(100g)" : 17,
    "Chopped celery(120g)" : 19,
    "Spinach(30g)" : 7,
    "Chopped mushrooms(70g)" : 15,
    "Chopped pumpkin(116g)" : 30,
    "Peeled eggplant(450g)" : 110,
}
Beans = {
    "Cooked peas(100g)" : 18,
    "Baked pinto beans(100g)" : 143,
    "Baked black beans(100g)" : 132,
    "Green beans(100g)" : 31,
    "White cowpea(100g)" : 85,
    "Baked red beans(100g)" : 127,
    "Raw red beans(100g)" : 333,
    "Baked white beans(100g)" : 139,
    "Raw white beans(100g)" : 333,
    "Cooked cobs(100g)" : 118,
    "Raw cobs(100g)" : 340,
    "Cooked lentils(100g)" : 116,
    "Raw lentils(100g)" : 353,
    "Cooked peas(100g)" : 164,
    "Raw chickpeas(100g)" : 364,
    "Cooked mung bean(100g)" : 105,
    "Raw mung bean(100g)" : 347,
}
Dairy = {
    "Parmesan cheese(100g)" : 431,
    "Cheddar cheese(130g)" : 532,
    "Cream cheese(230g)" : 810,
    "Cheddar cheese(200g)" : 705,
    "Mozzarella cheese(112g)" : 336,
    "Cream(120g)" : 414,
    "Full fat milk(245g)" : 146,
    "Skimmed milk()245g" : 86,
    "Low-fat milk(244g)" : 102,
    "Butter(227g)" : 1628,
    "Fatty yogurt(245g)" : 149,
    "Low fat yogurt(245g)" : 137,
}

energy = 0

username = input("""Hello, welcome.
Next,you can see the calories of your favorite foods.
To get started, please enter the information below.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Username: """).title()

print(f"Welcome dear {username}.")
while 1:
    user_ingredient = input("From which group do you want to add some ingredients?\nif you want to end the code at any time, use the finish sentence.\nProtein\nRice\nThe_vegetables\nBeans\nDairy\n>> ").title()
    if user_ingredient.startswith("P"):
        ingredients = tuple(Protein.keys())
        for member in range(len(ingredients)):
            print(f"{member+1} : {ingredients[member]}")
        user_ingredient = input("Which one do you want to add? ")
        if user_ingredient in ingredients:
            energy += Protein[user_ingredient]
        else:
            print("The entered ingredient doesn't exist!")
    elif user_ingredient.startswith("R"):
        ingredients = tuple(Rice.keys())
        for member in range(len(ingredients)):
            print(f"{member+1} : {ingredients[member]}")
        user_ingredient = input("Which one do you want to add? ")
        if user_ingredient in ingredients:
            energy += Rice[user_ingredient]
        else:
            print("The entered ingredient doesn't exist!")
    elif user_ingredient.startswith("T"):
        ingredients = tuple(The_vegetables.keys())
        for member in range(len(ingredients)):
            print(f"{member+1} : {ingredients[member]}")
        user_ingredient = input("Which one do you want to add? ")
        if user_ingredient in ingredients:
            energy += The_vegetables[user_ingredient]
        else:
            print("The entered ingredient doesn't exist!")
    elif user_ingredient.startswith("B"):
        ingredients = tuple(Beans.keys())
        for member in range(len(ingredients)):
            print(f"{member+1} : {ingredients[member]}")
        user_ingredient = input("Which one do you want to add? ")
        if user_ingredient in ingredients:
            energy += Beans[user_ingredient]
        else:
            print("The entered ingredient doesn't exist!")
    elif user_ingredient.startswith("D"):
        ingredients = tuple(Dairy.keys())
        for member in range(len(ingredients)):
            print(f"{member+1} : {ingredients[member]}")
        user_ingredient = input("Which one do you want to add? ")
        if user_ingredient in ingredients:
                energy += Dairy[user_ingredient]
        else:
                print("The entered ingredient doesn't exist!")
                
    user_selection = input("Do you want to end the program? ").title()
    if user_selection.startswith("Y"):
        break
# print(f"The consumed energy : {energy}") 
with open("consumption.txt","w") as file:
    file.write(f"The consumed energy : {energy}")
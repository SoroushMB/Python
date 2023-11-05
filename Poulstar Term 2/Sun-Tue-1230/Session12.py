# Lasagna : Ingredients - Preparation Time : 20 mins - Baking Time : 40 mins
def mavad():
    ingredients = ["Meat",
                "Mushroom",
                "Cheese",
                "Fried-Onion",
                "Potato (Optional)",
                "Pasta Layer",
                "Tomato Paste",
                "Spice"]
    for i in range(len(ingredients)):
        print(f"{i+1}: {ingredients[i]}")

def making_time(count):
    return count * 60

time_of_preparation = making_time(count=6)
print(f"Your order will take {time_of_preparation} mins to prepare!")
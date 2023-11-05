fruits = {
    "Apple" : 130,
    "Avocado" : 50,
    "Banana" : 110,
    "Kiwifruit" : 90,
    "Pear" : 100,
    "Sweet Cherries" : 100
}
user_selected_fruit = input("Item: ").strip().title()
if user_selected_fruit in fruits:
    print(f"Calories: {fruits[user_selected_fruit]}")

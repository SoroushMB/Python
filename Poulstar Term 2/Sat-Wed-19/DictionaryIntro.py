# Dictionaries
# Saman : if - for
fruits = {
    # key : value --> item
    "Apple" : 56,
    "Banana" : 84,
    "Watermelon" : 31,
    "Pineapple" : 53
}

fruits_list = list(fruits.keys())
for fruit in fruits_list:
    print(fruit)
    
user_fav_fruit = input("Your favorite fruit : ")
print(fruits[user_fav_fruit])

user_answer = input("Do you want to add more fruits (Yes/No): ")

if user_answer == "Yes":
    fruit = input("What do you want to add : ")
    energy = input("How much energy does it have : ")
    fruits.update({fruit : energy})
    fruits_list = list(fruits.keys())
    for fruit in fruits_list:
        print(fruit)
elif user_answer == "No":
    print("Ok, there will be no new fruits added to the dictionary!")
    cleaning = input("What do you want to delete from dictionary : ")
    fruits.pop(cleaning)
    fruits_list = list(fruits.keys())
    for fruit in fruits_list:
        print(fruit)    
else:
    print("You have chosen a wrong")
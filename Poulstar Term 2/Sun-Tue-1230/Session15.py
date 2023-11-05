# cars = ["Nissan","Mercedes-Benz","BMW"]
# for car in cars:
#     print(car)

# user_choice = input("How do you wish to delete your item?'Index / Element'\n>> ").lower()

# if user_choice.startswith("e"):
#     element = input("Which one do you wish to delete?\n>> ")
#     cars.remove(element)
#     for item in cars:
#         print(item)
# elif user_choice.startswith("i"):
#     user_index = int(input("Which one do you wish to delete?\n>> "))
#     cars.pop(user_index)
#     for item in cars:
#         print(item)
user_input = input("camelCase: ")
for letter in user_input:
    if letter.isupper():
        user_input = user_input.replace(letter,f"_{letter.lower()}")
print(f"snake_case: {user_input}")
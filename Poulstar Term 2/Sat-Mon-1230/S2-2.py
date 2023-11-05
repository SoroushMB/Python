# print(f"Hello, {username}! Welcome to our program {username}!")
# String Methods : Lower , Upper , Capitalize , Title , Replace
username = input("What's your name : ").capitalize()
# password = input("What's your password : ").upper()
# print(f"Password : {password}")
book = input("What is your favorite book : ").title().replace(" ","n")
print(book)
age = int(input("How old are you? "))
print(f"{username} is {age} years old!")
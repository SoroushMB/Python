from sys import exit

user_number = int(input(">> "))

if user_number > 10:
    exit("The user's input was greater than 10!")
elif user_number < 10: 
    exit("The user's input was less than 10!")
else:
    exit("The user has inputted exactly the number 10!")

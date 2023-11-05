# Conditionals
# If,Elif,Else
number1 = int(input("Enter first number >> "))
number2 = int(input("Enter second number >> "))

if number1 > number2: # True
    print("The first one is greater than the second one!")
elif number2 > number1: # False
    print("The second one is greater than the first one!")
else:
    print("They are equal")

# Function = تابع
# Define = تعریف کردن
# Global = سراسری
# Built-in , User-Defined
def sum(number1,number2):
    return number1 + number2
first_number = int(input("Enter your number : "))
second_number = int(input("Enter your number : "))
print(sum(number1=first_number,number2=second_number))
# String Methods : Lower - Upper - Capitalize - Replace - Title
name = input("What is your name : ").title().replace(" ","")
print(name)
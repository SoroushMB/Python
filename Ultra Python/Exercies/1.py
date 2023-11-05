def main():
    user_selection = input("Sum | Multiply : ")
    if user_selection == "sum":
        print(sum(number1=int(input(">>")),number2=int(input(">>"))))
    elif user_selection == "multiply":
        print(multiply(number1=int(input(">>")),number2=int(input(">>"))))

def sum(number1 : int,number2 : int):
    return number1 + number2

def multiply(number1 : int,number2 : int):
    return number1 * number2

main()
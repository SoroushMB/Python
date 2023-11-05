def main():    
    user_equation = input("Equation : ")
    first_number,symbol,second_number = user_equation.split()
    if symbol == "+":
        print(f"Result : {int(first_number) + int(second_number)}")
    elif symbol == "-":
        print(f"Result : {int(first_number) - int(second_number)}")
    elif symbol == "/":
        print(f"Result : {int(first_number) / int(second_number)}")
    elif symbol == "*":
        print(f"Result : {int(first_number) * int(second_number)}")
main()
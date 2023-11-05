def main():
    user_number = int(input("Number: "))
    validate = valid(number=user_number)
    if validate:
        print("Even")
    else:
        print("Odd")

def valid(number):
    if number % 2 == 0:
        return True
    else:
        return False

main()

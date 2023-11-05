def main():
    user_number = int(input("Number: "))
    valid(number=user_number)

def valid(number):
    print("Even") if number % 2 == 0 else print("Odd")

main()

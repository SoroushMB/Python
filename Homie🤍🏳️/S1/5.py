def main():
    user_number = int(input("Number: "))
    valid(number=user_number)

def valid(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

main()

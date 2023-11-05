def main():
    user_number = int(input("Your number : "))
    if is_even(number=user_number) == True:
        print("Even")
    else:
        print("Odd")

def is_even(number):
    if number % 2 == 0: # True
        return True
    else:
        return False

main()
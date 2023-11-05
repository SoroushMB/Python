def main():
    user_number = int(input("Your number : "))
    if is_even(number=user_number) == True:
        print("Even")
    else:
        print("Odd")

def is_even(number):
    return number % 2 == 0 # 0 : False - 1 : True

main()
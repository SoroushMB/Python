def main():
    user_number = int(input("Enter number : "))
    example_num = is_even(number=user_number)
    if example_num == 0:
        print("Number is even!")
    else:
        print("Number is odd!")

def is_even(number:int):
    return int(number) % 2

if __name__ == "__main__":
    main()
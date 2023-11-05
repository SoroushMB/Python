def main():
    sum(user_number=int(input("Enter your number : ")))

def sum(user_number):
    for number in range(user_number):
        result = number
        result += number - 1
        if result != -1:
            print(f"The current number is {number} and the sum result is {result}")
main()

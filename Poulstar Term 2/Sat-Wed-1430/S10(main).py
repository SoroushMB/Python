def greeting(n):
    for i in range(n):
        name = input("What's your name? ")
        age = int(input("How old are you? "))
        print(f"{name} is {age} years old!")
for i in range(3):
    greeting(n=3)
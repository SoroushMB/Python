def main():
    saying_meow(count=get_a_number()) #count=number
    print("Finished!")

def get_a_number():
    while True:
        number = int(input("How many times do you want to 'meow'? "))
        if number > 0:
            return number

def saying_meow(count):
    for _ in range(count):
        print("meow")

main()
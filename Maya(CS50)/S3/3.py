def main():
    user_number = get_num() # user_number = user_input
    print(f"Number is {user_number}")

def get_num():
    while True:
        try:    
            return int(input(">> "))
        except ValueError:
            pass

main()
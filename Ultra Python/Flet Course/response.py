import validators

def main():
    print(validator(input("What's your email address? ")))

def validator(email):
    return "Valid" if validators.email(email) == True else "Invalid"

if __name__ == "__main__":
    main()
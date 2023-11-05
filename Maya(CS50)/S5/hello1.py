def main():
    name = input("What's your name? ")
    print(hello(to=name))
    
def hello(to):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()
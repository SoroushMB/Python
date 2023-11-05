def main():
    x = int(input("What's x? "))
    squared = square(n=x)
    print(f"x squared is {squared}")

def square(n):
    return n**2

if __name__ == "__main__":
    main()
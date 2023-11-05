def main():
    print(tip())
    
def tip():
    price = input(">> ")
    return f"{price}$"

if __name__ == "__main__":
    main()
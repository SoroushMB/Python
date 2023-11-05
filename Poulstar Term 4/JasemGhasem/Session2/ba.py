def main():
    alaki = info()
    name,house = alaki[0],alaki[1]
    print(f"{name} from {house}")

def info():
    return (input("House : "),input("Name : "))
if __name__ == "__main__":
    main()
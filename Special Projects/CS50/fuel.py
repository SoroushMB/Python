def main():
    while True:
        user_input = input("Fraction: ")
        result = gauge(percentage=user_input)
        if result is not None:
            break
    if 2 > result >= 0:
        print("E")
    elif result > 98:
        print("F")
    else:
        print(f"{result}%")


def convert(fraction:str) -> tuple:
    while True:
        try:
            x,y = fraction.split("/")
            if int(x) <= int(y):
                return (int(x),int(y))
            else:
                break
        except ValueError:
            break   


def gauge(percentage:tuple):
    while True:
        everything = convert(fraction=percentage)
        try:
            return int(round(number=everything[0]/everything[1],ndigits=2)*100)
        except Exception:
            break


if __name__ == "__main__":
    main()
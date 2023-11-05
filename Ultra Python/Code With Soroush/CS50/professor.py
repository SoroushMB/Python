from contextlib import suppress
from random import randint


def main():
    level = get_level()
    score = main_game(level=level)
    print(f"Score: {score}")


def get_level():
    while True:
        with suppress(Exception):
            getting_level = int(input("Level: "))
            if getting_level in {1, 2, 3}:
                break
    return getting_level


def generate_integer(level):
    match level:
        case 1:
            x, y = randint(0, 9), randint(0, 9)
        case 2:
            x, y = randint(10, 99), randint(10, 99)
        case _:
            x, y = randint(100, 999), randint(100, 999)
    return x, y


def generate_round(x: int, y: int):
    tries = 1
    while tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            result = x + y
            if answer == result:
                return True
            tries += 1
            print("EEE")
        except Exception:
            tries += 1
            print("EEE")
    print(f"{x} + {y} = {result}")
    return False


def main_game(level):
    score = 0
    for _ in range(1, 11):
        x, y = generate_integer(level)
        response = generate_round(x, y)
        if response == True:
            score += 1
    return score


if __name__ == "__main__":
    main()

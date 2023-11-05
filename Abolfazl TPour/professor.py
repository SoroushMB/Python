import random
import sys

def main():
    level = get_level()
    equation_counter = 0
    user_score = 0
    while equation_counter <= 10:
        equation_counter += 1    
        generated_equation = generate_integer(level=level)
        user_answer_counter = 0
        try:
            while True:
                user_answer = int(input(f"{generated_equation[0]} + {generated_equation[1]} = "))
                real_answer = generated_equation[2]
                if user_answer == real_answer:
                    user_answer_counter += 1
                    user_score += 1
                    break
                else:
                    user_answer_counter += 1
                    print("EEE")
                    if user_answer_counter == 3:
                        break
                    else:
                        continue
        except ValueError:
            print("EEE")
            user_answer_counter += 1
            if user_answer_counter == 3:
                print(f"{generated_equation[0]} + {generated_equation[1]} = {generated_equation[2]}")
                break
            else:
                continue
    print(f"Score: {user_score}")
    sys.exit()

def get_level():
    while True:
        try:
            user_input = int(input("Level: "))
            if user_input in {1,2,3}:
                return user_input
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):  # sourcery skip: extract-duplicate-method
    if level == 1:
        X = random.randint(0,9)
        Y = random.randint(0,9)
        return X,Y,X+Y
    elif level == 2:
        X = random.randint(10,99)
        Y = random.randint(10,99)
        return X,Y,X+Y
    elif level == 3:
        X = random.randint(100,999)
        Y = random.randint(100,999)
        return X,Y,X+Y
    
if __name__ == "__main__":
    main()
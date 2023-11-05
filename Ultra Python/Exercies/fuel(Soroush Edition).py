def main():
    final_result = result()
    if final_result > 0.9:
        print("F")
    elif final_result < 0.1:
        print("E")
    else:
        print(f"{final_result}%")
def result():
    while True:
        user_input = input("Fraction: ").replace("/"," / ")
        X,symbol,Y = user_input.split()
        try:
            fraction = int(X) / int(Y)
            if X > Y:
                continue
            break
        except (ValueError,ZeroDivisionError):
            continue
    return fraction * 100
main()
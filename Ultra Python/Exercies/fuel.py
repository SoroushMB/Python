# 1/5 -> 012
while True:
    num = input("Fraction: ")
    index = num.find("/") # index = 1 -> 2
    try:
        x = int(num[:index]) # x = int(num[:1])
        y = int(num[index+1:])
        fraction = x / y
        if x > y:
            continue
        break
    except (ValueError,ZeroDivisionError):
        continue

percentage = fraction * 100

if fraction > 0.9:
    print("F")
elif fraction < 0.1:
    print("E")
else:
    print(f"{str(percentage)}%")
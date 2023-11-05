numbers = [12,15,18,14]
number = 0
for i in numbers:
    if number < i:
        number = i
    elif number == i:
        continue
    else:
        continue
print(number)
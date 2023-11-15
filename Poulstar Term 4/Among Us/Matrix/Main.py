# print(f" | 1 2 3")
# print(f"--------")
# print(f"1| {number}")
# print(f"")
number = "9 5 7"
counter = 0

def validation(number):
    global counter
    for digit in number:
        if digit.isdigit() == False:
            counter += 1
        
    if counter == 2:
        return number
    else:
        return "Not compatible!"

print(validation(number=number))
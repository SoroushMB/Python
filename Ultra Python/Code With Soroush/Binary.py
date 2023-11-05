user_binary : str = input("Enter your binary code : ")
binary_list : list = list(user_binary)
length_of_list = len(binary_list) # Count of Bits
converted_list : list = []
counter = 0
decimal_number = 0

for number in range(length_of_list):
    powered = 2**number
    converted_list.append(powered)

for i in binary_list:
    counter += 1
    match i:
        case "1":
            decimal_number += converted_list[length_of_list-counter]
        case "0":
            continue
print(decimal_number)
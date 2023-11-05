user_binary = input("Enter your binary code: ")
decimal_number = 0

for bit in user_binary:
    decimal_number = (decimal_number << 1) + int(bit)
print(decimal_number)
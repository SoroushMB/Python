number1 = 0
number2 = 1

# 2 -> 10 : (1 0 0 0 1 0 -> 34)
# 8 -> 10
# 16 -> 10 : 0123456789abcdef -> 0fa -> 11111010 -> 128+64+32+16+8+2 = 250
# 8 -> 2 : 01234567
# NAND -> Not-AND
if not(number1 == 0 and number2 == 1):
    print("Yes")
else:
    print("No")
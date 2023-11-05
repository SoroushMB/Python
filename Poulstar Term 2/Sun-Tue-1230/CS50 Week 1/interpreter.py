# 60 + 50
num1,symbol,num2 = input("Expression: ").split(" ")

if symbol == "+":
    print(int(num1) + int(num2))
elif symbol == "-":
    print(int(num1) - int(num2))
elif symbol == "/":
    print(int(num1) / int(num2))
elif symbol == "*":
    print(int(num1) * int(num2))
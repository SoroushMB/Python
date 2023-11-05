user_equation = input("Expression: ")

x,y,z = user_equation.split(" ")

# if y == "+":
#     result = x + y 
#     print(f"{float(result):.1f}")
# elif y == "-":
#     result = x - y 
#     print(f"{float(result):.1f}")
# elif y == "*":
#     result = x * y 
#     print(f"{float(result):.1f}")
# elif y == "/":
#     result = x / y 
#     print(f"{float(result):.1f}")

match y:
    case "+":
        result = x + y 
        print(f"{float(result):.1f}")
    case "-":
        result = x - y 
        print(f"{float(result):.1f}")
    case "*":
        result = x * y 
        print(f"{float(result):.1f}")
    case "/":
        result = x / y 
        print(f"{float(result):.1f}")

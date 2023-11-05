user_equation = input("Expression: ")
x,y,z = user_equation.split(" ")
x,z = int(x),int(z)

if y == "+":
    print(f"{float(x + z):.1f}")
elif y == "-":
    print(f"{float(x - z):.1f}")
elif y == "*":
    print(f"{float(x * z):.1f}")
elif y == "/":
    print(f"{float(x / z):.1f}")
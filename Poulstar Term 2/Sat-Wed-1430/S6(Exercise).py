# temp = int(input("What is the temprature outside : "))
# if temp<=20:
#     print("The weather is cold!")
# elif 20 < temp < 40:
#     print("The weather is okay outside!")
# else:
#     print("Please stay at your home!")
# print("The weather is cold outside!") if temp <= 20 else print("Please stay at your home!")
# --------------------------------------------------------------------------------------------------------------------------------------------
number1 = int(input(">> "))
number2 = int(input(">> "))
operator = input("What do you want to do (Plus,Minus,Multiply,Division)>> ").capitalize()

if operator == "Plus":
    print(f"Result : {number1+number2}")
elif operator == "Minus":
    print(f"Result : {number1-number2}")
elif operator == "Multiply":
    print(f"Result : {number1*number2}")
elif operator == "Division":
    print(f"Result : {number1/number2}")
else:
    print("Boro tuye kooche!")
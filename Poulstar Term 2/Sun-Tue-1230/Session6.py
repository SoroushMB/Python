# $40 , 10% -> $4 Tip
# price = float(input("How much was the meal? ").replace("$",""))
# tip = float(input("What percentage would you like to tip? ").replace("%","")) / 100
# result = (price * tip)+price

# print(f"Leave ${result}!")
# Variable : name = value
# Function : parameter = argument
def main():
    money = input("How much was the meal? ")
    tip = input("What percentage would you like to tip? ")
    final_price = (percent_to_float(percent=tip) * dollar_to_float(dollar=money)) + dollar_to_float(dollar=money) 
    print(f"Leave ${final_price:.2f}")

def percent_to_float(percent):
    return float(percent.replace("%",""))/100
    
def dollar_to_float(dollar):
    return float(dollar.replace("$",""))

main()
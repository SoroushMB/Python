# Tip Calculator
# Meal : $50 , Tip : 15% -> Leave $7.50
def main():
    user_meal_price = input("How much was the meal? ")
    user_tip_percent = input("What percentage would you like to tip? ")
    final_tip = gatherer(dollar=user_meal_price,percent=user_tip_percent)
    print(f"Leave ${final_tip:.2f}")

def gatherer(dollar,percent):
    percent = float(percent.replace("%","")) / 100
    dollar = float(dollar.replace("$",""))
    result = percent * dollar
    return result

main()
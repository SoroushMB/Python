# 50 , int(10%) -> $5
def main():
    food_price = float(input("How much was your meal? ").replace("$",""))
    tip = float(input("What percentage would you like to tip? ").replace("%",""))/100
    final_result = tip*food_price
    print(f"Leave ${final_result}")
main()
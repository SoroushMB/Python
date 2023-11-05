def main():
    ump = input("How much was the meal? ")
    utp = input("What percentage would you like to tip? ")
    final_result = cal(dollar=ump , percent=utp)
    print(f"Leave ${final_result:.2f}")
    
def cal(dollar : str, percent : str) -> float:
    dollar = float(dollar.replace("$",""))
    percent = float(percent.replace("%","")) / 100
    result = dollar * percent
    return result

main()
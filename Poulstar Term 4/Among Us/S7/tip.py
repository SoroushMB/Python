def main():
    dollars = convert_to_float(input("How much was the meal? "),input("What percentage would you like to tip? "))
    tip = dollars[0] * dollars[1]
    print(f"Leave ${tip:.2f}")

def convert_to_float(d,p):
    return (float(d.replace("$","")),float(p.replace("%",""))/100)

main()
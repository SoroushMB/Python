from json import load

with open("test.json","r") as file:
    something = load(file)

model = input(">> ")
price = something[model]["Price"]
if price:
    print(f"Money : ${price}")
else:
    print("Nothing!")
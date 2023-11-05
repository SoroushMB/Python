from json import loads

with open("cars.json","r") as file:
    converted = file.read()
    
if "lamborghini" in converted:
    print("Yes, it exists!")
else:
    print("No, it doesn't exist!")
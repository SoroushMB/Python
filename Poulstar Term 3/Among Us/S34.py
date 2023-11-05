from json import load

with open("test.json","r") as file:
    data = load(file)
    
print(data["names"][0:2])
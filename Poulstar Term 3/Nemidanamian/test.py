# sourcery skip: sum-comprehension
name = "Arshia123"
counter = 0
for i in name:
    if i.isdigit():
        counter += 1
        name = name.replace(i,"")
if counter != 0:
    print(f"There is number in variable!\nCount of number: {counter}\nThe new name: {name}")
else:
    print("There isn't number in variable!")
    
names = ["a","b","c"]
if name in names:
    ...
names = []

for i in range(3):
    user = input(">> ")
    names.append(user)
for name in sorted(names):
    print(f"Hello, {name}")
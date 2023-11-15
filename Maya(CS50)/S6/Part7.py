names = []
with open("Part3.txt") as file:
    for khat in file:
        names.append(khat.rstrip())
for name in sorted(names):
    print(f"Hello, {name}")
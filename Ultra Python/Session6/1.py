names = []
with open("test.txt") as file:
    for line in file:
        names.append(line.rstrip())
# Hermione
for name in sorted(names):
    print(name)
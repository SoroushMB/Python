with open("Part3.txt") as file:
    khatha = file.readlines()
print(khatha)
for khat in khatha:
    print(f"Hello, {khat}")
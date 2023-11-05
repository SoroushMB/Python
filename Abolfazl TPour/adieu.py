import inflect

plural = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break
output = plural.join(names)
print(f"Adieu, adieu, to {output}")
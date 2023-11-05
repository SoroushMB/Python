import sys

counter = len(sys.argv)

if counter > 2:
    print("Too many args!")
elif counter < 2:
    print("Too few args!")
else:
    print(f"Hello, welcome to our program dear {sys.argv[1]}")
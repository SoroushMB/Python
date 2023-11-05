from sys import argv,exit

counter = len(argv)
if counter > 2:
    exit("Too many args!")
elif counter < 2:
    exit("Too few args!")
else:
    print(f"Hi, {argv[1]}")
    
print("Hello, World!")
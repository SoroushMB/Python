counter = 0
for i in range(1,32):
    if 31 % i == 0:
        counter += 1

if counter == 2:
    print("The number entered is a prime")
else:
    print("The number isn't prime!")
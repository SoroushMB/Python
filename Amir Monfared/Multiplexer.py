A0 = 0
A1 = 1
A2 = 2
A3 = 3

B0 = "00"
B1 = 11
B2 = 22
B3 = 33

E = str(input("Turn on or off the power(0/1) : "))
if E == "0":
    print("Nothing")
elif E == "1":
    T = str(input("What do you want to send(0/1) : "))
    if T == "0":
        number = int(input("Enter the one you want : "))
        if number == 0:
            print(A0)
        elif number == 1:
            print(A1)
        elif number == 2:
            print(A2)
        elif number == 3:
            print(A3)
    elif T == "1":
        number = int(input("Enter the one you want : "))
        if number == 0:
            print(B0)
        elif number == 1:
            print(B1)
        elif number == 2:
            print(B2)
        elif number == 3:
            print(B3)
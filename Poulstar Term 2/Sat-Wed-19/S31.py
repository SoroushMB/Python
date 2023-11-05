# Loops : For
# For + Range
for number in range( 11 ):
    print(number)
# For + String
name = input(">> ")
for word in name:
    print(word)
for number in range(0,11):
    print(f"{number}:Arsha!!!")
# For + List
names = ["Arsha","Sina","Arisa","Saman","Anahita","Koushan"]
for name in names:
    print(f"{name}❤️")
# While Function
while True:
    number1 , number2 = 10 , int(input(">> "))
    if number1 > number2:
        print("Avalie bozorgtare!")
        break
    else:
        continue
print("Halghe karesh tamoom shod!")
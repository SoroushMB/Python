# 3 Attempts for guessing number!
# Loops : For , While
# temp = 22
# if temp == 22:
#     print("First!")
# elif temp == 23:
#     print("Second!")
# if temp == 22:
#     print("Third!")
# exact_number = 35
# for ghasemi in range(10):
#     guessed_number = int(input("Number: "))
#     if guessed_number == exact_number:
#         print("You have guessed the right number!")
#         break
#     else:
#         print("Your guess was wrong!")
#         continue
for i in range(10,101,5):
    print(f"{i/5}:{i}")
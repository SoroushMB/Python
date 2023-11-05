score = int(input("Score: "))
# Chaining Comparisons
if 17 <= score <= 20:
    print("Grade A")
elif 14 <= score < 17:
    print("Grade B")
elif 12 <= score < 14:
    print("Grade C")
elif 10 <= score < 12:
    print("Grade D")
elif score < 10:
    print("Grade F!De de deee!")
else:
    print("Out of range!")
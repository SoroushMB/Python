score = 0
while True:
    user_word = input("Enter your word >> ")
    if "S" in user_word[0]:
        # score = score + 10
        score += 10
    elif user_word == "End":
        break
    else:
        continue
print(f"Score : {score}")

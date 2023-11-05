Score = 0
while True:
    user_input = int(input(">> "))
    if Score < 50:
        Score += user_input
        print(f"Score : {Score}")
    else:
        break
print("Finished!")
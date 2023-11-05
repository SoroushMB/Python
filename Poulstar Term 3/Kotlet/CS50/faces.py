emojis = {
    ":)" : "🙂",
    ":(" : "🙁"
}

user_input = input("")
if ":)" in user_input:
    user_input = user_input.replace(":)",f"{emojis[':)']}")
elif ":(" in user_input:
    user_input = user_input.replace(":(",f"{emojis[':(']}")
print(user_input)
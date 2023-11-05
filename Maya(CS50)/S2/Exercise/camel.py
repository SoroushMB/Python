# Snake Case : file_name <- Camel Case : fileName
def main():
    user_input = input("camelCase: ")
    for letter in user_input:
        if letter.isupper():
            user_input = user_input.replace(letter,f"_{letter.lower()}")
    print(f"snake_case: {user_input}")
main()
# fileName -> f i l e _n a m e -> snake_case = file_name
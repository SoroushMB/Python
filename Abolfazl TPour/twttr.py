def main():
    text = input("Input: ")
    print(shorten(text))
def shorten(word):
    vowels = ["a","e","i","o","u"]
    new_text = "".join(word[i] for i in range(len(word)) if word[i].lower() not in vowels)
    return new_text

if __name__ == "__main__":
    main()
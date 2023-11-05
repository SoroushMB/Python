def main():
    print(shorten(word="Hello"))

def shorten(word):
    letter_vowels = ("a","e","i","o","u")
    for letter in word:
        if letter in letter_vowels:
            word = word.replace(letter,"")
    return word

if __name__ == "__main__":
    main()
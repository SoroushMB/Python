def main():
    even(input(">> "))
def even(word):
    for i in range(len(word)):
        if i%2 == 0:
            print(word[i])
main()
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    for letter in s:
        if not letter.isalpha():
            if letter == "0":
                return False
            else:
                break

    return all(c not in ["."," ","!","?"] for c in s)

main()
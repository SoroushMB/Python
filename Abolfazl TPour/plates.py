def main():
    plate = input("Plate: ")
    if is_valid(s=plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    bibin = 0
    while bibin < len(s):
        if s[bibin].isalpha() == False:
            if s[bibin] == "0":
                return False
            elif s[bibin:].isdigit() == False:
                return False
            else:
                break
        print(s[bibin])
        bibin += 1
    for barikala in s:
        if barikala in ["."," ","!","?"]:
            return False
    return True
main()
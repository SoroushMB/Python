def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    counter = 0
    if s[0:2].isalpha():
        counter += 1
    else:
        counter -= 1
    
    if 2 <= len(s) <= 6:
        counter += 1
    else:
        counter -= 1
    
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] != "0":
                if s[i:].isdigit():
                    counter += 1
                    break
                else:
                    counter -= 1
                    break
            else:
                counter -= 1
                break

    punc_mark = ("!","?","-",","," ")
    for i in punc_mark:
        if i in s:
            counter -= 1
    else:
        counter += 1
    if counter == 4:
        return True
    else:
        return False

main()
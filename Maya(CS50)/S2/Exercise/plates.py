def main():
    user_plate = input("Plate: ")
    if is_valid(plate=user_plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if 2 <= len(plate) <= 6 and plate.isalnum():
        if plate.isalpha():
            return True
        else:
            if plate[:2].isalpha() and plate[-2:].isdigit():
                for i in range(len(plate)):
                    if plate[i].isdigit():
                        if plate[i].startswith("0") or plate[i:].isalpha():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False

main()

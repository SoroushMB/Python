# Scope : A space which is limited to certain area of a program like functions & classes
# Outer Scope - Inner Scopes
# Outer Scope
# Nonlocal
name = "AmirTaha"

def greeting():
    # Inner Scope greeting function

    other_name = "Soroush"
    other_lastname = "Masoum Babaei"

    def joining():
        # Upper Scope
        nonlocal other_name,other_lastname
        new_name = f"{other_name} {other_lastname}"
        return new_name

    print(joining())

greeting()
from calculator0 import square

def main():
    test_square()
    
def test_square():
    if square(2) == 4:
        print("2 squared was 4!")
    if square(100) == 10000:
        print("100 squared was 10000!")

if __name__ == "__main__":
    main()
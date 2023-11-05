from calculator0 import square

def main():
    test_squared()
    
def test_squared():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared wasn't 4!")
    try:    
        assert square(100) == 10000
    except AssertionError:
        print("100 squared wasn't 10000!")
        
    
if __name__ == "__main__":
    main()
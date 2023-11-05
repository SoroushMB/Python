from calculator0 import square

def main():
    test_squared()
    
def test_squared():
    assert square(2) == 4
    assert square(100) == 10000
    
if __name__ == "__main__":
    main()
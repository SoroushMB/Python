from twttr import shorten

def main():
    test_twttr()
    
def test_twttr():
    assert shorten("hello") == "hll"
    assert shorten("23") == "23"

if __name__ == "__main__":
    main()
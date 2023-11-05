from hello1 import hello

names = ["Maya","Soroush","Kourosh"]

def test_hamintori():
    for name in names:
        assert hello(name) == f"Hello, {name}"
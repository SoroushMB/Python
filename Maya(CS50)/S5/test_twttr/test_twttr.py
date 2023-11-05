from twttr import shorten
def test_part_one():
    assert shorten("Auto") == "t"
    assert shorten("HELLO") == "HELLO"
    assert shorten("Hello") == "Hll"
    assert shorten("CS50") == "CS50"
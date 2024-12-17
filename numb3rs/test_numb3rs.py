from numb3rs import validate

def test_letters():
    assert validate("127.f.1.1") == False

def test_numbers():
    assert validate("275.122.3.2") == False
    assert validate("1.122.275.2") == False
    assert validate("255.1.20.2") == True

def test_whitespace():
    assert validate("   1.1.1.1   ") == False


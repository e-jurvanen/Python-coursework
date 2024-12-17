from bank import value

def test_lowercase():
    assert value("hello") == 0

def test_uppercase():
    assert value("Hi") == 20

def test_greeting():
    assert value("Greetings!") == 100

from plates import is_valid

def test_lenght():
    assert is_valid("C") == False
    assert is_valid("CS50") == True
    assert is_valid("ASDFGHJKL") == False

def test_start_letters():
    assert is_valid("50CS") == False
    assert is_valid("CSH50") == True
    assert is_valid("567") == False

def test_special_characters():
    assert is_valid("CS50!") == False
    assert is_valid("!CSH6") == False

def test_numbers():
    assert is_valid("CS50D") == False
    assert is_valid("CS05") == False

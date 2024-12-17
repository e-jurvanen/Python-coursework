from um import count

def test_ignorecase():
    assert count("HELLO, UM, PY") == 1
    assert count("hello, um , world") == 1
    assert count("um, hello, Um, world") == 2

def test_words():
    assert count("hello, um, umberella") == 1
    assert count("hi yummy") == 0

def test_characters():
    assert count("HELLO, um? how do you, um... do?") == 2

from twttr import shorten

def test_stripping():
    assert shorten("David") == "Dvd"

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_numbers():
    assert shorten("CS50") == "CS50"

def test_punctuation():
    assert shorten("twitter.com") == "twttr.cm"

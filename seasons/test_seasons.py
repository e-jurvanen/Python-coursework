from seasons import convert, words

def test_date():
    assert convert("2024-09-17") == "1440"

def test_words():
    assert words(1995) =="one thousand, nine hundred and ninety-five"

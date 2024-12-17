from project import validate


def test_length():
    assert validate("160972-054W") == True
    assert validate("160972-054") == False # too few character
    assert validate("160972-0541W") == False # too many characters


def test_date_and_seperator():
    assert validate("050780-1722") == True
    assert validate("051380-1722") == False # no 13th month, creates an IndexError
    assert validate("050780D1722") == False # not a valid seperator
    assert validate("290224A033K") == True # testing leap year


def test_ending():
    assert validate("050780-1722") == True
    assert validate("050780-172A") == False # correct ending would be 2
    assert validate("221109A283L") == False # correct ending would be H


def test_typos_errors():
    assert validate("A50780-1722") == False # beginning part can't contain letters
    assert validate("050780-A722") == False # only seperator and last character might be letters

from fuel import convert, gauge
import pytest

def test_convert_int():
    assert convert("1/3") == 33

def test_gauge_percent():
    assert gauge(33) == "33%"

def test_gauge_letter():
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_Errors():
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")



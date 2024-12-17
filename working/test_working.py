from working import convert
import pytest

def test_convert_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_convert_mins():
    assert convert("9:20 AM to 5:50 PM") == "09:20 to 17:50"
    assert convert("10:30 PM to 11:50 PM") == "22:30 to 23:50"

def test_error():
    with pytest.raises(ValueError):
        assert convert("9 to 5")
    with pytest.raises(ValueError):
        assert convert("9-00 to 5-00")
    with pytest.raises(ValueError):
        assert convert("9:65 AM to 5:00 PM")
    with pytest.raises(ValueError):
        assert convert("9 AM 5 PM")


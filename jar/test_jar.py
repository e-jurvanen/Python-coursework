from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(5)
    assert str(jar) =="🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.withdraw(8)


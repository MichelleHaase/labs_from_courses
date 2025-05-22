from jar import Jar
import pytest


def test_init():
    jar = Jar(capacity=10, size=5)
    assert jar.capacity == 10
    assert jar.size == 5


def test_capacity():
    with pytest.raises(ValueError):
        jar2 = Jar(capacity=-5)
    with pytest.raises(ValueError):
        jar2 = Jar(capacity="a")
    with pytest.raises(ValueError):
        jar2 = Jar(capacity="abcdf")
    with pytest.raises(ValueError):
        jar2 = Jar(capacity=5.3)


def test_str():
    jar = Jar(capacity=10, size=5)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(capacity=10, size=5)
    jar.deposit(5)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar(capacity=10, size=5)
    jar.withdraw(4)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)

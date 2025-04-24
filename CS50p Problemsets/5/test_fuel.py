import pytest

from fuel import gauge
from fuel import convert

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"

def test_convert():
    assert convert("1/3") == 33

def test_errors():
    with pytest.raises(ValueError):
        convert("1.3/3")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

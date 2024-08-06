from fuel import convert
from fuel import gauge

import pytest


def test_ve():
    with pytest.raises(ValueError):
        convert("sd")
        convert("s/d")
        convert("s/50")
    with pytest.raises(ValueError):
        convert("-5/10")
        convert("5/-3")
    with pytest.raises(ValueError):
        convert("1.5/3")
        convert("5/3")


def test_convert_ZeroDivisionErrors():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("3/0")

def test_convert():
    assert convert("1/4") == 25
    assert convert("99/100") == 99
    assert convert("1/100") == 1

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(30) == "30%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"

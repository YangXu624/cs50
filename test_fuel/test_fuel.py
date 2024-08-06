from fuel import convert
from fuel import gauge

import pytest


def test_convert_ValueErrors():
    with pytest.raises(ValueError):
        convert("cat/car")
        convert("12/3")
        convert("1")
        convert("  ")


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

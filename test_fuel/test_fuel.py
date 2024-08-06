from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("1/4") == 25
    assert convert("99/100") == 99
    assert convert("1/100") == 1

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(30) == "30%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"

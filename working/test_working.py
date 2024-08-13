from working import convert
import pytest

def test_convert():
    assert convert("10:35 AM to 9:00 PM") == "10:35 to 21:00"

def test_valueerror():
    with pytest.raises(ValueError):
        convert("10 AM - 12 PM")
        convert("27 AM to 29:09 PM")

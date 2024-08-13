from seasons import check
import pytest

def test_check():
    assert check("2022-08-14") == "One million, fifty-one thousand, two hundred minutes"

def test_fail():
    with pytest.raises(ValueError):
        check("okboomer")

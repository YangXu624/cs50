from plates import is_valid

def test_true():
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True


def test_false():
    assert is_valid("AA22YY") == False
    assert is_valid("C05YYY") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("HI.P") == False
    assert is_valid("12345") == False
    assert is_valid("ABC1234") == False

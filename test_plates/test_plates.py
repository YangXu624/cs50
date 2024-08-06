from plates import is_valid

def check_true():
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True

def check_false():
    assert is_valid("AA22YY") == False
    assert is_valid("C05YYY") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("HI.P") == False

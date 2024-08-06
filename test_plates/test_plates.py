from plates import is_valid

def check():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("HI.P") == False
    assert is_valid("AAA222") == True
    assert is_valid("AA22YY") == False
    assert is_valid("C05YYY") == False
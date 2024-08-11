from numb3rs import validate


def test_true():
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True

def test_false():
    assert validate("256.1.2.3") == False
    assert validate("yes.1.2.3") == False
    assert validate("25.1.1.2.3") == False
    assert validate("-9") == False

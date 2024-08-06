from bank import value

def test0():
    assert value("hello") == 0
    assert value("hello,") == 0
    assert value("hello!") == 0

def test20():
    assert value("hippo") == 20
    assert value("hi, whats up") == 20

def test100():
    assert value("morning") == 100

def test_case():
    assert value("HeLlO") == 0
    assert value("HIPPO") == 20
    assert value("ANythinG") == 100

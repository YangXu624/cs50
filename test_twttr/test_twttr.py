from twttr import shorten



def test_lower():
    assert shorten("dbaeioujk") == "dbjk"

def test_upper():
    assert shorten("ABCDEFIOU") == "BCDF"

def test_num():
    assert shorten("bd151523467890") == "bd151523467890

def test_punc():
    assert shorten("ok,.!?") == "k,.!?"

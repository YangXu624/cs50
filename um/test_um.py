from um import count

def test_count1():
    assert count("yum") == 0

def test_count2():
    assert count("um, um um um") == 4

def test_count3():
    assert count("Um, thanks, um...") == 2

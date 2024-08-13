from working import convert

def test_convert():
    assert convert("10:35 AM to 9:00 PM") == "10:35 to 21:00"

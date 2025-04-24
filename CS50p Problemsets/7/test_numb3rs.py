from numb3rs import validate

def test_words():
    assert validate("vat") == False
    assert validate("Hello World") == False
    assert validate("My name is") == False

def test_Sonderzeichen():
    assert validate("123.123.123.???") == False
    assert validate("123,123,123,122") == False
    assert validate("123!123?123-123") == False

def test_numbers():
    assert validate("123.123.123.123") == True
    assert validate("127.0.0.1") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("75.456.76.65") == False

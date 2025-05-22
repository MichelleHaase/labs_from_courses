from bank import value


def test_upper_lower():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("Hi") == 20
    assert value("hi") == 20
    assert value("Good Day") == 100
    assert value("good day") == 100


def test_numbers():
    assert value("123") == 100
    assert value("He3llo") == 20
    assert value("H3") == 20
    assert value("3Hello") == 100


def test_Sonderzeichen():
    assert value("Hello,.") == 0
    assert value("Hel,lo") == 20
    assert value("?Hello") == 100

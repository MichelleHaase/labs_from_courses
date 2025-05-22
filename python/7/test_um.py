from um import count


def test_singleWords():
    assert count("um") == 1
    assert count("umum") == 0
    assert count("um ") == 1
    assert count(" um") == 1
    assert count("yummy") == 0


def test_Sonderzeichen():
    assert count("um?") == 1
    assert count("um.") == 1
    assert count("um,") == 1
    assert count("um-") == 1


def test_numbers():
    assert count("1um") == 0
    assert count("um2") == 0
    assert count("um 2") == 1


def test_sentences():
    assert count("hello, um, world") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...,") == 2

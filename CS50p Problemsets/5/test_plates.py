from plates import is_valid


def test_known_right():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("H") == False
    assert is_valid("LA") == True
    assert is_valid("PI3.14") == False
    assert is_valid("123") == False


# def test_whitespace():
#     assert is_valid(" CS50 ") == True
#     assert is_valid("CS50   ") == True
#     assert is_valid("   CS50") == True


def test_numbers():
    assert is_valid("PI3.14") == False
    assert is_valid("123") == False


# def test_Len_limit():
#     assert is_valid("OUTATIME") == False
#     assert is_valid("LALILIK") == False


# def test_lowercase():
#     assert is_valid("cs50") == False
#     assert is_valid("la") == False


# def test_Sonderzeichen():
#     assert is_valid("CS?50") == False
#     assert is_valid("CS.50") == False
#     assert is_valid("LA:") == False

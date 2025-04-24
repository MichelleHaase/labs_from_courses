from working import convert
import pytest

def test_Sonderzeichen():
    with pytest.raises(ValueError):
        convert("05 AM - 06 PM")
    with pytest.raises(ValueError):
        convert("05 AM ? 06 PM")
    with pytest.raises(ValueError):
        convert("05 AM : 06 PM")
    with pytest.raises(ValueError):
        convert("05 AM . 06 PM")

def test_missingStuff():
    with pytest.raises(ValueError):
        convert("05 to 06 PM")
    with pytest.raises(ValueError):
        convert("05 AM to 06")
    with pytest.raises(ValueError):
        convert("05 AMto06 PM")

def test_wrongTime():
    with pytest.raises(ValueError):
        convert("100 AM to 06 PM")
    with pytest.raises(ValueError):
        convert("05 AM to 20 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 06 PM")
    assert convert("9 AM to 5 PM") == f"09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == f"09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == f"10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == f"22:30 to 08:00"
    # assert convert("10:30 PM to 8 AM  ") == f"22:30 to 08:00"
    # assert convert("  10:30 PM to 8 AM") == f"22:30 to 08:00"
    # assert convert("    10:30 PM to 8 AM") == f"22:30 to 08:00"

# def test_right_input():



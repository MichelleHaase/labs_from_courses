import pytest
import seasons

def test_dateformats():
    assert seasons.days("2024-11-05") == "One thousand, four hundred forty minutes"
    assert seasons.days("2023-11-06") == "Five hundred twenty-seven thousand forty minutes"
    assert seasons.days("2022-11-06") == "One million, fifty-two thousand, six hundred forty minutes"

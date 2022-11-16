from working import convert
import pytest

def test_normal():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM")=="22:30 to 08:50"

def test_another():
    assert convert("9:00 AM to 5:00 PM")=="09:00 to 17:00"

def test_else():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_wrong():
    with pytest.raises(ValueError):
        convert("9:00 - 5:00")

def test_empty():
    with pytest.raises(ValueError):
        convert(" to ")


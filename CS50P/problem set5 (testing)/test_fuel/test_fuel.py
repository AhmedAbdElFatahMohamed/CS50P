from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4")==75
def test_gauge():
    assert gauge(99)=='F'
    assert gauge(1)=='E'
    assert gauge(75)=='75%'
def test_str():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")



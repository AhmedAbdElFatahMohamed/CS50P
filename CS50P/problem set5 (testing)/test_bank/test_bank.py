from bank import value
import pytest

def test_zero():
    assert value("hello")==0
    assert value("Hello")==0

def test_20():
    assert value("hey")==20

def test_100():
    assert value("yo")==100
    assert value("good moning")==100
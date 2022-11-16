from um import count
import pytest

def test_1():
    assert count("yummy")==0

def test_2():
    assert count("Um hello")==1

def test_3():
    assert count("um thanks")==1
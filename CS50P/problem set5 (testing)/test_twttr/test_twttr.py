from twttr import shorten
import pytest

def test_lower():
        assert shorten("ahmed")=="hmd"
        assert shorten("twitter")=="twttr"

def test_upper():
    assert shorten("AHMED")=="HMD"

def test_num():
    assert shorten("1258")=="1258"

def test_punc():
    assert shorten(",.!")==",.!"
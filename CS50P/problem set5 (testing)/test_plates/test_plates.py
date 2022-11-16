from plates import is_valid

def test_Beg():
    assert is_valid("A7FG")==False
    assert is_valid("45CS")==False
    assert is_valid("AS435")==True
    assert is_valid("CS50")==True
    assert is_valid("6CQX")==False
    assert is_valid("HELLO")==True
    assert is_valid("A2")==False

def test_start():
    assert is_valid("ASDE")==True
    assert is_valid("C5SS")==False
    assert is_valid("ZX90")==True
    assert is_valid("AA22AA")==False

def test_alpha():
    assert is_valid("23pf")==False
    assert is_valid("AAA222")==True

def test_zero():
    assert is_valid("CS05")==False
    assert is_valid("A0ED")==False
    assert is_valid("CS50")==True

def test_punc():
    assert is_valid("cs.50")==False

def test_length():
    assert is_valid("ascvfghtuy")==False

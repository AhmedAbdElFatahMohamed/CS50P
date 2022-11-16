from hello import hello

def test_hello():
    for name in ["Harry","Hermoine","Draco"]:
        assert hello(name)==f"hello, {name}"
def test_default():
    assert hello()=="hello, world"
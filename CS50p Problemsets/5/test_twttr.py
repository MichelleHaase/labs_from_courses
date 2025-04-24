from twttr import shorten

def test_names():
    assert shorten("Lalao")== "Ll"
    assert shorten("LALOE")== "LL"
    assert shorten("LAle")== "Ll"
    assert shorten("LUlaIli")== "Lll"

def test_Sonderzeichen():
    assert shorten("Lala:,D")== "Ll:,D"
    assert shorten("Kla!ni?fu")== "Kl!n?f"

def test_numbers():
    assert shorten("La2l3a")== "L2l3"
    assert shorten("1256")== "1256"


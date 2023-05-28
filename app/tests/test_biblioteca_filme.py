import lib.biblioteca_filme as bfilme

def test_an_lansare():
    var = bfilme.an_lansare()
    if var == "2010" : 
        assert True
    else: 
        assert False
        

def test_rating():
    var = bfilme.rating()
    if var == "8.2" :
        assert True
    else: 
        assert False



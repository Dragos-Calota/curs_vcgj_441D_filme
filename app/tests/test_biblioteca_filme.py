import lib.biblioteca_filme as bfilme

def test_an_lansare():
    var = bfilme.an_lansare()
    if var == "1972" : 
        assert True
    else: 
        assert False
        

def test_rating():
    var = bfilme.rating()
    if var == "9.2" :
        assert True
    else: 
        assert False



import lib.biblioteca_filme as bfilme

def test_an_lansare_baywatch():
    var = bfilme.an_lansare_baywatch()
    if var == "2017" : 
        assert True
    else: 
        assert False
        

def test_rating_baywatch():
    var = bfilme.rating_baywatch()
    if var == "5.5" :
        assert True
    else: 
        assert False


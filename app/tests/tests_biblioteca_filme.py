import lib.biblioteca_filme as bfilme

def test_an_lansare_django():
    var = bfilme.an_lansare_django()
    if var == "2012" : 
        assert True
    else: 
        assert False
        

def test_rating_django():
    var = bfilme.rating_django()
    if var == "8.4" :
        assert True
    else: 
        assert False

